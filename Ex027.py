#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome=str(input("Informe seu nome completo: ")).title().strip()

n1=nome.split()
print("Seu primeiro nome é \033[4;33m{}\033[m".format(n1[0]))

print("Seu último nome é \033[4;36m{}\033[m".format(n1[len(n1)-1]))