#Desenvolva um programa que leia as duas notas de um aluno,  calcule e mostre a sua média.
print("Bem-vindo estudante!")
n1=int(input("Informe a sua primeira nota: "))
n2=int(input("Informe a sua segunda nota: "))
m=(n1+n2)/2
print("A média entre \033[1;36m{}\033[m e \033[1;35m{}\033[m foi de \033[1;33m{:.1f}\033[m".format(n1,n2,m))