#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

'''a=float(input("Informe um cateto oposto: "))
b=float(input("Informe outro cateto adjacente: "))
c = (a**2+b**2)**(1/2)  
print("O cateto oposto é {}\n O cateto adjacente é {}\n A hipotenusa é {:.2f}".format(a,b,c))'''

#OU

from math import hypot
a=float(input("Informe o valor do cateto oposto: "))
b=float(input("Informe o valor do cateto adjacente: "))
print("O valor do cateto oposto é \033[36m{:.2f}\n\033[m O valor do cateto adjacente é \033[34m{:.2f}\n\033[m O valor da hipotenusa é \033[1;4;35m{:.2f}\033[m".format (a,b, hypot(a,b)))