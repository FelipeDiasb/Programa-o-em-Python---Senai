import sqlite3

con = sqlite3.connect("Meu_banco.db")

cur = con.cursor()


# cur.execute("""
#        CREATE TABLE MARKETING  (
#        id_campanha INT NOT NULL PRIMARY KEY AUTOINCREMENT,
#        nome_campanha VARCHAR(255))NOT NULL,
#        tipo_campanha VARCHAR(55) not null,
#        data_inicio (DATE) NOT NULL,
#        email TEXT NOT NULL,
#        fone TEXT,
#        cidade TEXT,
#        uf VARCHAR(2) NOT NULL,
#         criado_em DATE NOT NULL );
#  """)

# print('Tabela criada com sucesso.')








# data_inicio (DATE) – Data de início da campanha.

# data_fim (DATE) – Data de término da campanha.

# status (VARCHAR) – Status da campanha (e.g., ativa, finalizada, pausada).

# orçamento (DECIMAL) – Orçamento alocado para a campanha.

# canal (VARCHAR) – Canal utilizado (e.g., Facebook, Google Ads, E-mail, etc.).

# objetivo (VARCHAR) – Objetivo da campanha (e.g., conversão, geração de leads, aumento de tráfego).

# descricao (TEXT) – Descrição da campanha.

# Tabela: Leads



# cur.execute("DROP TABLE movie")



# con.commit()

# #Closing the connection
# con.close()


#cur.execute('select * from movie')



import sqlite3



conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()
cursor.execute('''
     CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
     )
 ''')



nome =  input('Digite um nome')
idade = int(input('Digite sua idade'))
cidade = input('Cidade:')



cursor.execute('''
     INSERT INTO pessoas (nome, idade, cidade)
     VALUES (?, ?, ?)
 ''', (nome, idade, cidade))




conexao.commit()


cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()




for pessoa in pessoas:
     print(f'ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]}, Cidade: {pessoa[3]}')



    
conexao.close()