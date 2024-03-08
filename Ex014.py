#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c=float(input("Informe a temperatuda desejada: °C "))
print("A temperatura °C \033[1;47;363m{}\033[m em fahrenheit é de \033[1;41;34m{}\033[m °F".format (c,(c * 9/5)+32))