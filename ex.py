import tkinter as tk
import sys

window = tk.Tk()

label = tk.Label(window, text = "Informe uma temperatura")
label.pack(padx = 20, pady = 20)

Temp = tk.Entry(window, width = 100)
Temp.pack(padx = 20, pady = 20)

def sair():
    sys.exit()

def celsius():
    texto = int(Temp.get())
    label.config(text = f"Temperatura: {texto}")

def far():
    texto = int(Temp.get())
    label.config(text = f"Temperatura: {(texto * 9/5) + 32}")

botao = tk.Button(window, text = "Celsius", command = celsius)
botao.pack(pady = 10)

botao2 = tk.Button(window, text = "Fahrenheit", command = far)
botao2.pack(pady = 10)

botao3 = tk.Button(window, text = "Sair", command = sair)
botao3.pack(pady = 10)

window.mainloop()