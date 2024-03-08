#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p=float(input("Informe o preço de um produto:R$"))
r=p-(p/100*5)

print("O produto que custava \033R$[4;33m{}\033[m recebeu um desconto e passou a custar \033[1;4;32mR${:.2f}\033[m".format(p,r))