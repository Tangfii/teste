#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s=float(input("Informe seu salário: "))
r=s+(s/100*15)
print("O seu salário saiu de \033[1;4;33m R${:.2f}\033[m  para \033[1;4;32mR${:.2f}\033[m ".format(s, r))