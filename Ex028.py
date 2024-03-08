#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computer= randint(0, 5)

print("-=-"*20)
print("Vou pensar em um número de 0 a 5, tente adivinhar: ")
print("-=-"*20)
print("")
n=int(input("Em qual número eu pensei? "))
print("\033[1;33mPROCESSANDO...\033[m")
sleep(3)
if n== computer:
    print("O número que eu estava pensando era \033[34m{}\033[m. Parábens, você \033[1;32macertou!\033[m".format(n))
else:
    print("Você \033[1;31merrou!\033[m eu estava pensando no número \033[31m{}\033[m não no \033[32m{}\033[m".format(computer,n))
