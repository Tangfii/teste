#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("\033[1;33m-=-\033[m"*20)
print("\033[1;33mAnalisador de Triângulos\033[m")
print("\033[1;33m-=-\033[m"*20)

s1=float(input("Informe o primeiro segmento de um triângulo: "))
s2=float(input("Informe o segundo segmento de um triângulo: "))
s3=float(input("Informe o segmento do terceiro triângulo: "))

if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print("Estes segmentos \033[1;4;32mSÃO CAPAZES\033[m de formar um triângulo.")
else:
    print("Estes segmentos \033[1;4;31mNÃO SÃO CAPAZES\033[m de formar um triângulo.")