#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''import math
num=float(input("Informe um número: "))
seno=math.sin(math.radians(num))
print("O ângulo {} tem o Seno {:.2f}".format(num, seno))
cosseno=math.cos(math.radians(num))
print("O ângulo {} tem o Cosseno {:.2f}".format(num, cosseno))
tangente=math.tan(math.radians(num))
print("O ângulo {} tem o Tangente {:.2f}".format (num, tangente))'''

#OU

from math import radians, sin, cos, tan
num=float(input("Informe um número: "))
seno=sin(radians(num))
print("O ângulo \033[1;35m{}\033[m tem o Seno \033[1;34m{:.2f}\033[m".format(num, seno))
cosseno=cos(radians(num))
print("O ângulo \033[1;35m{}\033[m tem o Cosseno \033[1;34m{:.2f}\033[m".format(num, cosseno))
tangente=tan(radians(num))
print("O ângulo \033[1;35m{}\033[m tem o Tangente \033[1;34m{:.2f}\033[m".format (num, tangente))