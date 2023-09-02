def main():
    capital = float(input("Digite o valor a ser investido: "))
    taxa = float(input("Digite a taxa de juros por período %: "))
    periodos = int(input("Digite a quantidade de períodos: "))

    montante = calcula_montante(capital, taxa, periodos)

    print('O valor final do investimento depois de {} periodos é: R $ {}'.format(periodos, round(montante, 2)))



def calcula_montante(c, t, n):
    #montante = capital investido * (1 + taxa_juros/100) ++ 2 
    montante = c * (1 + t/100) ** 2 

    return montante

if __name__=='__main__':
    main()