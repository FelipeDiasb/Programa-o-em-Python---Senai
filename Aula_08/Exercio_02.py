<!-- - ***Desafio 1 Condicionais***

***Crie um sistema de e-commerce, onde o usuário possa:***

*Utilize variáveis, listas, condicionais*

Foco resolver o problema

Vamos trabalhar:

***Criatividade | Pensamento lógico | Flexibilidade cognitiva***

- ***cadastrar-se***
- ***comprar um produto***
- ***descobrir o valor total***
- ***pagar***

___________________________________________________________________________________

- ***Desafio 2:  Condicionais***

***Sistema de Reservas de Hotel:***

***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

- *Cadastro de Cliente:*

*O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

- *Reservas de Quartos:*

***O sistema deve oferecer 3 tipos de quartos:*** 

***"Simples", "Duplo" e "Luxo".***

***Cada cliente deve escolher um quarto para sua estadia.
O preço da diária varia conforme o tipo de quarto:
Simples: R$ 100,00 por dia.
Duplo: R$ 150,00 por dia.
Luxo: R$ 250,00 por dia.***

- ***Cálculo da Estadia:***

***O usuário deve informar quantos dias cada cliente ficará no hotel.
O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

Exemplo: 

 ***valor_cliente3 = preco_duplo * cliente3_dias***

*Pagamento:*

*O sistema deve exibir o valor total a ser pago por cada cliente após a aplicação do desconto.*

*Regras Adicionais:
Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*

***O sistema não deve usar loops (for, while) nem funções.**
O código deve considerar todos os casos possíveis de escolha dos clientes.* -->

print('E-commerce X')
nome = input('Digite seu nome: ')
usuario = input('Digite seu usuario: ')
email = input('Digite seu e-mail: ')
senha = input('Digite seu senha: ')

print('olá', nome, 'seu usuário é ', usuario)

senha_dig = input('Senha: ')
usuario_dig = input('Usuário: ')

if  senha_dig == senha and usuario_dig == usuario: 
    print('Seja bem vindo(a)', nome, 'faça seu pedido:')
    menu = {
     'camiseta': 150.00,
     'meia': 50.00,
     'computador': 20.000,
     'fone': 100.00

    }
    print('produtos: ', menu )
    
    meus_produtos  = []
    total_pagar  = []
    pedido1 = input('digite o produto')
    pedido2 = input('digite o produto')
    pedido3 = input('digite o produto')
    
    meus_produtos +=(pedido1, pedido2, pedido3)
    total_pagar  += [menu[pedido1], menu[pedido2], menu[pedido3]]

    print('SEUS PEDIDOS:')
    print(meus_produtos)
    print(total_pagar)
    
    soma =  sum(total_pagar)
    float(soma)
    print('TOTAL DA COMPRA:')
    print('R$', soma)

    forma_pag = input('''
    ESCOLHA A FORMA DE PAGAMENTO:
    1 -  PIX
    2 - CC
    3 - PAYPALL
       
    ''')

    if forma_pag == '1':
        print('Seu pagamento foi efetuado com PIX: R$ ', soma )
    elif forma_pag == '2':
        print('Seu pagamento foi efetuado com CC: R$ ', soma )
    elif forma_pag == '3':
        print('Seu pagamento foi efetuado com PYPALL: R$ ', soma )   
    else: 
        print('digite algo valido')    

else: 
    print('Algo foi digitado errado')    




....................................................


# - Desafio 1 Condicionais

# Crie um sistema de e-commerce, onde o usuário possa:

# *Utilize variáveis, listas, condicionais*

# Foco resolver o problema

# Vamos trabalhar:

# Criatividade | Pensamento lógico | Flexibilidade cognitiva

# - cadastrar-se


nome   = []
idades = []
emails = []
senhas = []

my_nome, minha_idade, meu_email, minha_senha  =  input('Digite seu nome'),input('Digite sua idade'), input('Digite seu email'),input('Digite sua senha') 

nome.append(my_nome)
idades.append(minha_idade)
emails.append(meu_email)
senhas.append(minha_senha)

print('DADOS INSERIDOS COM SUCESSO!')

print(f'SEJA BEM VINDO(A) {nome[0]}')

dados = (nome[0],idades[0],emails[0],senhas[0])
print(dados)

# - comprar um produto

