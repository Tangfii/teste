#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1=str(input("Informe o nome do primeiro aluno(a): "))
a2=str(input("Informe o nome do segundo aluno(a): "))
a3=str(input("Informe o nome do terceiro aluno(a): "))
a4=str(input("Informe o nome do quarto aluno(a): "))
lista=[a1,a2,a3,a4]
shuffle(lista)
print("A ordem da apresentação será:")
print('\033[44;33m',lista,'\033[m')