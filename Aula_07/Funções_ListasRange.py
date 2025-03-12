
# # Funções_listas 

# lista_vazia = [] # vazia  

# #       -5 -7 -6 -5 - 4 -3 - 2 -1

# lista = [1,10,5,3,20,'a' True,5.2]
# lista_f = [5.3,5.2,8.4,10.8]
# lista_i = [1,5,6,10,5,32,45]
# lista_b = [True, False]
# lista_str = ['palavras'] 


# lista[0] = 100 
# lista[1] = 200
# # lista[8] = 200
# lista[0] = lista[1] * 2
# print(lista)

# numero = lista[2]
# numero2  = lista[3]

# soma = numero + numero2


# print(dir(lista))

# print(soma)

# # inserir dados 
# # append() - insert() - +=() extend()

# lista = [1,10,5,3,20,'a' True,5.2]
# print('Original: ', lista)
# lista.append(250)
# lista.append('teste') # vai colocar 1 dados no final
# lista.insert(0,'ola') # o insert no indise escolhido e vai empurra o outro para frente e coloca o 'Olá'
# lista +=(100,200,300,2500,250)# add varios dados de uma só vez
# lista.extend([500,200,30,20,20])# add varios de uma só vez

# print('ALTERAÇÃO',lista)

# #remover dados 
# # pop del remove


# lista.pop() # remove o ultimo indice da lista
# lista.pop(2) 

# del lista[3]# remove de dentro para fora
# lista.remove('a')# remove  oque é visto na lista



# # Contar, quanto tem um valor


# lista  = [1,2,2,2,3,,4,3,5,8,2,2,]
# print(lista.count(20)) # contar, quanto tem um determinado valor 


# #len - tamanho cumprimento 

# tamanho = len(lista)
# print(tamanho)


# # max 

# Maior = max(lista)

# Menor = min(lista)
# print(Menor)


# # index


# print('onde está no indice',lista.index(8)) # verificação 

# lista1 = (lista1.clear())
# lista =  lista
# print(lista.clear())


# print( lista)
# lista.clear
# lista.copy



# lista_1 = list(range(1,33)) # para criar uma lista
#print(lista_1)


#0


pares = list (range(1,11, 2))
print(pares)

print()
#pront.windows (lista)
 # 1 
numeros_i  = list(range(1,11))
print(numeros_i)

# 2 
print(numeros_i[2])

# 3 
numeros_i.append(9)
print(numeros_i)

#4
numeros_i.remove(5)
print(numeros_i)

#5 
carros = ['onix','Gol','HRV']
resultando = numeros_i + carros
print(resultando)


