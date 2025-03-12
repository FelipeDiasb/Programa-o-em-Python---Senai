
# Crie um e-commerce com a estrutura de dicionários.

# Produtos:  Livros, tablets e fones de ouvido

# As ações: 

# Comprar()

# Pagar()

# mostra o valor da compra

# documentação 

# [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

print('E-commere')

produtos =  ['Livros ', 'tablets','fones de ouvido']
valores  =  [10.0,15.00,8.00]
carrinho = []
meu_valores = []

produto1 =  int(input('''
0 - ARROZ
1 - FEIJÃO 
2 - MACARRÃO
3 - MOLHO
>> '''))

produto2 = int(input('''
0 - ARROZ
1 - FEIJÃO 
2 - MACARRÃO
3 - MOLHO
>> '''))


carrinho = [produtos[produto1], produtos[produto2]]
meu_valores = [valores[produto1], valores[produto2]]
SOMA =  sum(meu_valores)

print(f'''
.................................
CUPOM

1 - {produtos[produto1]} R$ {valores[produto1]:.2f}
2 - {produtos[produto2]} R$ {valores[produto2]:.2f}

.................................
R$ {SOMA:.2f}

Compra realizada com sucesso!

''')

