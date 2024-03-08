#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
'''n1=int(input("Informe um valor: "))
r1=n1+1
r2=n1-1
print("Analisando o valor={} sucessor da soma é={} e o antecessor é {}".format (n1,r1,r2))'''

#OU

n2=int(input("Informe um valor: "))
print("Analisando o valor= \033[4;33m{}\033[m sucessor da soma é= \033[4;32m{}\033[m e o antecessor é= \033[4;31m{}\033[m".format(n2,(n2+1),(n2-1)))