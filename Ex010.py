#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$ 1,00=R$3,27

n=float(input("Informe o valor que você têm em sua carteira: R$"))
d=n/3.27
print("Com \033[1;32mR${}\033[m você poderá comprar \033[1;31mUS${:.2f}\033[m .".format(n,d))