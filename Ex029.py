#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

velo=float(input("Qual a velocidade atual do carro? "))
if velo <=80:
    print("\033[1;32mTenha um bom dia! Dirija com segurança.\033[m")

if velo >80:
    multa= (velo-80)*7
    print("\033[1;31mMULTA! Você excedeu o limite permetido de 80Km/h\033[m \n Você deverá pagar uma multa de \033[1;4;31mR${:.2f}!\033[m".format(multa))