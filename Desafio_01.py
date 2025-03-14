
# - ***Desafio 1 Condicionais***

# ***Crie um sistema de e-commerce, onde o usuário possa:***

# *Utilize variáveis, listas, condicionais*

# Foco resolver o problema

# Vamos trabalhar:

# ***Criatividade | Pensamento lógico | Flexibilidade cognitiva***

# - ***cadastrar-se***
# - ***comprar um produto***
# - ***descobrir o valor total***
# - ***pagar***



print('                                            ')
print('-----------E-commercer------------- ')

print(''' 
         |  Cadastre-se  |
          ---------------          ''')

nome = str(input('Digite seu Nome:'))
idade = int(input('Digite sua Idade:'))
Email = str(input('Digite o E-mail:'))
senha = int(input('Digite sua senha:'))




print('                                     ')
print('                                     ') 
print(f'{nome}, Seja bem-vindo! Cadastro realizado com sucesso!')
print('                                                       ')
print('Deseja continuar para acessar nossos produtos: Opções 1 Sim ♥ --> 2  Não')


op = int(input())

if op == 1:
    print('Nossos produtos listados abaixo:')
elif op == 2:
    print('Obrigado pelo cadastro!')
    exit() 
else:
    print('Opção inválida!')


# - comprar um produto

print('''
Escolha um produto a partir Código do produto:
0-books
1-Manuais e apostilas
2-Infográficos
3-softwares
4-Podcasts
''')

carrinho_prod =  ['-books', 'Manuais e apostilas', 'Infográficos','softwares','Podcasts']
carrinho_valores  =  [20.50,15.00,25,150.00,10.00]

opcao =  int(input('Digite o ID do Produto: '))

compra = []
total =  []

if opcao == 0:
    compra.append(carrinho_prod[opcao])
    total.append(carrinho_valores[opcao])
    print('-------------------'*2)
    print('                                 ')
    print(f'Produto -  {carrinho_prod[opcao]} valor R$ {carrinho_valores[opcao]}')
elif opcao == 1:
    compra.append(carrinho_prod[opcao])
    total.append(carrinho_valores[opcao])
    print('-------------------'*2)
    print('                                 ')
    print(f'Produto -  {carrinho_prod[opcao]} valor R$ {carrinho_valores[opcao]}')
elif opcao == 2:
    compra.append(carrinho_prod[opcao])
    total.append(carrinho_valores[opcão])
    print('-------------------'*2)
    print('                                 ')
    print(f'Produto -  {carrinho_prod[opcao]} valor R$ {carrinho_valores[opcao]}')
elif opcao == 3:
    compra.append(carrinho_prod[opcao])
    total.append(carrinho_valores[opcao])
    print('-------------------'*2)
    print('                                 ')
    print(f'Produto -  {carrinho_prod[opcao]} valor R$ {carrinho_valores[opcao]}')
    compra.append(carrinho_prod[opcao])
    total.append(carrinho_valores[opcao])
    print('-------------------'*2)
    print('                                 ')
    print(f'Produto -  {carrinho_prod[opcao]} valor R$ {carrinho_valores[opcao]}')
else:
    print('Código invalido')     



print(f'Total - R$ {carrinho_valores[opcao]}')





forma_de_pagamento = {
 1: "PIX",
 2:'Debito',
 3:'DINHEIRO'
 }

print('''
Forma de pagamento:
1: PIX,
2: Debito
3: DINHEIRO
''')

escolha_fr_pag =  int(input('Escolha a forma de pagamento: 1 pix, 2 CC, 3CD, 4 Dinheiro '))

if escolha_fr_pag == 1:
    forma =  forma_de_pagamento[1]
    print(f'Seu pagamento vai ser efetuado em {forma}')
elif escolha_fr_pag == 2:
    forma =  forma_de_pagamento[2]
    print(f'Seu pagamento vai ser efetuado em {forma}')  
elif escolha_fr_pag == 3:
    forma =  forma_de_pagamento[3]
    print(f'Seu pagamento vai ser efetuado em {forma}')
else: 
    print('Digite algo valido: ')        

