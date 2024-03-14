import numpy as np

def escribir(extractor,modelo,vec_train,vec_test):
    '''
    :param extractor: {extrac1,extrac2}
    :param modelo: {std,color,uniforme/normalizada}
    :param vec_train: vector de train
    :param vec_test: vector de test
    '''
    if(extractor == 'extrac1'):
        if(modelo == 'std'):
            f = open("EX1_STD_100_vec_train.txt", "x")
            f = open("EX1_STD_100_vec_test.txt", "x")
            np.savetxt("EX1_STD_100_vec_train.txt", vec_train,fmt='%i')
            np.savetxt("EX1_STD_100_vec_test.txt", vec_test,fmt='%i')

        elif(modelo == 'color'):
            f = open("EX1_COLOR_100_vec_train.txt", "x")
            f = open("EX1_COLOR_100_vec_test.txt", "x")
            np.savetxt("EX1_COLOR_100_vec_train.txt", vec_train,fmt='%i')
            np.savetxt("EX1_COLOR_100_vec_test.txt", vec_test,fmt='%i')

        elif(modelo == 'uniforme'):
            f = open("EX1_UNIFORM_100_vec_train.txt", "x")
            f = open("EX1_UNIFORM_100_vec_test.txt", "x")
            np.savetxt("EX1_UNIFORM_100_vec_train.txt", vec_train,fmt='%i')
            np.savetxt("EX1_UNIFORM_100_vec_test.txt", vec_test,fmt='%i')

        else:
            print('El modelo que has introducido es incorrecto, escoge entre "std","color" y "uniforme"')

    elif(extractor == 'extrac2'):
        if(modelo == 'std'):
            f = open("EX2_STD_100_vec_train.txt", "x")
            f = open("EX2_STD_100_vec_test.txt", "x")
            np.savetxt("EX2_STD_100_vec_train.txt", vec_train,fmt='%1.5f')
            np.savetxt("EX2_STD_100_vec_test.txt", vec_test,fmt='%1.5f')

        elif(modelo == 'color'):
            f = open("EX2_COLOR_100_vec_train.txt", "x")
            f = open("EX2_COLOR_100_vec_test.txt", "x")
            np.savetxt("EX2_COLOR_100_vec_train.txt", vec_train,fmt='%1.5f')
            np.savetxt("EX2_COLOR_100_vec_test.txt", vec_test,fmt='%1.5f')

        elif(modelo == 'normalizada'):
            f = open("EX2_NORMALIZADA_100_vec_train.txt", "x")
            f = open("EX2_NORMALIZADA_100_vec_test.txt", "x")
            np.savetxt("EX2_NORMALIZADA_100_vec_train.txt", vec_train,fmt='%1.5f')
            np.savetxt("EX2_NORMALIZADA_100_vec_test.txt", vec_test,fmt='%1.5f')
        else:
            print('El modelo que has introducido es incorrecto, escoge entre "std","color" y "normalizada"')

    else:
        print('El extractor que has introducido es incorrecto, escoge entre "extrac1" y "extrac2"')