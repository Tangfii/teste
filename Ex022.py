#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome

nome=str(input("Informe seu nome completo: ")).strip()
print("Seu nome em letras maiúsculas é: \033[4;34m",(nome.upper()),"\033[m")
print("Seu nome em letras minúsculas é: \033[4;35m",(nome.lower()),"\033[m")
print("Seu nome contém \033[1;36m{}\033[m letras ao todo.".format(len(nome.replace(" ", ""))))
n=(nome.split())
print("Seu primeiro nome contém \033[1;32m{}\033[m letras ao todo.".format(len(n[0])))