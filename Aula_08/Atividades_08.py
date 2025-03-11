

# As estruturas condicionais são fundamentais na programação, permitindo que um programa
#  tome decisões com base em certas condições. Em Python, você pode usar os 
# comandos `if`, `elif` (abreviação de "else if") e `else` para criar fluxos 
# de execução condicionais. Essas estruturas permitem que você execute diferentes 
# blocos de código com base em avaliações de expressões booleanas (verdadeiro ou falso).

# 1. O Comando if:

# O comando if` é a base das estruturas condicionais em Python. Ele avalia uma 
# expressão booleana e executa o bloco de código aninhado apenas se a expressão 
# for verdadeira. A sintaxe básica é a seguinte:

# if expressao_booleana:
#     # Bloco de código a ser executado se a expressão for verdadeira


# CONDICIONAL SIMPLES

# idade = 18
# if idade >= 18:
#     print("Você é maior de idade.")


# A PARTIR DAQUI É COMPOSTA

# 2. O Comando elif:

# O comando elif é usado para testar múltiplas condições em sequência. 
# Ele só é avaliado se as condições anteriores forem falsas. 
# A sintaxe é a seguinte:

# if expressao_booleana1:
#     # Bloco de código a ser executado se a expressão 1 for verdadeira
# elif expressao_booleana2:
#     # Bloco de código a ser executado se a expressão 2 for verdadeira
# else:
#     # Bloco de código a ser executado se nenhuma expressão for verdadeira




# nota = 85
# if nota >= 90:
#     print("Ótimo desempenho!")
# elif nota >= 70:
#     print("Bom desempenho.")
# else:
#     print("Melhorar na próxima.")


# 3. O Comando else:

# O comando else é usado para 
# definir um bloco de código a ser executado quando 
# todas as condições anteriores forem falsas. Ele não tem uma expressão booleana 
# associada, pois é o último caso a ser considerado quando nenhum dos casos anteriores 
# for verdadeiro.



# numero = 7
# if numero % 2 == 0:
#     print("O número não é par.")
# else:
#     print("O número impar.")



# JOGO** ADVINHAÇÃO

# import random

# numero_aleatorio = random.randint(1,10)
# meu_chute  =  int(input('Declare seu chute'))

# if numero_aleatorio == meu_chute:
#     print('Sensacional você acertou em cheio!', numero_aleatorio)
# elif numero_aleatorio > meu_chute:
#     print('Você esta quase lá, o número é maior, tente novamente')    
# elif numero_aleatorio < meu_chute:
#     print('Você esta quase lá, o número é menor, tente novamente')       
# else:
#     print('Errou Feio!', numero_aleatorio)    





# As estruturas condicionais em Python permitem que você crie programas dinâmicos 
# que reagem a diferentes situações. Com o uso de if, `elif` e `else`, você pode 
# controlar o fluxo de execução de acordo com as condições que você define. 
# Isso é essencial para criar programas flexíveis e capazes de lidar com uma 
# variedade de cenários.




# print('MERCADO Z')

# senha  = 123
# login = 'bea@'

# my_login =  input('Digite o login')
# my_senha  = int(input('Digite a sua senha'))

# if my_login == login and my_senha == senha:
#     lista =  ['arroz', 'feijão', 'salada', 'ovos'] # string
#     meu_carrinho = []
#     meu_total = []
#     valores = [10.00,5.0,4.40,12.0] # float
#     print('PRODUTOS')
#     print(f'''digite o ID do produto:
#     0 - Arroz
#     1 - Feijão
#     2 - Salada
#     3 - Ovos            
#     ''')

#     escolha  =  input('Deseja fazer o pedido? s/n')
#     if escolha == 's':
#         produto1 = int(input('>>'))
#         produto2 = int(input('>>'))
#         produto3 = int(input('>>'))
#         meu_carrinho += (lista[produto1],lista[produto2],lista[produto3] )
#         meu_total +=(valores[produto1],valores[produto2], valores[produto3])
#         print('Carrinho:', meu_carrinho)
#         print('Total')
#         soma = sum(meu_total)
#         print(f'R$, {soma:.2f}')
#         print(f'''
#     1 - PIX
#     2 - CC
#     3 - CD                    

#     ''')
#         forma_pag =  input('Digite a forma de pagamento')
  
#         if forma_pag:
#             print('Pagamento efetuado com sucesso volte sempre!')  
#     else:
#         print('Pedido cancelado')
# else:
#     print('dados incorretos - Digite novamente')








# # import random

# # numero_aleatorio = random.randint(1,10)
# # meu_chute  =  int(input('Declare seu chute'))

