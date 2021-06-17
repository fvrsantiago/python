# Faça um sistema que pedirá as seguintes informações:

# Nome
# Idade
# Email
# Telefone

# apresentará o seguinte menu:

# Bem vindo(a)! <nome>

# Opções:

# 1 - Mostrar todas suas informações
# 2 - Mostrar apenas o seu nome e idade
# 3 - Mostrar seu email e telefone
# 0 - Sair

nome = input("DIGITE SEU NOME: ")
idade = str(input("DIGITE SUA IDADE: "))
email = input("DIGITE SEU E-MAIL: ")
telefone = input("DIGITE SEU TELEFONE: ")

while True:
    print("=====================================")
    print(f"BEM VINDO {nome}")
    print("-------------------------------------")
    print("DIGITE:")
    print("1 - Mostrar todas suas informações")
    print("2 - Mostrar apenas o seu nome e idade")
    print("3 - Mostrar seu email e telefone")
    print("0 - Sair")
    print("=====================================")

    opcao = int(input("DIGITE UMA OPCAO: "))
    if opcao == 1:
        print(f"Nome: {nome}\nIdade: {idade}\nE-mail: {email}\nTelefone: {telefone}")
        input("")
    elif opcao == 2:
        print(nome, idade)
    elif opcao == 3:
        print(email, telefone)
    else:
        print("Obrigado por usar nosso sistema!")
        break

