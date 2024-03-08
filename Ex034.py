#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salario=float(input("Informe o seu salário: R$"))

if salario<=1250:
    aumento=salario+(salario/100*15)
    print("Seu salário saiu de \033[1;31mR${:.2f}\033[m e foi para \033[1;32mR${:.2f}\033[m".format(salario,aumento))
else:
    aumento=salario+(salario/100*10)
    print("Seu salário saiu de \033[1;31mR${:.2f}\033[m e foi para \033[1;32mR${:.2f}\033[m".format(salario,aumento))