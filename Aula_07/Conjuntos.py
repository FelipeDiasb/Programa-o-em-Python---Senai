# ## Cojuntos

# # Quando Usar Conjuntos?
# # Quando você precisa armazenar elementos únicos.
# # Quando você precisa realizar operações de conjuntos, como união, interseção ou diferença.
# # Para remover duplicatas de uma lista ou sequência.



# conjunto1 = {1, 2, 3, 4}
# conjunto2 = {3, 4, 5, 6}

# # União
# uniao = conjunto1 | conjunto2  # ou conjunto1.union(conjunto2)
# print(uniao)  # Saída: {1, 2, 3, 4, 5, 6}

# # Interseção
# intersecao = conjunto1 & conjunto2  # ou conjunto1.intersection(conjunto2)
# print(intersecao)  # Saída: {3, 4}

# # Diferença
# diferenca = conjunto1 - conjunto2  # ou conjunto1.difference(conjunto2)
# print(diferenca)  # Saída: {1, 2}

# # Diferença simétrica
# dif_simetrica = conjunto1 ^ conjunto2  # ou conjunto1.symmetric_difference(conjunto2)
# print(dif_simetrica)  # Saída: {1, 2, 5, 6}

# # Verificar subconjunto
# print({1, 2}.issubset(conjunto1))  # Saída: True
# print(conjunto1.issuperset({1, 2}))  # Saída: True



# # Criando um conjunto com chaves {}
# conjunto1 = {1, 2, 3, 4, 5}
# print(conjunto1)  # Saída: {1, 2, 3, 4, 5}

# # Criando um conjunto com a função set()
# conjunto2 = set([1, 2, 3, 4, 5])
# print(conjunto2)  # Saída: {1, 2, 3, 4, 5}

# Adicionando Elementos
# Para adicionar elementos a um conjunto, utilize o método add().


# conjunto = {1, 2, 3}
# conjunto.add(4)
# print(conjunto)  # Saída: {1, 2, 3, 4}

# Removendo Elementos
# Para remover um elemento de um conjunto, utilize os métodos remove() ou discard(). A diferença entre eles é que remove() gera um erro se o elemento não estiver presente no conjunto, enquanto discard() não gera erro.


# conjunto = {1, 2, 3, 4}
# conjunto.remove(3)
# print(conjunto)  # Saída: {1, 2, 4}

# conjunto.discard(2)
# print(conjunto)  # Saída: {1, 4}

# conjunto.discard(5)  # Não gera erro se o elemento não existir
# print(conjunto)  # Saída: {1, 4}


# # # Criando um dicionário de informações de um usuário

# # usuario = {
# # 'nome': 'João',
# # 'idade': 30,
# # 'cidade': 'São Paulo',
# # 'email': 'joao@example.com'
# # }

# # Acessando valores no dicionário

# # print(usuario['nome'])  # Saída: João
# # print(usuario['idade'])  # Saída: 30

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

