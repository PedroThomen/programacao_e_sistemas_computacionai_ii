
def main(): #o escopo do programa está dentro do main
    print("oi")

    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura em cm: "))



    # chamo o programa
    imc = calcula_imc (peso, altura)

    print('Seu IMC é: {}'.format(round(imc)))
    print('Sua classificação é: {}'.format(classificacao_corporal(imc)))
    print(classificacao_corporal(calcula_imc(peso, altura)))

   

def calcula_imc(peso, altura):
     imc = peso / (altura/100) ** 2

     return imc


def classificacao_corporal(imc):
    if imc <= 18.5:
        return 'Magreza'
    elif imc <= 24.9 and imc > 18.5:
        return 'Normal'
    elif imc <= 29.9 and imc > 24.9:
        return 'Sobrepeso'
    elif imc <= 34.9 and imc > 29.9:
        return "Obesidade I"
    elif imc <= 39.9 and imc > 34.9:
        return "Obesidade II"
    else:
        return "Obesidade III"
    



if __name__ == '__main__':
    main()