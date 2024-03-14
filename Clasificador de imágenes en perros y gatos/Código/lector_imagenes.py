import numpy as np
import cv2
import glob


def crea_dataset(path = 'cat_dog_100',BN = 0,tamanio_imagen = (380,380)):
    """
    Esta función lee una carpeta y extrae sus archivos, dividiéndolos
    en train y en test según el nombre de la subcarpeta.
    :param path: dirección donde se encuentran las carpetas con las imágenes que queremos leer
    :param BN: Si queremos leer en blanco y negro o en color
    :param tamanio_imagen: Tamaño al que queremos dejar todas las imágenes
    """
    #Se escoge de forma arbitraria : clase 0 = gatos, clase 1 = perros
    imagenes_train = glob.glob(path+'/train/*/*')
    imagenes_test = glob.glob(path+'/test/*/*')
    
    #Vectores de train
    y_train = np.zeros((len(imagenes_train),1)) #Vector de clases
    y_train[len(glob.glob(path+'/train/cat/*')):,:] = 1 #Sé que leo primero son gatos
    X_train = []
    for i in range(len(imagenes_train)):
        imagen = cv2.imread(imagenes_train[i], BN)
        imagen = cv2.resize(imagen,(tamanio_imagen)) #Hago que todas las imágenes sean del mismo tamaño
        X_train.append(imagen)
    X_train = np.asarray(X_train,dtype=np.uint8)

    #Vectores de test
    y_test = np.zeros((len(imagenes_test),1)) #Vector de clases
    y_test[len(glob.glob(path+'/test/cat/*')):,:] = 1 #Sé que leo primero son gatos
    X_test = []
    for i in range(len(imagenes_test)):
        imagen = cv2.imread(imagenes_test[i], BN)
        imagen = cv2.resize(imagen,tamanio_imagen) #Hago que todas las imágenes sean del mismo tamaño
        X_test.append(imagen)
    X_test = np.asarray(X_test,dtype=np.uint8)

    return X_train,y_train,X_test,y_test