#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

a=str(input("Informe uma frase qualquer: ")).strip()

a1=a.lower()

print('A letra a aparece \033[1;4;7m{}\033[m vezes nesta frase'.format(a1.count('a',0)))

print("A primeira letra 'A' apareceu na \033[1;4;7;46m{}\033[m posição.".format(a1.find('a')+1))

print("A última letra 'A' está na \033[1;4;7;45m{}\033[m posição.".format(a1.rfind('a')+1))