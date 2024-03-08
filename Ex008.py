#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''m=float(input("Informe uma medida em metros: "))
v1=m*100
v2=m*1000
print("A medida de {} metros \nem centímetros é= {:.0f}cm \nem milímetros= {:.0f}mm".format (m, v1, v2))'''

#Desafio do Professor: Mostra a medida de Metros em: km, hm, dam, dm, cm, mm.
m=float(input("Informe uma medida em Metros: "))
a=m*0.001
b=m*0.01
c=m*0.1
d=m*10
e=m*100
f=m*1000
print("A medida de \033[30m{:.0f}m\033[m em:\n Quilomêtros: \033[31m{:.0f}km\033[m \n Hectômetro: \033[32m {:.0f}hm\033[m \n Decâmetro: \033[33m {:.0f}dam\033[m \n Decímetro: \033[34m {:.0f}dm\033[m \n Centímetro: \033[35m{:.0f}cm\033[m \n Milímetro: \033[36m{:.0f}mm\033[m ".format (m,a,b,c,d,e,f))