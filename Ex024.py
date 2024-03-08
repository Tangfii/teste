#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade=str(input("Informe o nome da cidade que você nasceu: ")).strip()

print('\033[1;32m',cidade[:5].upper() == 'SANTO','\033[m')