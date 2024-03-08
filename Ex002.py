#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

'''nome=input("Informe seu nome: ")
print("É um prazer te conhecer,", nome)'''

#OU

nome2=input("Informe seu nome: ")
print("É um prazer te conhecer, {}{}{}!". format ('\033[1;36m',nome2,'\033[m'))