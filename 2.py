import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Função para conectar ao banco de dados SQLite
def conectar():
    return sqlite3.connect('clinica.db')

# Função para criar a tabela de pacientes no banco de dados
def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS pacientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            imc REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

# Função para cadastrar um novo paciente
def cadastrar_paciente():
    nome = entry_nome.get()
    idade = entry_idade.get()
    peso = entry_peso.get()
    altura = entry_altura.get()

    # Verificar se os campos estão preenchidos corretamente
    if nome and idade and peso and altura:
        try:
            idade = int(idade)
            peso = float(peso)
            altura = float(altura)
            imc = calcular_imc(peso, altura)

            # Inserir dados no banco de dados
            conn = conectar()
            c = conn.cursor()
            c.execute('INSERT INTO pacientes (nome, idade, peso, altura, imc) VALUES (?, ?, ?, ?, ?)', 
                      (nome, idade, peso, altura, imc))
            conn.commit()
            conn.close()

            messagebox.showinfo('Cadastro', 'Paciente cadastrado com sucesso!')
            mostrar_pacientes()
        except ValueError:
            messagebox.showerror('Erro', 'Por favor, insira valores válidos para idade, peso e altura.')
    else:
        messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')

# Função para mostrar os pacientes cadastrados
def mostrar_pacientes():
    for row in tree.get_children():
        tree.delete(row)

    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM pacientes')
    pacientes = c.fetchall()

    for paciente in pacientes:
        tree.insert("", "end", values=(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4], paciente[5]))
    
    conn.close()

# Função para editar um paciente
def editar_paciente():
    paciente_selecionado = tree.selection()
    if paciente_selecionado:
        paciente_id = tree.item(paciente_selecionado)['values'][0]
        novo_nome = entry_nome.get()
        nova_idade = entry_idade.get()
        novo_peso = entry_peso.get()
        nova_altura = entry_altura.get()

        if novo_nome and nova_idade and novo_peso and nova_altura:
            try:
                nova_idade = int(nova_idade)
                novo_peso = float(novo_peso)
                nova_altura = float(nova_altura)
                novo_imc = calcular_imc(novo_peso, nova_altura)

                conn = conectar()
                c = conn.cursor()
                c.execute('UPDATE pacientes SET nome = ?, idade = ?, peso = ?, altura = ?, imc = ? WHERE id = ?',
                          (novo_nome, nova_idade, novo_peso, nova_altura, novo_imc, paciente_id))
                conn.commit()
                conn.close()

                messagebox.showinfo('Edição', 'Dados atualizados com sucesso!')
                mostrar_pacientes()
            except ValueError:
                messagebox.showerror('Erro', 'Por favor, insira valores válidos para idade, peso e altura.')
        else:
            messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')
    else:
        messagebox.showerror('Erro', 'Selecione um paciente para editar.')

# Função para excluir um paciente
def excluir_paciente():
    paciente_selecionado = tree.selection()
    if paciente_selecionado:
        paciente_id = tree.item(paciente_selecionado)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM pacientes WHERE id = ?', (paciente_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo('Exclusão', 'Paciente excluído com sucesso!')
        mostrar_pacientes()
    else:
        messagebox.showerror('Erro', 'Selecione um paciente para excluir.')

# Interface Gráfica
janela = tk.Tk()
janela.title('Cadastro de Pacientes - Saúde & Bem-Estar')

# Campos de entrada
label_nome = tk.Label(janela, text='Nome:')
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(janela, text='Idade:')
label_idade.grid(row=1, column=0, padx=10, pady=10)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

label_peso = tk.Label(janela, text='Peso (kg):')
label_peso.grid(row=2, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=2, column=1, padx=10, pady=10)

label_altura = tk.Label(janela, text='Altura (m):')
label_altura.grid(row=3, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=3, column=1, padx=10, pady=10)

# Botões de ação
btn_cadastrar = tk.Button(janela, text='Cadastrar', command=cadastrar_paciente)
btn_cadastrar.grid(row=4, column=0, padx=10, pady=10)

btn_editar = tk.Button(janela, text='Editar', command=editar_paciente)
btn_editar.grid(row=4, column=1, padx=10, pady=10)

btn_excluir = tk.Button(janela, text='Excluir', command=excluir_paciente)
btn_excluir.grid(row=4, column=2, padx=10, pady=10)

# Exibir pacientes cadastrados
columns = ('ID', 'Nome', 'Idade', 'Peso', 'Altura', 'IMC')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

# Iniciar tabela e exibição dos dados
criar_tabela()
mostrar_pacientes()

# Rodar a aplicação
janela.mainloop()