print('''
Escolha um produto a partir do ID
id 0 - a
id 1 - b
id 2 - c            

''')

menu =  ['a', 'b', 'c']
valores  =  [20.5,150,250]

escolha =  int(input('Digite o ID do Produto: '))

meu_carrinho = []
meu_total =  []

if escolha == 0:
    meu_carrinho.append(menu[escolha])
    meu_total.append(valores[escolha])
    print('.....................')
    print(f'Produto -  {menu[escolha]} valor R$ {valores[escolha]}')
elif escolha == 1:
    meu_carrinho.append(menu[escolha])
    meu_total.append(valores[escolha])
    print('.....................')
    print(f'Produto -  {menu[escolha]} valor R$ {valores[escolha]}')
elif escolha == 2:
    meu_carrinho.append(menu[escolha])
    meu_total.append(valores[escolha])
    print('.....................')
    print(f'Produto -  {menu[escolha]} valor R$ {valores[escolha]}')
else:
    print('Digitação incorreta')     




# - 

print(f'Total - R$ {valores[escolha]}')





forma_de_pagamento = {
1: "PIX",
2:'CC',
3:'CD',
4:'DINHEIRO'
}


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
elif escolha_fr_pag == 4:
    forma =  forma_de_pagamento[1]
    print(f'Seu pagamento vai ser efetuado em {forma}')  
else: 
    print('Digite algo valido: ')        









---------------------------------------------------------------




cliente1_nome = input('Digite o nome do Cliente 1: ')
cliente1_idade = int(input('Digite a idade do Cliente 1: '))

cliente2_nome = input('Digite o nome do Cliente 2: ')
cliente2_idade = int(input('Digite a idade do Cliente 2: '))

cliente3_nome = input('Digite o nome do Cliente 3: ')
cliente3_idade = int(input('Digite a idade do Cliente 3: '))


print('Tipos de Quarto: Simples, Duplo, Luxo')

cliente1_quarto = input('Escolha o quarto para o Cliente 1: ')
cliente2_quarto = input('Escolha o quarto para o Cliente 2: ')
cliente3_quarto = input('Escolha o quarto para o Cliente 3: ')

# preço quartos
preco_simples = 100
preco_duplo = 150
preco_luxo = 250

cliente1_dias = int(input(f'Quantos dias o Cliente 1 ({cliente1_nome}) ficará hospedado? '))
cliente2_dias = int(input(f'Quantos dias o Cliente 2 ({cliente2_nome}) ficará hospedado? '))
cliente3_dias = int(input(f'Quantos dias o Cliente 3 ({cliente3_nome}) ficará hospedado? '))


if cliente1_quarto == 'simples':
    valor_cliente1 = preco_simples * cliente1_dias
elif cliente1_quarto == 'duplo':
    valor_cliente1 = preco_duplo * cliente1_dias
else:
    valor_cliente1 = preco_luxo * cliente1_dias

if cliente2_quarto == 'simples':
    valor_cliente2 = preco_simples * cliente2_dias
elif cliente2_quarto == 'duplo':
    valor_cliente2 = preco_duplo * cliente2_dias
else:
    valor_cliente2 = preco_luxo * cliente2_dias

if cliente3_quarto == 'simples':
    valor_cliente3 = preco_simples * cliente3_dias
elif cliente3_quarto == 'duplo':
    valor_cliente3 = preco_duplo * cliente3_dias
else:
    valor_cliente3 = preco_luxo * cliente3_dias


print(f'Cliente 1: {cliente1_nome}, {cliente1_idade} anos, Quarto {cliente1_quarto}, {cliente1_dias} dias')
print(f'Valor Total Cliente 1: R$ {valor_cliente1:.2f}')

print(f'Cliente 2: {cliente2_nome}, {cliente2_idade} anos, Quarto {cliente2_quarto}, {cliente2_dias} dias')
print(f'Valor Total Cliente 2: R$ {valor_cliente2:.2f}')

print(f'Cliente 3: {cliente3_nome}, {cliente3_idade} anos, Quarto {cliente3_quarto}, {cliente3_dias} dias')
print(f'Valor Total Cliente 3: R$ {valor_cliente3:.2f}')







---------------------------------------------------------------
opção 3 

