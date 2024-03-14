import numpy as np
import cv2

def recortaImagen(imagen,n):
    """
    Esta función recibe una imagen y un tamaño n y recorta la imagen de tal manera que el número final de filas/columnas 
    sea múltiplo de n.
    """
    i,j = imagen.shape[:2]
    difFil = i%n
    difCol = j%n
    if(difFil != 0):
        imagen = imagen[:i-difFil,:]
    if(difCol != 0):
        imagen = imagen[:,:j-difCol]
    return imagen

def filtro(imagen, mascara):
    '''
    Se realiza una imagen nueva con un mascara
    '''
    m,n = imagen.shape
    dif = len(mascara)//2
    imagen_filtrada = np.zeros_like(imagen)
    imagen_ampliada = cv2.copyMakeBorder(imagen, dif, dif, dif, dif, cv2.BORDER_REPLICATE)
    for i in range(dif,m+dif):
        for j in range(dif,n+dif):
            imagen_filtrada[i-dif,j-dif] = np.sum(np.multiply(imagen_ampliada[i-dif:i+dif+1,j-dif:j+dif+1],mascara))
    return imagen_filtrada

def gradiente(imagen):
    '''
    Función a la cual pasarle una imagen y calcula la magnitud y orientación del gradiente respecto a unas mascaras
    '''
    m_g_x = filtro(imagen, np.array([-1,0,1]))
    m_g_y = filtro(imagen, np.array([[-1],[0],[1]]))
    E = np.sqrt(m_g_x**2+m_g_y**2)
    Phi = np.rad2deg(np.arctan2(m_g_y,m_g_x))

    Phi[(Phi<=20)&(Phi>=-20)] = 1
    Phi[((Phi>=20)&(Phi<=40))|((Phi<=-20)&(Phi>=-40))] = 2
    Phi[((Phi>=40)&(Phi<=60))|((Phi<=-40)&(Phi>=-60))] = 3
    Phi[((Phi>=60)&(Phi<=80))|((Phi<=-60)&(Phi>=-80))] = 4
    Phi[((Phi>=80)&(Phi<=100))|((Phi<=-80)&(Phi>=-100))] = 5
    Phi[((Phi>=100)&(Phi<=120))|((Phi<=-100)&(Phi>=-120))] = 6
    Phi[((Phi>=120)&(Phi<=140))|((Phi<=-120)&(Phi>=-140))] = 7
    Phi[((Phi>=140)&(Phi<=160))|((Phi<=-140)&(Phi>=-160))] = 8
    Phi[((Phi>=160)&(Phi<=180))|((Phi<=-160)&(Phi>=-180))] = 9

    return E, Phi


def tratarCelda(celda,E,Phi):
    '''
    Obtiene del bloque un array de 9 columnas (9 bins) divididos segun el gradiente del bloque
    '''
    m,n = celda.shape
    E = E.reshape((-1,1))
    Phi = Phi.reshape((-1,1))
    
    bins = np.zeros((9))

    for i in range(Phi.shape[0]):
        if(Phi[i,0] == 1):
            bins[0] += E[i,0]
        elif(Phi[i,0] == 2):
            bins[1] += E[i,0]
        elif(Phi[i,0] == 3):
            bins[2] += E[i,0]
        elif(Phi[i,0] == 4):
            bins[3] += E[i,0]
        elif(Phi[i,0] == 5):
            bins[4] += E[i,0]
        elif(Phi[i,0] == 6):
            bins[5] += E[i,0]
        elif(Phi[i,0] == 7):
            bins[6] += E[i,0]
        elif(Phi[i,0] == 8):
            bins[7] += E[i,0]
        elif(Phi[i,0] == 9):
            bins[8] += E[i,0]
    return bins

def extraerCarCeldas(imagen,n):
    """
    Esta función recibe una imagen y un tamaño n y separa la imagen en bloques disjuntos de tamaño n*n y nos devuelve
    el histograma por celda.
    """
    imagen = recortaImagen(imagen, n)
    a,b = imagen.shape
    a = int(a/n)
    b = int(b/n)
    E,Phi = gradiente(imagen)
    carCeldas = np.zeros((a,b,9))
    for i in range(a):
        for j in range(b):
            celda = tratarCelda(imagen[n*i:n*(i+1),n*j:n*(j+1)],E[n*i:n*(i+1),n*j:n*(j+1)],Phi[n*i:n*(i+1),n*j:n*(j+1)])
            carCeldas[i,j] = np.divide(celda,np.linalg.norm(celda))
    return carCeldas

def normalizarCeldas(carCeldas, m):
    '''
    Se realiza una normalización por n vecinos
    '''
    a,b = carCeldas.shape[0:2]
    a = a-m+1
    b = b-m+1
    carVecinos = np.zeros((a,b,m*m*9))
    for i in range(a):
        for j in range(b):
            if(i!=a or j!=b):
                carVecinos[i,j] = np.divide(carCeldas[i:i+m,j:j+m,:].flatten(),np.linalg.norm(carCeldas[i:i+m,j:j+m,:]))
            else:
                if(i!=a):
                    carVecinos[i,j] = np.divide(carCeldas[i-m:i,j:j+m,:].flatten(),np.linalg.norm(carCeldas[i-m:i,j:j+m,:]))
                elif(j!=b):
                    carVecinos[i,j] = np.divide(carCeldas[i:i+m,j-m:j,:].flatten(),np.linalg.norm(carCeldas[i:i+m,j-m:j,:]))
                elif(i!=a and j!=b):
                    carVecinos[i,j] = np.divide(carCeldas[i-m:i,j-m:j,:].flatten(),np.linalg.norm(carCeldas[i-m:i,j-m:j,:]))
    return carVecinos





#############################################################################################################################################################################################
#ESTAS FUNCIONES SON A LAS QUE SE LES PUEDE LLAMAR. LAS ESCRITAS MÁS ARRIBA SON SOLO
#FUCIONALES PARA ESTAS
#############################################################################################################################################################################################





def crear_vector_caracteristicas_BW(imagen,n,m,normalizar = True):
    carCeldas = extraerCarCeldas(imagen,n)
    if(normalizar):
        carCeldas = normalizarCeldas(carCeldas,m)
    return carCeldas.flatten()

def crear_vector_caracteristicas_color_1(imagen,n,m,normalizar = True):
    carImagen = np.array([])
    for i in range(imagen.shape[2]):
        carCeldas = extraerCarCeldas(imagen[:,:,i],n)
        if (normalizar):
            carCeldas = normalizarCeldas(carCeldas,m)
        carImagen = np.append(carImagen,carCeldas.flatten())
    return carImagen