#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1=int(input("Informe um número qualquer: "))
n2=int(input("Informe um número qualquer: "))
n3=int(input("Informe um número qualquer: "))

menor=n1
if  n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3

maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3

print("O menor valor digitado foi \033[33;46m{}\033[m".format(menor))
print("O maior valor digitado foi \033[43;36m{}\033[m".format(maior))

#OU

'''n1=int(input("Informe um número qualquer: "))
n2=int(input("Informe um número qualquer: "))
n3=int(input("Informe um número qualquer: "))

max=max(n1,n2,n3)
min=min(n1,n2,n3)

print("O menor valor digitado é ",min)
print("O maior valor digitado é ",max)'''