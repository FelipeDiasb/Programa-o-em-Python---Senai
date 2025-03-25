# Exercício 1:
# Peça ao usuário para inserir um número e 
# manipule a exceção caso ele insira algo que não seja um número inteiro.

while True:
    try:
        numero = int(input("Por favor, insira um número inteiro: "))
        print(f"Você inseriu o número {numero}.")
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Erro: Você deve inserir um número inteiro válido. Tente novamente.")


# Explicação:
# try: Tenta converter a entrada do usuário para um número inteiro.

# except ValueError: Captura a exceção se o usuário inserir algo que não seja um número inteiro.

# while True: Mantém o programa rodando até que uma entrada válida seja fornecida.

# break: Sai do loop assim que o usuário insere um número inteiro corretamente.


# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule
# a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

while True:
    try:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
        break  # Sai do loop se a operação for bem-sucedida
    except ValueError:
        print("Erro: Você deve inserir números inteiros válidos. Tente novamente.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero. Insira um número diferente de zero para o divisor.")


# Explicação:
# try: Tenta converter as entradas e realizar a divisão.

# except ValueError: Captura o erro caso o usuário insira algo que não seja um número inteiro.

# except ZeroDivisionError: Captura o erro caso o usuário tente dividir por zero.

# while True: Mantém o programa rodando até que uma entrada válida seja fornecida.

# break: Sai do loop assim que a operação for bem-sucedida.

# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice. Manipule a exceção caso o índice seja inválido
# (caso imprima um indice que não exista na lista).

