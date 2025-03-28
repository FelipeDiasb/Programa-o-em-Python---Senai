

import tkinter as tk


def somar():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    soma = n1 + n2
    resultado.config(text=f'{soma}')

def subtrair():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    sub = n1 - n2
    resultado.config(text=f'{sub}')

def multiplicar():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    mult = n1 * n2
    resultado.config(text=f'{mult}')

def dividir():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    if n2 != 0:
        div = n1 / n2
        resultado.config(text=f'{div}')
    else:
        resultado.config(text="Erro: Divisão por zero")



root = tk.Tk()
root.title('CALCULADORA')
root.geometry('300x400')  

# Texto de título
text = tk.Label(root, text='CALCULADORA', fg='white', justify='center', bg='black', font=("Arial", 16, "bold"))
text.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

# Campo de entrada do primeiro número
text2 = tk.Label(root, text='Digite um número')
text2.grid(row=1, column=0, columnspan=2, pady=5, padx=10)
numero1 = tk.Entry(root, width=15)
numero1.grid(row=2, column=0, columnspan=2, pady=5, padx=10)

# Campo de entrada do segundo número
text3 = tk.Label(root, text='Digite um número')
text3.grid(row=3, column=0, columnspan=2, pady=5, padx=10)
numero2 = tk.Entry(root, width=15)
numero2.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

# Resultado
resultado = tk.Label(root, text='Resultado', fg='black', font=("Arial", 12, 'bold'))
resultado.grid(row=5, column=0, columnspan=2, pady=15)

# Botões de operação
btn_somar = tk.Button(root, text='+', command=somar, width=10)
btn_somar.grid(row=6, column=0, pady=7)

btn_subtrair = tk.Button(root, text='-', command=subtrair, width=10)
btn_subtrair.grid(row=6, column=1, pady=5)

btn_multiplicar = tk.Button(root, text='*', command=multiplicar, width=10)
btn_multiplicar.grid(row=7, column=0, pady=5)

btn_dividir = tk.Button(root, text='/',  activebackground="blue", activeforeground="white", command=dividir, width=10)
btn_dividir.grid(row=7, column=1, pady=5)

# Ajustando o layout
for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for j in range(2):
    root.grid_columnconfigure(j, weight=1)

# Iniciar a interface
root.mainloop()