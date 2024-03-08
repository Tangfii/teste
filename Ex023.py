#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

from time import sleep

n=int(input("Informe um número qualquer: "))

u= n // 1 %10
d= n//10%10
c= n//100%10
m= n//1000%10

print("Analisando o número:\033[1;33m...{}...\033[m ".format(n))
sleep(3)

print("Unidades: ",'\033[1;31m',u,'\033[m')
print("Dezenas: ",'\033[1;32m',d,'\033[m')
print("Centenas: ",'\033[1;33m',c,'\033[m')
print("Milhar: ",'\033[1;34m',m,'\033[m')