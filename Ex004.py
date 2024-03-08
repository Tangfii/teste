#FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE.
e=input("Informe um valor: ")
print(type(e))
print('Se tiver somente espaços?','\033[1;32m',e.isspace(),'\033[m')
print('Se tiver somente números?','\033[1;31m',e.isnumeric(),'\033[m')
print('Se for alfábetico?','\033[1;33m', e.isalpha(),'\033[m')
print('Se for alfanumérico?','\033[1;36m',e.isalnum(),'\033[m')  