#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''n=float(input("Informe qualquer número: "))
v1=n*2
v2=n*3
v3=n**(1/2)
print("O dobro do número escrito é= {} \nO triplo é= {}  \nA raiz quadrada é= {:.2f}".format (v1, v2, v3))'''

#OU

n1=float(input("Informe qualquer número: "))
print("O dobro de \033[1;36m{}\033[m é= \033[1;34m{}\033[m \nO triplo é= \033[1;33m{}\033[m  \nA raiz quadrada é= \033[1;32m{:.2f}\033[m".format (n1,(n1*2),(n1*3),pow(n1, (1/2))))

#A nova função pow é uma outra maneira de calcular a raiz quadrada.