# # if numero_aleatorio == meu_chute:
# #     print('Sensacional você acertou em cheio!', numero_aleatorio)
# # elif numero_aleatorio > meu_chute:
# #     print('Você esta quase lá, o número é maior, tente novamente')    
# # elif numero_aleatorio < meu_chute:
# #     print('Você esta quase lá, o número é menor, tente novamente')       
# # else:
# #     print('Errou Feio!', numero_aleatorio)    









# # number  =  0

# # if number > 2:
# #     print('é maior que 2 ')

# # if number == 3:
# #     print('é 3 ')

# # if number < 0:
# #     print('é negativo ')

# # if number >200:
# #     print('é maior que 200 ')    

# # # else: 
# # #     print('É menor')    

# # # composta  
    
# # nome  =  input('Digite seu nome: ')
# # lista  =  ['Ana','José','Caio']


# # if nome in lista:
# #     print('Seja bem vindo(a), cliente', nome)
# # elif nome == 'Julia':
# #     print('Seja bem vinda cliente Premium ', nome)
# # elif nome  == '':
# #      print('Esta vazio digite novamente')    
# # else:    
# #     print('Seja bem vindo(a) novo(a) cliente', nome)

# OUTROS EXEMPLOS: 

# meu_carrinho = []
# total_valores = []
# produtos=  ['arroz', 'feijão', 'ervilha']
# valores =  [20.0,18.0,5.]

# produto1 = input('Digite o produto 1')
# produto2 = input('Digite o produto 2')
# produto3 = input('Digite o produto 3')

# # if (produto1, produto2, produto3) == (produtos[0], produtos[1], produtos[2]):
# #     meu_carrinho += (produtos[0], produtos[1], produtos[2])
# #     print(meu_carrinho)
# # if (produto1, produto2, produto3) != produtos:
# #     print('Não existe o produto')

# # if produto1 in produtos or produto2 in produtos or produto3 in produtos:
# #    meu_carrinho.append(produto1)
# #    meu_carrinho.append(produto2)
# #    meu_carrinho.append(produto3)

# # if produto1 in produtos:
# #    meu_carrinho.append(produto1)
# #    print(meu_carrinho)
# #    meu_carrinho2 = meu_carrinho
# # if produto2 in produtos:
# #    meu_carrinho2.append(produto2)
# #    print(meu_carrinho2)
# #    meu_carrinho3 = meu_carrinho2
# # if produto3 in produtos:
# #    meu_carrinho3.append(produto3)



# EXEMPLO COM CONDICIONAIS -  MERCADO 


# produtos = ['arroz', 'Banana', 'Leite', 'feijao', 'pao']
# precos = [1.50, 2.00, 3.20, 2.50, 5.00]


# carrinho = []
# total = 0

# print("Produtos disponíveis:")
# print("1. arroz - R$ 1.50")
# print("2. Banana - R$ 2.00")
# print("3. Leite - R$ 3.20")
# print("4. feijãp - R$ 2.50")
# print("5. pao - R$ 5.00")


# escolha1 = input("Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar): ")

# if escolha1 == '1':
#     carrinho.append(produtos[0])
#     total += precos[0]
# elif escolha1 == '2':
#     carrinho.append(produtos[1])
#     total += precos[1]
# elif escolha1 == '3':
#     carrinho.append(produtos[2])
#     total += precos[2]
# elif escolha1 == '4':
#     carrinho.append(produtos[3])
#     total += precos[3]
# elif escolha1 == '5':
#     carrinho.append(produtos[4])
#     total += precos[4]


# escolha2 = input("Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar): ")

# if escolha2 == '1':
#     carrinho.append(produtos[0])
#     total += precos[0]
# elif escolha2 == '2':
#     carrinho.append(produtos[1])
#     total += precos[1]
# elif escolha2 == '3':
#     carrinho.append(produtos[2])
#     total += precos[2]
# elif escolha2 == '4':
#     carrinho.append(produtos[3])
#     total += precos[3]
# elif escolha2 == '5':
#     carrinho.append(produtos[4])
#     total += precos[4]


# escolha3 = input("Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar): ")

# if escolha3 == '1':
#     carrinho.append(produtos[0])
#     total += precos[0]
# elif escolha3 == '2':
#     carrinho.append(produtos[1])
#     total += precos[1]
# elif escolha3 == '3':
#     carrinho.append(produtos[2])
#     total += precos[2]
# elif escolha3 == '4':
#     carrinho.append(produtos[3])
#     total += precos[3]
# elif escolha3 == '5':
#     carrinho.append(produtos[4])
#     total += precos[4]


# print("\nVocê comprou:")
# if len(carrinho) > 0:
#     print(carrinho)
#     print(f"Total: R$ {total:.2f}")
# else:
#     print("Nenhum produto comprado.")





