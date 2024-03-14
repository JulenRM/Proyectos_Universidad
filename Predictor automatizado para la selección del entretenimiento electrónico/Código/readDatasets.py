import numpy as np
import csv
import sys

datos_esrb = np.loadtxt('datos/caracteristicas_esrb.txt',delimiter=',',dtype=str)
generos = np.loadtxt('datos/generos.txt',delimiter=',',dtype=str)
plataformasPortables = np.loadtxt('datos/plataformasPortables.txt',delimiter=',',dtype=str)

class juego:
    def __init__(self,parametros):
        self.nombre = parametros[1]
        self.fechaSalida = np.int(parametros[2].replace(' ','').split(',')[1])
        self.genero = self.procesarGeneros(np.array(parametros[3].lower().replace(' ','').split(',')))
        self.plataforma = np.array([parametros[4]])
        self.portable = self.procesarPlataformas(parametros[4].lower())
        self.desarrollador = parametros[5]
        self.esrb = esrb(parametros[6],parametros[7])
        self.metaScore = np.array([])
        if(parametros[8] != 'tbd'):
            self.metaScore = np.append(self.metaScore,float(parametros[8]))
        self.userScore = np.array([])
        if(parametros[9] != 'tbd'):
            self.userScore = np.append(self.userScore,float(parametros[9]))
        self.multijugador, self.online  = self.procesarNumJugadores(parametros[12])
        self.sinopsis = parametros[13]
        self.reviews = np.zeros((0,2))
        
    def incluirReview(self,rating,review):
        self.reviews = np.append(self.reviews,[[rating,review.lower()]],axis=0)

    def incluirCaracteristicas(self,parametros):
        if(np.int(parametros[2].replace(' ','').split(',')[1]) < self.fechaSalida):
            self.fechaSalida = np.int8(parametros[2].split(',')[1])
        self.plataforma = np.append(self.plataforma,parametros[4])
        if(self.portable == 0):
            self.portable = self.procesarPlataformas(parametros[4].lower())
        if(parametros[7]!=''):
            self.esrb.caracteristicas = self.esrb.tratarCaracteristicas(parametros[7].lower())
        if(parametros[8] != 'tbd'):
            self.metaScore = np.append(self.metaScore,float(parametros[8]))
        if(parametros[9] != 'tbd'):
            self.userScore = np.append(self.userScore,float(parametros[9]))
        self.multijugador, self.online = self.procesarNumJugadores(parametros[12])
    
    def calcularScores(self):
        if(self.metaScore.size != 0):
            self.metaScore = np.round(np.mean(self.metaScore),2)
        else:
            self.metaScore = -1
        if(self.userScore.size != 0):
            self.userScore = np.round(np.mean(self.userScore),2)
        else:
            self.userScore = -1
    
    def procesarPlataformas(self,plataforma):
        port = 0
        if (plataforma in plataformasPortables):
            port = 1
        return port

    def procesarGeneros(self,generosJuego):
        generoFinal = ''
        for i in generos:
            if(i in generosJuego):
                generoFinal = i
                break
        return generoFinal

    def procesarNumJugadores(self,numJugadores):
        multijugador = 1
        online = 0
        numJugadores = numJugadores.lower().replace(', ',',')
        numJugadores = numJugadores.replace('no online','noonline')
        numJugadores = numJugadores.replace('-',' ').split(' ')
        if('1' in numJugadores):
            multijugador = 0
        if(('online' in numJugadores or 'multuplayer' in numJugadores or 'friend' in numJugadores) and 'noonline' not in numJugadores):
            online = 1
        return multijugador,online

class esrb:
    def __init__(self,rating,variables):
        self.rating = rating
        self.caracteristicas = -1
        if(variables != ''):
            self.caracteristicas = self.tratarCaracteristicas(variables.lower())
    
    def tratarCaracteristicas(self,variables):
        variables = self.preprocesarVariables(variables)
        arrayCaracteristicas = self.caracteristicas
        if(isinstance(self.caracteristicas,int)):
            arrayCaracteristicas = np.zeros_like(datos_esrb,dtype=int)
        for i in range(len(datos_esrb)):
            if(datos_esrb[i] in variables and arrayCaracteristicas[i] == 0):
                arrayCaracteristicas[i] += 1
        return arrayCaracteristicas

    def preprocesarVariables(self,variables):
        variables = variables.replace('&','and')
        for caracteristica in datos_esrb:
            aux = caracteristica.replace('_',' ')
            if(aux in variables):
                variables = variables.replace(aux,caracteristica)
        return variables

def lecturaDatos(pathGame, pathReview, listaJuegos=None):
    yes = 1
    if(listaJuegos is None):
        yes = 0
        listaJuegos = {}
    maxInt = sys.maxsize
    while True:
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)

    with open(pathGame, newline='',encoding='utf8') as csvfile:
        DictReader_obj = csv.DictReader(csvfile)
        for item in DictReader_obj:
            if(item['esrb_rating']!='' and item['ESRBs']!='' and item['num_players']!=''):
                if(item['game']) not in listaJuegos:
                    listaJuegos[item['game']] = juego(list(item.values()))
                else:
                    if(yes==1):
                        listaJuegos[item['game']].incluirCaracteristicas(list(item.values()))
                    else:
                        if(item['platforms']!='Dreamcast'):
                            listaJuegos[item['game']].incluirCaracteristicas(list(item.values()))
    if(yes==1):
        for value in listaJuegos.values():
            value.calcularScores()

    with open(pathReview, newline='',encoding='utf8') as csvfile:
        DictReader_obj = csv.DictReader(csvfile)
        for item in DictReader_obj:
            if(item['game']) in listaJuegos:
                listaJuegos[item['game']].incluirReview(int(item['rating']),item['review'])
    return listaJuegos
