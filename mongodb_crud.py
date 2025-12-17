from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")

db = client["ecommerce"]
usuarios = db["usuarios"]

print("=" * 60)
print(" MongoDB + Python ")
print(" CRUD INTERATIVO - MONGODB (DOCUMENTOS)")
print("=" * 60)

def email_existe(email):
    return usuarios.find_one({"email": email}) is not None

def inserir_usuario():
    print("\n--- INSERIR USUÁRIO ---")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("Estado: ").strip()

    if not nome or not email:
        print(" Nome e email são obrigatórios.")
        return

    if email_existe(email):
        print(" Email já cadastrado.")
        return

    usuario = {
        "nome": nome,
        "email": email,
        "endereco": {
            "cidade": cidade,
            "estado": estado
        },
        "pedidos": []
    }

    usuarios.insert_one(usuario)
    print("\n Usuário inserido com sucesso!")
    pprint(usuario)


def listar_usuarios():
    print("\n--- LISTAR USUÁRIOS ---")
    dados = list(usuarios.find())

    if not dados:
        print(" Nenhum usuário cadastrado.")
    else:
        for usuario in dados:
            pprint(usuario)


def buscar_usuario_por_email():
    print("\n--- BUSCAR USUÁRIO POR EMAIL ---")
    email = input("Email: ").strip()
    usuario = usuarios.find_one({"email": email})

    if usuario:
        pprint(usuario)
    else:
        print(" Usuário não encontrado.")


def atualizar_usuario():
    print("\n--- ATUALIZAR ENDERECO ---")
    email = input("Email do usuário: ").strip()

    if not email_existe(email):
        print(" Usuário não encontrado.")
        return

    nova_cidade = input("Nova cidade: ").strip()
    novo_estado = input("Novo estado: ").strip()

    usuarios.update_one(
        {"email": email},
        {"$set": {
            "endereco.cidade": nova_cidade,
            "endereco.estado": novo_estado
        }}
    )

    print("\n Endereco atualizado com sucesso!")
    usuario = usuarios.find_one({"email": email})
    pprint(usuario)


def excluir_usuario():
    print("\n--- EXCLUIR USUÁRIO ---")
    email = input("Email do usuário: ").strip()

    resultado = usuarios.delete_one({"email": email})

    if resultado.deleted_count == 0:
        print(" Usuário não encontrado.")
    else:
        print("\n Usuário excluído com sucesso!")
        print("\n Usuários restantes:")
        for usuario in usuarios.find():
            pprint(usuario)

def adicionar_pedido():
    print("\n--- ADICIONAR PEDIDO ---")
    email = input("Email do usuário: ").strip()

    if not email_existe(email):
        print(" Usuário não encontrado.")
        return

    descricao = (input("descricao do pedido: "))
    status = input("Status do pedido: ")

    pedido = {
        "descricao": descricao,
        "status": status
    }

    usuarios.update_one(
        {"email": email},
        {"$push": {"pedidos": pedido}}
    )

    print("\n Pedido adicionado com sucesso!")
    usuario = usuarios.find_one({"email": email})
    pprint(usuario)

def listar_por_cidade():
    print("\n--- LISTAR USUÁRIOS POR CIDADE ---")
    cidade = input("Cidade: ").strip()

    dados = usuarios.find({"endereco.cidade": cidade})

    encontrou = False
    for usuario in dados:
        pprint(usuario)
        encontrou = True

    if not encontrou:
        print(" Nenhum usuário encontrado para essa cidade.")


def contar_usuarios():
    total = usuarios.count_documents({})
    print(f"\n Total de usuários cadastrados: {total}")

while True:
    print("\n" + "=" * 60)
    print("MENU")
    print("1 - Inserir usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário por email")
    print("4 - Atualizar endereco")
    print("5 - Excluir usuário")
    print("6 - Adicionar pedido")
    print("7 - Listar usuários por cidade")
    print("8 - Contar usuários")
    print("0 - Sair")
    print("=" * 60)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        inserir_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        buscar_usuario_por_email()
    elif opcao == "4":
        atualizar_usuario()
    elif opcao == "5":
        excluir_usuario()
    elif opcao == "6":
        adicionar_pedido()
    elif opcao == "7":
        listar_por_cidade()
    elif opcao == "8":
        contar_usuarios()
    elif opcao == "0":
        print("\n Encerrando aplicação...")
        break
    else:
        print("\n Opção inválida. Tente novamente.")
