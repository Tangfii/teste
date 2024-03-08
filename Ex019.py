#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choices
a1=str(input("Informe o nome do primeiro aluno(a): "))
a2=str(input("Informe o nome do segundo aluno(a): "))
a3=str(input("Informe o nome do terceiro aluno(a): "))
a4=str(input("Informe o nome do quarto aluno(a)"))
lista=[a1,a2,a3,a4]
print("O aluno(a) escolhido foi \033[1;4;46;33m{}\033[m".format (choices(lista)))