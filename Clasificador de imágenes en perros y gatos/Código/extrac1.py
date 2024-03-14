import numpy as np
import cv2
import copy
from sklearn.decomposition import PCA

def recorta_imagen(imagen, n):
    """
    Esta función recibe una imagen y un tamaño n y recorta la imagen de tal manera que el número final de 
    filas/columnas sea múltiplo de n.
    """
    i = imagen.shape[0]
    j = imagen.shape[1]
    if (i%n != 0): #Recortar filas
        dif = i%n
        imagen = imagen[0:i-dif,:]
    if (j%n != 0): #Recortar columnas
        dif = j%n
        imagen = imagen[:,0:j-dif]
    
    return imagen

def calculaBinario_N_VecinosMasCercanos(bloque):
    """
    Esta función recibe un bloque de píxeles. Calculará, desde el pixel central del bloque, 
    el valor en binario de convertir cada pixel a 0 o 1 según sea menor o mayor que él.
    """
    mascaraBinaria = [[128,64,32],[1,0,16],[2,4,8]]
    dif = len(bloque)//2
    valorPixelCentral = bloque[dif,dif]
    
    copiaBloque = copy.deepcopy(bloque) #Hace falta una copia para no cambiar el bloque original
    
    copiaBloque[copiaBloque < valorPixelCentral] = 0
    copiaBloque[copiaBloque >= valorPixelCentral] = 1
    
    return np.sum(np.multiply(copiaBloque,mascaraBinaria))

def calculaBinario_N_VecinosMasCercanos_Uniforme(bloque,diccionario):
    """
    Esta función recibe un bloque de píxeles. Calculará, desde el pixel central del bloque, 
    el valor en binario de convertir cada pixel a 0 o 1 según sea menor o mayor que él.
    Con tratamiento de transición uniforme
    """
    
    mascaraBinaria = [[128,64,32],[1,0,16],[2,4,8]]
    dif = len(bloque)//2
    valorPixelCentral = bloque[dif,dif]
    
    copiaBloque = copy.deepcopy(bloque) #Hace falta una copia para no cambiar el bloque original
    
    copiaBloque[copiaBloque < valorPixelCentral] = 0
    copiaBloque[copiaBloque >= valorPixelCentral] = 1
    copiaBloque = np.multiply(copiaBloque,mascaraBinaria)
    valorBinario = np.sum(copiaBloque)
    
    #Compruebo si es un número uniforme o no
    if(valorBinario in diccionario):
        valorBinario = diccionario[valorBinario]
    else:
        valorBinario = 58
    
    return valorBinario

def transforma_bloque(bloque):
    """
    Esta función recibe un bloque de píxeles y devuelve un bloque donde cada pixel ha sido sustituido
    por el valor en binario de sus vecinos.
    """
    dif = 1 #Solo cojo el vecindario de distancia 1
    bloquePrimo = np.zeros((len(bloque),len(bloque)))
    bloqueAmpliado = cv2.copyMakeBorder(bloque, dif, dif, dif, dif, cv2.BORDER_REPLICATE)
    
    for i in range(dif,len(bloqueAmpliado)-dif):
        for j in range(dif,len(bloqueAmpliado)-dif):
            bloquePrimo[i-dif,j-dif] = calculaBinario_N_VecinosMasCercanos(bloqueAmpliado[i-dif:i+dif+1,j-dif:j+dif+1])
        
    return bloquePrimo

def transforma_bloque_Uniforme(bloque,diccionario):
    """
    Esta función recibe un bloque de píxeles y devuelve un bloque donde cada pixel ha sido sustituido
    por el valor en binario de sus vecinos. Con tratamiento de transición uniforme
    """
    dif = 1 #Solo cojo el vecindario de distancia 1
    bloquePrimo = np.zeros((len(bloque),len(bloque)))
    bloqueAmpliado = cv2.copyMakeBorder(bloque, dif, dif, dif, dif, cv2.BORDER_REPLICATE)
    
    for i in range(dif,len(bloqueAmpliado)-dif):
        for j in range(dif,len(bloqueAmpliado)-dif):
            bloquePrimo[i-dif,j-dif] = calculaBinario_N_VecinosMasCercanos_Uniforme(bloqueAmpliado[i-dif:i+dif+1,j-dif:j+dif+1],diccionario)
        
    return bloquePrimo






