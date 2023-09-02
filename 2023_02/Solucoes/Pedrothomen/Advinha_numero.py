#o programa pensa num numero de n digitos e o ususario deve advinhar
#o numero em 10 tentativas

import random
NUM_DIGITOS = 4
NUM_MAX_TENTATIVAS = 10

def main():
    num_tentativas = 1 
    numero_aleatorio = pensa_numero_aleatorio()
    print(numero_aleatorio)
    
    while num_tentativas < NUM_MAX_TENTATIVAS:

        numero_usuario =str(int(input("Digite um numero com {} digitos!:".format(NUM_DIGITOS))))
    
        if verifica_numero(numero_aleatorio, numero_usuario):
            print("VOce Acertou")
            break
        else:
            print("Voce errou")
            num_tentativas +=1

def verifica_numero(numero_aleatorio, numero_usuario):
    if numero_usuario == numero_aleatorio:
        return True
    else:
        return False


def pensa_numero_aleatorio():
    possiveis_numeros=list('0123456789')
    random.shuffle(possiveis_numeros)
    lista_numeros = possiveis_numeros[0:NUM_DIGITOS]

    numero_aleatorio = ''

    for numero in lista_numeros:
       
        numero_aleatorio += str(numero)

    return numero_aleatorio





if __name__=='__main__':
    main()