#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nom

nome=str(input("Informe seu completo: ")).strip()
n=nome.title()
print("Seu nome tem Silva: ", '\033[32m','Silva'in n, '\033[m')