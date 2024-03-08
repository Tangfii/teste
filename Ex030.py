#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n=int(input("Informe um número: "))
r=n%2
if r==0:
    print("O número \033[1;31{}\033[m é \033[1;4;44;36mPar\033[m".format(n))
else:
    print("O número \033[1;31{}\033[m é \033[1;4;34;46mÍmpar\033[m".format(n))