def get_element(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Erro: Índice fora do intervalo válido."
    except TypeError:
        return "Erro: O índice deve ser um número inteiro."

# Exemplo de uso
lista_exemplo = [10, 20, 30, 40, 50]
indice = int(input("Digite o índice do elemento que deseja acessar: "))

print(get_element(lista_exemplo, indice))

#  Explicação:

# A função tenta acessar o elemento na posição informada.

# Se o índice estiver fora do intervalo, a exceção IndexError é capturada e uma mensagem de erro é retornada.

# Se o índice for de um tipo inválido (exemplo: string), a exceção TypeError será tratada.



# Exercício 4:
# Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.

def dividir_numeros(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = dividir_numeros(num1, num2)
print("Resultado:", resultado)


# Explicação:

# A função dividir_numeros(a, b) tenta dividir a por b.

# Se b for 0, a exceção ZeroDivisionError será tratada e uma mensagem de erro será exibida.

# O código permite inserir números decimais, tornando-o mais flexível.


# **************************************************************
# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não
#seja um número inteiro.

# try:
#     numero =  int(input('Insira um número: '))
# except TypeError:
#     print('Você inseriu um tipo de dado incorreto')
# except ValueError:
#     print('Você inseriu um tipo de dado incorreto')
# else:
#    print(numero)




# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de
# divisão. Manipule a exceção caso ocorra um erro na operação
# #-ZeroDivisionError.
# import random

# chances = 3

# while  chances > 0:
#    chances = chances - 1
#    n  =   int(input('Digite um numero> '))
#    r = random.randint(1,2)

#    if n  == r : 
#       print(f'vc ganhou o jogo, o número é: {r}') 
#       break
#    else: 
#       print(f'Voc perdeu o jogo, o número é {r}')     

#    try:
#     n1 =  int(input('Insira o numero 1: '))
#     n2 =  int(input('Insira o numero 2: '))
#     div  =  n1 / n2
#     print(div)
#    except ZeroDivisionError:
#     print('O divisor não pode ser 0')
#    except ValueError:
#     print('O Precisa ser um número')

# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e 
# retorne o elemento naquele índice.
# Manipule a exceção caso o índice seja inválido(caso imprima um indice que não 
# exista na lista).

# def mostrar_indice(number):
#     lista = [1,2,3,4,5,6]
    
#     try:
#         print(lista[number])
#     except IndexError:
#        print('Esse indice não existe')


# number  =  int(input('Digite o valor do indice'))   
# mostrar_indice(number)         
     




# Exercício 4:
# Crie uma função que divida dois números e manipule a exceção 
#caso o divisor seja zero.


# def div():
#     try:
#        n  = int(input())
#        n1  = int(input()) 
#        print('Divisão >   ', n / n1)
#     except ZeroDivisionError: 
#       print('Não pode dividir por zero')



# div()



# # Exercício 1:
# # Peça ao usuário para inserir um número e manipule a exceção caso ele insira 
# # algo que não seja um número inteiro.


# # def verificar():
# #     try:
# #        numero  =  int(input('>>'))
# #        print(numero - 1)
# #     except ValueError as erro:
# #        print(erro) 
# #     finally:
# #         print('Fim do carregamento!')

# # verificar()       




# # Exercício 2:
# # Peça ao usuário para inserir dois números e realize uma 
# # operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.



# def verificar2():
#     try:
#        numero2  =  int(input('>>'))
#        numero3  =  int(input('>>'))
#        result  = numero2/numero3

#     except ValueError as erro:
#        print(erro) 
#     except ZeroDivisionError as erro:
#        print(erro)  
#     else: 
#        print(result)     
#     finally:
#         print('Fim do carregamento!')

# verificar2()  


# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele 
# índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).


# def handle(lista):
#     try: 
#         n = int(input(':'))
#         i = lista[n]
#     except ValueError:
#         print('Utilize números apenas!')    
#     except IndexError:
#         print('Esse indice não existe na lista!', n)
#     else: 
#         print(f'Essa é a lista: {lista}, e esse é o valor {i}, indice é o {n}')



# lista =  [1,4,6,56,6,56,65]
# handle(lista)


# # Exercício 4:
# # Crie uma função que divida dois números e manipule a 
# # exceção caso o divisor seja zero.


# def verificar3():
#     try:
#        numero2  =  int(input('>>'))
#        numero3  =  int(input('>>'))
#        result  = numero2/numero3
#        print(result)

#     except ZeroDivisionError:
#        print('O divisor não pode ser zero!')  
   


# verificar3()





# # # Exercício 1:
# # # Peça ao usuário para inserir um número e manipule a 
# # exceção caso ele insira  algo que não seja um número inteiro.

# # # Exercício 2:
# # # Peça ao usuário para inserir dois números e realize uma 
# # # operação de divisão. Manipule a exceção caso ocorra um 
# # erro na operação.

# def pega_numero1():

#     try : 
#         number  =  int(input())
#         return number 
#     except ValueError:
#         print('Esse valor que foi inserido não é valido')


# def pega_numero2():
    
#     try: 
#         number  =  int(input())
#         return number 
#     except ValueError:
#         print('Esse valor que foi inserido não é valido')







# def verificar():

#      try:

#         numero1  =  pega_numero1()
#         numero2  =  pega_numero2()
#         result  =  numero1/numero2

   
   
#      except ZeroDivisionError as erro:        
#             print(erro)
#      else: 
#             print(result)       
#      finally:
#             print('Fim do carregamento!')


# verificar()       



# # Exercício 1:
# # Peça ao usuário para inserir um número 
# # e manipule a exceção caso ele insira algo 
# # que não seja um número inteiro.
# try:
#   n =  int(input('>>'))
# except:
#   print('Algo deu errado')  



# # Exercício 2:
# # Peça ao usuário para inserir dois números 
# # e realize uma operação de divisão. 
# # Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
# def divisao():
#     try:
#         n1 =  int(input('>>'))
#         n2 =  int(input('>>'))
#         op  =  n1 / n2
#         print(op)
#     except ZeroDivisionError:
#           print('O divisor não pode ser zero')  

# divisao()






# # def indice():                  
# #     try:
# #         lista = [1,2,3]
# #         indice = int(input('>>'))
# #         print(lista[indice])
# #     except IndexError:
# #             print('Não existe esse indice')

# # indice()




# # # try: 

# # #     numero = int(input('Digite um número'))
# # #     numero2 = int(input('Digite um número'))
# # #     soma = numero +  numero2
# # #     print(soma)
# # # except ZeroDivisionError as erro:
# # #     print(erro)
# # # except ValueError as erro:
# # #     print(erro)    
# # # except TypeError as erro:
# # #     print(erro)
# # # except:
# # #     print('Algo deu errado')    
# # # finally:
# # #     print('Fim de carregamento')    
  