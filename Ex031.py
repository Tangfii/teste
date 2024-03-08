#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km=float(input("Informe quantos km você percorreu: "))
if km <=200:
    p=km*0.50
    print("Você irá realizar uma viagem de \033[1;33m{}km\033[m \n Você terá de pagar \033[1;4;32mR${:.2f}\033[m. Boa viagem!".format(km,p))
if km >200:
    p=km*0.45
    print("Você irá realizar uma viagem de \033[1;33m{}km\033[m \nVocê terá de pegar \033[1;2;32mR${:.2f}\033[m. Boa viagem!".format(km,p))