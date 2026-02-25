# login_simples

Mini Projeto: Sistema de Login em Python
Este é um pequeno projeto em Python que simula um sistema simples de login com limite de tentativas. O usuário deve inserir um nome de usuário e senha corretos dentro de três tentativas; caso contrário, o acesso é bloqueado temporariamente.

 ## Funcionalidades
- Solicita usuário e senha via terminal.
- Valida as credenciais comparando com valores pré-definidos.
- Permite até 3 tentativas antes de bloquear o acesso.
- Exibe mensagens claras de sucesso ou bloqueio.

## Lógica do Programa
O programa utiliza um loop while que continua pedindo usuário e senha enquanto:
- As credenciais estiverem incorretas e
- O número de tentativas for menor que 3.
Se o usuário acertar, o programa exibe uma mensagem de sucesso.
Caso contrário, após três tentativas falhas, o acesso é bloqueado.
