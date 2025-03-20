# Crie um sistema de notas, com as seguintes operações:
# ***Utilize While ou for*** 
# # Sistema de notas de alunos

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga que a conta bloqueada 
# - Inserir notas 
# - Fazer a média



logins = []
senhas = []
for i in range(1,3):
    cad_login = input('login usuario:' )
    cad_senha = input('Senha usuario:')
    print('Cadastro usuario', i)
    logins.append(cad_login)
    senhas.append(cad_senha)
    print(logins)
    print(senhas)



acessar_sis = input('Deseja acessar o sistema? s/n')
lista_notas = []
c = 3
while acessar_sis == 's':
      senha_usu =  input('Senha: ')
      login_usu = input('Login: ')
      if senha_usu in senhas and login_usu in logins:        
               while c >0:
                print('Seja bem vindo(a) ao sistema de notas')
                qua = int(input('Digite a quantidade'))
                for n in range(0,qua):
                    nome = input('Digite o nome do aluno')
                    nota1 = float(input('Nota:'))
                    nota2 = float(input('Nota:'))
                    lista_notas.extend([nota1, nota2])
                    media = (nota1 +  nota2)/len(lista_notas)
                    print('média', media)
                    break

                else:
                    print('digite algo errado',c,'chances')
                    c=c-1
      else:
           print('Acesso bloqueado') 
           break        
        

n = input('Digite enter para sair')
