#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

'''import math
num=float(input("Informe um número: "))
print("O número informado é {} e sua porção inteira é {}".format (num,math.trunc(num)))'''

#Ou

'''from math import trunc
num1=float(input("Informe um número: "))
print("O número informado foi {} e a sua porção inteira é {}".format (num1,trunc(num1)))'''

#Ou 
num2=float(input("Informe um valor: "))
print("O valor informado foi \033[1;35m{}\033[m e a porção inteira é \033[1;36m{}\033[m".format (num2, int(num2)))