escolhas_quartos  = []
clientes =  []
meus_valores = []
quartos = ['SIMPLES','DUPLO','LUXO']
lista_precos =  [100.0,150.0,250.]
lista_desconto = [0.2,0.5,0.6]

print('''Sejam bem vindos,
Cadastre-se e
Escolha o ID  do quarto
SIMPLES(0),DUPLO(1),LUXO(2)''')

nome1 = input('nome1 : ')
idade1 = int(input('idade:'))
quarto1 = int(input('Escolha o ID quarto'))
dias1 = int(input('quantidade de dias'))

nome2 = input('nome1 : ')
idade2 = int(input('idade:'))
quarto2 = int(input('Escolha o ID quarto'))
dias2 = int(input('quantidade de dias'))

nome3 = input('nome1 : ')
idade3 = int(input('idade:'))
quarto3 = int(input('Escolha o ID quarto'))
dias3 = int(input('quantidade de dias'))


clientes.extend([nome1,nome2, nome3])
escolhas_quartos+=(quartos[quarto1],quartos[quarto2], quartos[quarto3])
meus_valores+=(lista_precos [quarto1],lista_precos [quarto2],lista_precos[quarto3])

cal1 = (lista_precos[quarto1] * dias1) 
cal2 = (lista_precos[quarto2] * dias2) 
cal3 = (lista_precos[quarto3] * dias3) 

print('****' * 21)

print(f'''

Quartos escolhidos -  {escolhas_quartos}

Valores escolhidos  -  {meus_valores}

Cliente 1 -  {nome1}
**********************************
QUARTO - {quarto1}
DIAS - {dias1}
VALOR R$ {cal1 * (20/100)}
**********************************
Cliente  2  -  {nome2 }

QUARTO - {quarto2}
DIAS - {dias2}
VALOR R$ {cal2 * ( 1 - 0.5)}
**********************************
Cliente 3  -  {nome3}

QUARTO - {quarto3}
DIAS - {dias3}
VALOR R$ {cal3 * ( 1 - 0.6)}

''')


----------------------------------------


escolhas_quartos  = []
clientes =  []
meus_valores = []
quartos = ['SIMPLES','DUPLO','LUXO']
lista_precos =  [100.0,150.0,250.]
lista_desconto = [0.2,0.5,0.6]

print('''Sejam bem vindos,
Cadastre-se e
Escolha o ID  do quarto
SIMPLES(0),DUPLO(1),LUXO(2)''')

nome1 = input('nome1 : ')
idade1 = int(input('idade:'))
quarto1 = int(input('Escolha o ID quarto'))
dias1 = int(input('quantidade de dias'))

nome2 = input('nome1 : ')
idade2 = int(input('idade:'))
quarto2 = int(input('Escolha o ID quarto'))
dias2 = int(input('quantidade de dias'))

nome3 = input('nome1 : ')
idade3 = int(input('idade:'))
quarto3 = int(input('Escolha o ID quarto'))
dias3 = int(input('quantidade de dias'))


clientes.extend([nome1,nome2, nome3])
escolhas_quartos+=(quartos[quarto1],quartos[quarto2], quartos[quarto3])
meus_valores+=(lista_precos [quarto1],lista_precos [quarto2],lista_precos[quarto3])

cal1 = (lista_precos[quarto1] * dias1) 
cal2 = (lista_precos[quarto2] * dias2) 
cal3 = (lista_precos[quarto3] * dias3)

d1 = cal1 * 0.20
d2 = cal2 * 0.50
d3 = cal3 * 0.60

print('****' * 21)

print(f'''

Quartos escolhidos -  {escolhas_quartos}

Valores escolhidos  -  {meus_valores}

Cliente 1 -  {nome1}
**********************************
QUARTO - {quarto1}
DIAS - {dias1}
VALOR R$ {cal1}
DESCONTO R${d1}
VALOR R$ {cal1 - d1}
**********************************
Cliente  2  -  {nome2 }

QUARTO - {quarto2}
DIAS - {dias2}
VALOR R$ {cal2}
DESCONTO R${d2}
VALOR R$ {cal2 - d2}
**********************************
Cliente 3  -  {nome3}

QUARTO - {quarto3}
DIAS - {dias3}
VALOR R$ {cal3}
DESCONTO R${d3}
VALOR R$ {cal3 - d3}

''')




