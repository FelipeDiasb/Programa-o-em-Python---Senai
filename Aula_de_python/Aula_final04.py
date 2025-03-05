import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Conectar ao banco de dados
def conectar():
    conn = sqlite3.connect("pacientes.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        idade INTEGER,
                        peso REAL,
                        altura REAL,
                        imc REAL)''')
    conn.commit()
    conn.close()

# Calcular IMC
def calcular_imc(peso, altura):
    if altura > 0:
        return round(peso / (altura ** 2), 2)
    return 0

# Adicionar paciente
def adicionar_paciente():
    nome = entry_nome.get()
    idade = entry_idade.get()
    peso = entry_peso.get()
    altura = entry_altura.get()
    
    if nome and idade and peso and altura:
        peso = float(peso)
        altura = float(altura)
        imc = calcular_imc(peso, altura)
        
        conn = sqlite3.connect("pacientes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pacientes (nome, idade, peso, altura, imc) VALUES (?, ?, ?, ?, ?)", 
                       (nome, idade, peso, altura, imc))
        conn.commit()
        conn.close()
        atualizar_lista()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

# Atualizar lista de pacientes
def atualizar_lista():
    conn = sqlite3.connect("pacientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes")
    rows = cursor.fetchall()
    conn.close()
    
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", tk.END, values=row)

# Limpar campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)

# Criar interface gráfica
root = tk.Tk()
root.title("Cadastro de Pacientes")
root.geometry("700x400")

conectar()

# Campos de entrada
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Idade:").grid(row=1, column=0, padx=10, pady=5)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Peso (kg):").grid(row=2, column=0, padx=10, pady=5)
entry_peso = tk.Entry(root)
entry_peso.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Altura (m):").grid(row=3, column=0, padx=10, pady=5)
entry_altura = tk.Entry(root)
entry_altura.grid(row=3, column=1, padx=10, pady=5)

# Botão para adicionar paciente
tk.Button(root, text="Adicionar Paciente", command=adicionar_paciente).grid(row=4, column=0, columnspan=2, pady=10)

# Tabela para exibir pacientes
tree = ttk.Treeview(root, columns=("ID", "Nome", "Idade", "Peso", "Altura", "IMC"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.heading("Peso", text="Peso (kg)")
tree.heading("Altura", text="Altura (m)")
tree.heading("IMC", text="IMC")
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

atualizar_lista()

root.mainloop()
