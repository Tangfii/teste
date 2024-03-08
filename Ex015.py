#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dias=int(input("Informe a quatidade de dias que o carro foi alugado: "))
km=float(input("Informe a quatidade de Quilômetros percorridos: "))
pago=(dias*60)+(km*0.15)
print("Você alugou o carro por \033[4;33m{}\033[m dias e percorreu \033[4;36m{}\033[m km\n O valor que deverá ser pago é: \033[1;4;41;34mR${}\033[m".format(dias,km,pago))