#############################################################################################################################################################################################
#ESTAS FUNCIONES SON A LAS QUE SE LES PUEDE LLAMAR. LAS ESCRITAS MÁS ARRIBA SON SOLO
#FUCIONALES PARA ESTAS
#############################################################################################################################################################################################





def crear_vector_caracteristicas_BW(imagen, n):
    """
    Esta función recibe una imagen y un tamaño n y separa la imagen en bloques disjuntos de tamaño n*n. A cada uno de 
    estos les haré un tratamiento para obtener su histograma. Los uno y devuelvo el resultado. IMÁGENES BLANCO Y NEGRO
    : param imagen : imagen de la que obtener el vector
    : param n: tamaño de bloque
    """
    histogramas = np.array([])
    imagen = recorta_imagen(imagen,n)
    a = imagen.shape[0]
    b = imagen.shape[1]
    
    for i in range(int(a//n)):
        for j in range(int(b//n)):
            bloque = imagen[n*i:n*(i+1),n*j:n*(j+1)]
            bloque = np.uint8(transforma_bloque(bloque))
            h = cv2.calcHist([bloque], [0], None, [256], [0,256]).flatten()
            histogramas = np.concatenate((histogramas,h))
            
    return histogramas

def crear_vector_caracteristicas_color_1(imagen, n):
    """
    Esta función recibe una imagen y un tamaño n y separa la imagen en bloques disjuntos de tamaño n*n. A cada uno de 
    estos les haré un tratamiento para obtener su histograma. Los uno y devuelvo el resultado. IMÁGENES A COLOR
    : param imagen : imagen de la que obtener el vector
    : param n: tamaño de bloque
    """
    histogramas = np.array([])
    imagen = recorta_imagen(imagen,n)
    a = imagen.shape[0]
    b = imagen.shape[1]
    
    for k in range(3): #Itero sobre los tres colores
        for i in range(int(a//n)):
            for j in range(int(b//n)):
                bloque = imagen[n*i:n*(i+1),n*j:n*(j+1),k]
                bloque = np.uint8(transforma_bloque(bloque))
                h = cv2.calcHist([bloque], [0], None, [256], [0,256]).flatten()
                histogramas = np.concatenate((histogramas,h))
            
    return histogramas

def crear_vector_caracteristicas_BW_Uniforme(imagen, n):
    """
    Esta función recibe una imagen y un tamaño n y separa la imagen en bloques disjuntos de tamaño n*n. A cada uno de 
    estos les haré un tratamiento para obtener su histograma. Los uno y devuelvo el resultado. IMÁGENES BLANCO Y NEGRO
    Y tratamiento de transición uniforme
    : param imagen : imagen de la que obtener el vector
    : param n: tamaño de bloque
    """
    indices = np.arange(0,58)
    valores_uniformes = [0, 1, 2, 3, 4, 6, 7, 8, 12, 14, 15, 16, 24, 28, 
           30, 31, 32, 48, 56, 60, 62, 63, 64, 96, 112, 120,
           124, 126, 127, 128, 129, 131, 135, 143, 159, 191,
           192, 193, 195, 199, 207, 223, 224, 225, 227, 231,
           239, 240, 241, 243, 247, 248, 249, 251, 252, 253, 254, 255]
    diccionario = dict(zip(valores_uniformes, indices))

    histogramas = np.array([])
    imagen = recorta_imagen(imagen,n)
    a = imagen.shape[0]
    b = imagen.shape[1]
    
    for i in range(int(a//n)):
        for j in range(int(b//n)):
            bloque = imagen[n*i:n*(i+1),n*j:n*(j+1)]
            bloque = np.uint8(transforma_bloque_Uniforme(bloque,diccionario))
            h = cv2.calcHist([bloque], [0], None, [59], [0,59]).flatten()
            histogramas = np.concatenate((histogramas,h))
            
    return histogramas

def transforma_PCA(imagenes_train,imagenes_test,numeroComponentes):
    """
    Esta función recibe un conjunto de vectores de train y de test y les aplica 
    análisis de las componentes principales.
    :param imagenes_train: imágenes con las que entrenar PCA
    :param imagenes_test : imágenes a las que aplicarles la transformación PCA sin haber entrenado con ellas
    :param numeroComponentes: numero de componentes que conservará PCA
    """
    pca = PCA(numeroComponentes)
    pca.fit(imagenes_train)
    imagenes_train = pca.transform(imagenes_train)
    imagenes_test = pca.transform(imagenes_test)
    return imagenes_train,imagenes_test