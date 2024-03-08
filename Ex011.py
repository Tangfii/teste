#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

n1=float(input("Informe a largura em metros da parede: "))
n2=float(input("Informe a altura em metros da parede: "))
a=n1*n2
print("Sua parede tem dimenção de \033[34m{}\033[m x \033[35m{}\033[m e sua área é de: \033[1;33m{}m²\033[m".format (n1,n2,a))
r=a/2
print("A quantidade de tinta necessária para pintar esta parede é: ",r, "litros")