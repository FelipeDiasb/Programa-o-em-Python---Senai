import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Conectar ao banco de dados
def conectar():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        email TEXT,
                        telefone TEXT,
                        endereco TEXT)''')
    conn.commit()
    conn.close()

# Adicionar um novo cliente
def adicionar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()
    
    if nome and email and telefone and endereco:
        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)", (nome, email, telefone, endereco))
        conn.commit()
        conn.close()
        atualizar_lista()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

# Atualizar lista de clientes
def atualizar_lista():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    conn.close()
    
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", tk.END, values=row)

# Limpar campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Criar interface gráfica
root = tk.Tk()
root.title("Cadastro de Clientes")
root.geometry("600x400")

conectar()

# Campos de entrada
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Telefone:").grid(row=2, column=0, padx=10, pady=5)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Endereço:").grid(row=3, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(root)
entry_endereco.grid(row=3, column=1, padx=10, pady=5)

# Botão para adicionar cliente
tk.Button(root, text="Adicionar Cliente", command=adicionar_cliente).grid(row=4, column=0, columnspan=2, pady=10)

# Tabela para exibir clientes
tree = ttk.Treeview(root, columns=("ID", "Nome", "Email", "Telefone", "Endereço"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Email", text="Email")
tree.heading("Telefone", text="Telefone")
tree.heading("Endereço", text="Endereço")
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

atualizar_lista()

root.mainloop()
