# # # Exercício 1: Crie uma lista chamada pessoas que contenha 
# # # os números inteiros de pessoa1 a pessoa5 e imprima-a na tela.

# # for numeros in range(1,6):
# #     print('pessoa'+str(numeros))


# # # Exercício 2: Acesse e imprima o terceiro elemento 
# # # da lista `numeros`.


# # numeros = [1,2,3,4,5,6]
# # print(numeros[2])



# # # Exercício 3: Adicione o número 9 à lista `numeros` e imprima a
# # #  lista atualizada.

# # # Exercício 4: Remova o número 5 da lista `numeros` 
# # # e imprima a 
# # # lista resultante.

# # # del numeros[4]
# # # numeros.remove(5)
# # print(numeros)



# # # Exercício 5: Crie uma lista chamada carros 
# # # contendo três nomes 
# # # de carros diferentes. Em seguida, concatene 
# # # essa lista com a lista `numeros` e imprima o resultado.



# # concatene =  carros + numeros
# # print(concatene)


# lista  =  [1,2,3]
# carros  =  ['ferrari', 'hb20', 'fusca']
# x =  lista + carros

 
   



# # # Exercício 6: Use um loop `for` para percorrer e 
# # # imprimir todos 
# # # os elementos da lista  = [12,45,45,89,78,3,6,78,87]

# # lista  =  [12,45,45,89,78,3,6,78,87]
# # for n_lista in lista: 
# #     print(n_lista)



# # # Exercício 7: Verifique se o número 5 está 
# # # presente na lista 
# # # `numeros` e imprima uma mensagem informando 
# # # se ele está na 
# # # lista ou não.

# if 5 in numeros: 
#    print('existe')
# else: 
#    print('Não existe')     

# variavel  = 5
# for n in range(5,6):
#     # x  =  int(input('Digite'))
#     if variavel in numeros:
#        print('certo')
#     else: 
#        print('Não esta')     
         
#     # *************************************

#     count(valor): Retorna o número de vezes que um determinado valor aparece na tupla.


# tupla = (1, 2, 2, 3, 4, 2)
# print(tupla.count(2))  # Saída: 3


# index(valor): Retorna o índice da primeira ocorrência de um valor na tupla.


# tupla = (1, 2, 3, 4, 5)
# print(tupla.index(3))  # Saída: 2


# len(tupla): Retorna o número de elementos na tupla.


# tupla = (1, 2, 3, 4, 5)
# print(len(tupla))  # Saída: 5



# sorted(tupla): Retorna uma nova lista ordenada a partir dos elementos da tupla.


# tupla = (5, 3, 1, 4, 2)
# lista_ordenada = sorted(tupla)
# print(lista_ordenada)  # Saída: [1, 2, 3, 4, 5]



# max(tupla) e min(tupla): Retorna o maior e o menor valor na tupla, respectivamente.


# tupla = (5, 3, 1, 4, 2)
# print(max(tupla))  # Saída: 5
# print(min(tupla))  # Saída: 1



# tuple(iterável): Converte um iterável em uma tupla.


# lista = [1, 2, 3]
# tupla = tuple(lista)
# print(tupla)  # Saída: (1, 2, 3)



# unpacking: Permite atribuir os elementos de uma tupla a variáveis individuais.


# tupla = (1, 2, 3)
# a, b, c = tupla
# print(a, b, c)  # Saída: 1 2 3

