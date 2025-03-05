import sqlite3

def conectar():
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS leads (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        email TEXT,
                        telefone TEXT,
                        interesse TEXT,
                        status TEXT)''')
    conn.commit()
    conn.close()

def adicionar_lead():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    interesse = input("Interesse: ")
    status = "Em andamento"
    
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leads (nome, email, telefone, interesse, status) VALUES (?, ?, ?, ?, ?)", (nome, email, telefone, interesse, status))
    conn.commit()
    conn.close()
    print("Lead cadastrado com sucesso!")

def listar_leads():
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads")
    leads = cursor.fetchall()
    conn.close()
    
    if leads:
        for lead in leads:
            print(f"ID: {lead[0]}, Nome: {lead[1]}, Email: {lead[2]}, Telefone: {lead[3]}, Interesse: {lead[4]}, Status: {lead[5]}")
    else:
        print("Nenhum lead cadastrado.")

def atualizar_status():
    listar_leads()
    lead_id = input("Digite o ID do lead para atualizar o status: ")
    novo_status = input("Novo status (Em andamento, Convertido, Perdido): ")
    
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE leads SET status = ? WHERE id = ?", (novo_status, lead_id))
    conn.commit()
    conn.close()
    print("Status atualizado com sucesso!")

def excluir_lead():
    listar_leads()
    lead_id = input("Digite o ID do lead para excluir: ")
    
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM leads WHERE id = ?", (lead_id,))
    conn.commit()
    conn.close()
    print("Lead excluído com sucesso!")

# Menu interativo
while True:
    print("\nGerenciamento de Leads")
    print("1. Adicionar Lead")
    print("2. Listar Leads")
    print("3. Atualizar Status")
    print("4. Excluir Lead")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_lead()
    elif opcao == "2":
        listar_leads()
    elif opcao == "3":
        atualizar_status()
    elif opcao == "4":
        excluir_lead()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
