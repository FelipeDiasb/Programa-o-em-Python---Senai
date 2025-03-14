



# EXERCÍCIOS: 

print( '1 ----------------------------Exercício -----------------------')

# Peça para o usuário digitar um número, verifique se um número 
# é positivo, negativo ou zero.

n = int(input('Digite um número: '))

if n  ==  0:
    print('O número é correspondente a zero')  
elif n < 0: 
    print('O número é negativo')
else:
    print ('Número positivo')

print(''

'')


print( '2 ----------------------------Exercício -----------------------')
# Peça para o usuário digitar a idade, verifique 
# se uma pessoa pode votar com base na idade.
print('Verificação de  idade para votação')
idade =  int(input('Digite a idade:'))
if idade >= 18:
     print('Maior de idade')
else: 
      print('menor de idade')    

print(''

'')



print( '3 ----------------------------Exercício -----------------------')

# # Declara uma variável com um número qualquer, 
# #determine se um número é par ou ímpar.
print('Números pares e impares')
n  = int(input('Digite um número:'))

if n % 2 == 0:
    print('Par')
else:
    print('impar') 

print(''

'')





print( '4 ----------------------------Exercício -----------------------')

# # Usuário vai digitar 3  números, para criar um triângulo, 
# #verifique se um triângulo é equilátero, isósceles ou escaleno

print('Tipos de Triangolos ')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 == n2 == n3:
   print('Equilatero') 
elif n1 == n2 and  n2!= n3  or  n1== n3 and n2 != n3:
   print('Isoceles') 
else:
  print('Escaleno')



print( '5 ----------------------------Exercício -----------------------')

# # Determine se um número é múltiplo de 5 e 7.
print('Números múltiplos')
n = int(input('Digite um número:'))

if n % 5 == 0 and n % 7 ==0: 
   print('É multiplo')
else: 
   print('Não é')



print( '6 ----------------------------Exercício -----------------------')

# # Verifique se um número é positivo e maior que 10

print('Verificão se o número é maior e positivo ')
n1  =  int(input())

if  n1 > 0 and n1 >10:

    print('Esse número é mair e positivo:')  

else: 

    print('Não é')




print( '7 ----------------------------Exercício -----------------------')

# # Verifique se um número é divisível por 3 ou 5.
    
print('O número é divisível por 3 e 5')   
n4 =  int(input('Entre com um número:'))

if n4 % 3 ==0 or n4 % 5 ==0: 
    print('Divisivel')
else:
    print('Não é ')
   
   
   

   
   
   
# # # 1* 
# # # Peça para o usuário digitar um número, verifique se um número é positivo, 
# # # negativo ou zero.

# # numero = int(input('Digite um número'))

# # if numero > 0:
# #     print('Positivo')
# # elif numero < 0:
# #     print('negativo')
# # else: 
# #     print('é zero')        



# # # 2*

# # # Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# # # base na idade.

# # idade  = int(input('Digite sua idade'))
# # if idade > 15 and idade < 66:
# #     print('Pode votar')
# # else: 
# #     print('Não pode votar')    




# # 3*

# # Declara uma variável com um número qualquer, determine se 
#     #um número é par ou ímpar.


# # numero = 15

# # if int(numero/2)*2 == numero:
# #     print('Par')
# # else: 
# #     print('Impar')    



# # 4*

# # Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# # é equilátero, isósceles ou escaleno

# # Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# # Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# # Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# # a = int(input('lado1'))
# # b = int(input('lado2'))
# # c = int(input('lado3'))

# # if a == b  == c:
# #    print('equilatero')
# # elif a != b or a != c or b == c or b != c :
# #     print('isóceles')
# # else:
# #     print('escaleno')    





# # 5*

# # Determine se um número é múltiplo de 5 e 7.
    
# # numero = int(input('digite um numero'))
# # if numero % 5 == 0 and numero % 7 == 0:
# #     print('é multiplo')
# # else: 
# #     print('Não é')    



# # 6*

# # Verifique se um número é positivo e maior que 10


# # numero = int(input('digite um numero'))

# # if numero > 0 and numero>10:
# #     print('verdadeiro')
# # else:
# #     print('Falso')    



# # 7*

# # Verifique se um número é divisível por 3 ou 5.
    

# # numero = int(input('digite um numero'))
# # if numero % 3 == 0 or numero % 5 == 0:
# #     print('é multiplo')
# # else: 
# #     print('Não é')  



# -------------------------------------------------


# # Cada cliente deve escolher um quarto para sua estadia.
# # O preço da diária varia conforme o tipo de quarto:
# # Simples: R$ 100,00 por dia.
# # Duplo: R$ 150,00 por dia.
# # Luxo: R$ 250,00 por dia.

# QUARTOS = ['SIMPLES', 'DUPLO', 'LUXO']



# simples = 100
# duplo = 150
# luxo = 250


# quartos1 = int(input('Quarto?'))


# if  quartos1 == 0:
#      print(f'Quaro escolhido {QUARTOS[0]}')
# elif quartos1 == 1:
#      print(f'Quaro escolhido {QUARTOS[1]}')   
# elif quartos1 == 2:
#      print(f'Quaro escolhido {QUARTOS[2]}')








# dias_cliente1  = int(input('Digite a quantidade de dias'))

# if  dias_cliente1 == 1:
#     total  = dias_cliente1 * simples 
#     print(f'Valor total do cliente 1 R$ {total}')
# elif dias_cliente1 == 2:
#      total  = dias_cliente1 * duplo 
#      print(f' Valor total do cliente 1 R$ {total}')   
# elif dias_cliente1 == 3:
#      total  = dias_cliente1 * luxo
#      print(f' Valor total do cliente 1 R$ {total}')


# dias_cliente2  = int(input('Digite a quantidade de dias'))

# if  dias_cliente2 == 1:
#     total2  = dias_cliente2 * simples 
#     print(f' Valor total2 do cliente 1 R$ {total2}')
# elif dias_cliente2 == 2:
#      total2  = dias_cliente2 * duplo 
#      print(f' Valor total2 do cliente 1 R$ {total2}')   
# elif dias_cliente2 == 3:
#      total2  = dias_cliente2 * luxo
#      print(f' Valor total2 do cliente 1 R$ {total2}')



# dias_cliente3  = int(input('Digite a quantidade de dias'))

# if  dias_cliente3 == 1:
#     total3  = dias_cliente3 * simples 
#     print(f' Valor total3 do cliente 1 R$ {total3}')
# elif dias_cliente3 == 2:
#      total3  = dias_cliente3 * duplo 
#      print(f' Valor total3 do cliente 1 R$ {total3}')   
# elif dias_cliente3 == 3:
#      total3  = dias_cliente3 * luxo
#      print(f' Valor total3 do cliente 1 R$ {total3}')          
