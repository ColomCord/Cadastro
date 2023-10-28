"""
Aluno: Arthur Colombo Cordeiro
RM: 551262
"""
contatos = {}

"""SUBALGORÍTIMOS"""
def menu():
    print("""MENU
1 - Cadastrar um contato
2 - Listar os contatos
3 - Editar Contatos
0 - SAIR""")


def cadastro():
    instagram = input("Instagram: @")
    if instagram in contatos:
        print("INSTAGRAM JÁ CADASTRADO")
        print(f"Instagram: @{instagram}")
        print(f"Nome: {contatos[instagram]['nome']}")
        print(f"E-mail: {contatos[instagram]['email']}")
    else:
        nome = input("Nome: ")
        email = input("E-mail: ")

        contatos[instagram] = {'nome': nome, 'email': email}
        print("Contato cadastrado com sucesso!")

def lista():
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        print("Lista de Contatos:")
        for instagram, info in contatos.items():
            print(f"Instagram: @{instagram}")
            print(f"Nome: {info['nome']}")
            print(f"E-mail: {info['email']}")
            print()

def editar():
    instagram = input("Instagram: @")
    if instagram in contatos:
        print(f"Instagram: @{instagram}")
        print(f"Nome: {contatos[instagram]['nome']}")
        print(f"E-mail: {contatos[instagram]['email']}")
        print("==> REGISTRO ENCONTRADO, EDITE-O!")

        Nnome = input("Novo Nome: ")
        Nemail= input("Novo E-mail: ")

        contatos[instagram]['nome'] = Nnome
        contatos[instagram]['email'] = Nemail
        print("Contato atualizado com sucesso!")
    else:
        print("CONTATO INEXISTENTE!")

"""CÓDIGO PRINCIPAL"""
while True:
    menu()
    escolha = input("Escolha: ")

    if escolha == '1':
        cadastro()
    elif escolha == '2':
        lista()
    elif escolha == '3':
        editar()
    elif escolha == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")
