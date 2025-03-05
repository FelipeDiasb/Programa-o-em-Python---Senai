import sqlite3
from datetime import datetime

# Conectar ao banco de dados
def conectar():
    conn = sqlite3.connect("horas_trabalho.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS horas_trabalhadas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        advogado TEXT,
                        cliente TEXT,
                        tarefa TEXT,
                        data TEXT,
                        horas REAL)''')
    conn.commit()
    conn.close()

# Adicionar registro de horas
def adicionar_horas(advogado, cliente, tarefa, horas):
    data = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect("horas_trabalho.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO horas_trabalhadas (advogado, cliente, tarefa, data, horas) VALUES (?, ?, ?, ?, ?)",
                   (advogado, cliente, tarefa, data, horas))
    conn.commit()
    conn.close()
    print("Horas registradas com sucesso!")

# Consultar horas trabalhadas
def consultar_horas():
    conn = sqlite3.connect("horas_trabalho.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM horas_trabalhadas")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(row)

# Gerar relatório total de horas
def relatorio_total():
    conn = sqlite3.connect("horas_trabalho.db")
    cursor = conn.cursor()
    cursor.execute("SELECT advogado, SUM(horas) FROM horas_trabalhadas GROUP BY advogado")
    rows = cursor.fetchall()
    conn.close()
    print("Total de horas trabalhadas por advogado:")
    for row in rows:
        print(f"Advogado: {row[0]} - Horas: {row[1]}")

# Criar banco de dados ao iniciar
conectar()

# Exemplo de uso
if __name__ == "__main__":
    while True:
        print("\nSistema de Controle de Horas")
        print("1. Adicionar horas")
        print("2. Consultar horas registradas")
        print("3. Relatório total de horas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            advogado = input("Nome do advogado: ")
            cliente = input("Nome do cliente: ")
            tarefa = input("Descrição da tarefa: ")
            horas = float(input("Horas trabalhadas: "))
            adicionar_horas(advogado, cliente, tarefa, horas)
        elif opcao == "2":
            consultar_horas()
        elif opcao == "3":
            relatorio_total()
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Tente novamente.")
