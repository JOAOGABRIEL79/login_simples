usuario = ''
senha = ''
tentativas = 0

while (usuario != 'joao' or senha != '12345b') and tentativas < 3:
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    tentativas += 1

if usuario == 'joao' and senha == '12345b':
    print('Login feito com sucesso')
else:
    print('Favor aguardar 30 minutos')