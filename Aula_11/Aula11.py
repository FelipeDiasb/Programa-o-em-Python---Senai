


try:

  a = int(input('Digite um número:'))

  b = int(input('Digite um número:'))

  print(a/b)

except:

 print('O divisor não pode ser zero')

## Outra opção:

# ```python

# a = int(input())
# b = int(input())

# try:
#       print(a/b)

# except ZeroDivisionError as error:
#       print(error)

# else:
#       print( ' Sem erros')

# finally:
#       print('Aqui sempre vai printar')

# ----------------------------------------------------

# def trantando_erros():
#     try: 
#         numero = int(input('>>'))
#     except ZeroDivisionError as erro:
#         print(erro)
#     except ValueError as erro2:
#         print('Erro no valor da variável')  
#     except NameError as erro:
#         print(erro)      
#     finally:
#         print('O sistema foi carregado')

# trantando_erros()

# ---------------------------------------------------------

# def divisao():

#     try:
#       n1 = float(input('>>'))
#       n2 = float(input('>>'))
#       div = n1/n2
#       print(div)  
#     except ZeroDivisionError:
#         print("A divisão não ser por zero")
#     except ValueError:
#         print('Um texo foi digitado')
#     except TypeError as erro:
#         print(erro)

#     else:
#         print('Algo deu errado ')    

     
           
# divisao() 

# import statistics 

# def divisao():
#     try:
#      lista=[0,2,1 , 5]
#      moda  =  statistics.mode(lista)
#      print(moda)
#     except ZeroDivisionError as erro:
#         print(erro)
#     except TypeError:
#         print('Provavelmente digitaram letras')
#     except ValueError as erro :
#         print(erro)
#     except NameError as erro:
#         print(erro)    
#     except SyntaxError as erro:
#         print(erro)     
#     finally:
#         print('Carregamento finalizado')

# divisao()        

  
# ```

# # 

# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

# Exercício 4:
# Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.

# [Praticando…](https://www.notion.so/Praticando-c30ced60bdf64bf7baa00950ae14ce07?pvs=21)