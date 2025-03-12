

# Acessando valores no dicionário
# print(usuario['nome'])  # Saída: João
# print(usuario['idade'])  # Saída: 30


# Exemplos Básicos:

# #Criando um dicionário vazio:

# meu_dicionario = {}
# dic = dict{}


# #Criando um dicionário com alguns valores:

# meu_dicionario = {'a': 1, 'b': 2, 'c': 3}


# #Acessando valores usando chaves:

# print(meu_dicionario['a'])  # Saída: 1


# #Adicionando um novo par chave-valor:

# meu_dicionario['d'] = 4
# print(meu_dicionario)  # Saída: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# #Removendo um par chave-valor:

# del meu_dicionario['a']
# print(meu_dicionario)  # Saída: {'b': 2, 'c': 3, 'd': 4}


# Principais Métodos:

# #`keys()`: Retorna uma lista contendo todas as chaves do dicionário.

# print(meu_dicionario.keys())  # Saída: dict_keys(['b', 'c', 'd'])


# #`values()`: Retorna uma lista contendo todos os valores do dicionário.

# print(meu_dicionario.values())  # Saída: dict_values([2, 3, 4])


# #`items()`: Retorna uma lista contendo tuplas de chave-valor.

# print(meu_dicionario.items())  
# # Saída: dict_items([('b', 2), ('c', 3), ('d', 4)])


# #`get()`: Retorna o valor associado à 
# chave especificada.

# print(meu_dicionario.get('b'))  # Saída: 2


# #`pop()`: Remove e retorna o valor 
# associado à chave especificada.

# valor = meu_dicionario.pop('c')
# print(valor)  # Saída: 3
# print(meu_dicionario)  # Saída: {'b': 2, 'd': 4}


# #`clear()`: Remove todos os itens do dicionário.

# meu_dicionario.clear()
# print(meu_dicionario)  # Saída: {}


# https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# ## Desafio 1

# Crie um e-commerce com a estrutura de dicionários.

# Produtos:  Livros, tablets e fones de ouvido

# As ações: 

# Comprar()

# Pagar()

# mostra o valor da compra

