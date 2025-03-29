import sqlite3
import tkinter as tk
from tkinter import messagebox




def create_db():
    conn =  sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('''
           CREATE TABLE IF NOT EXIST pessoas(
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL)''')
    conn.commit()
    conn.close()



def salvar():
    nome = entry_nome.get()


    if nome:
        conn =  sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pessoas (nome) VALUES (?)",(nome,))
        conn.commit()
        conn.close()
        messagebox.showinfo('CONFIRMADO', 'EFETUADO COM SUCESSO')
        limpar_nomes()
        limpar_campos()
    else:
        messagebox.showerror('Erro', 'Algo não funciona')


def listar_nomes():
    conn =  sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    registro =  cursor.fetchall()
    conn.close()


    listbox.delete(0, tk.END)
    for registro in registro:
        listbox.insert(tk.END,f" {registro[0]},Nome:{registro[1]}")



def limpar_campo():
    entry_nome.delete(0, tk.END)   

root = tk.Tk()
root.title('Cadastro de pessoas')

tk.Label(root, text='Nome').grid(row= 0, column=0, padx=10, pady=10)
entry_nome= tk.Entry(root)
entry_nome.nome(row)