from pymongo import MongoClient
from pprint import pprint

# ==============================
# CONEXÃO COM MONGODB (DOCKER)
# ==============================
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
usuarios = db["usuarios"]

print("=" * 60)
print(" MongoDB em Docker + Python ")
print(" CRUD INTERATIVO - MONGODB")
print("=" * 60)

def inserir_usuario():
    print("\n--- INSERIR USUÁRIO ---")
    nome = input("Nome: ")
    email = input("Email: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    usuario = {
        "nome": nome,
        "email": email,
        "endereco": {
            "cidade": cidade,
            "estado": estado
        }
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


def atualizar_usuario():
    print("\n--- ATUALIZAR USUÁRIO ---")
    email = input("Informe o email do usuário a ser atualizado: ")
    nova_cidade = input("Nova cidade: ")

    resultado = usuarios.update_one(
        {"email": email},
        {"$set": {"endereco.cidade": nova_cidade}}
    )

    if resultado.matched_count == 0:
        print(" Usuário não encontrado.")
    else:
        print("\n Usuário atualizado com sucesso!")
        usuario = usuarios.find_one({"email": email})
        pprint(usuario)


def excluir_usuario():
    print("\n--- EXCLUIR USUÁRIO ---")
    email = input("Informe o email do usuário a ser excluído: ")

    resultado = usuarios.delete_one({"email": email})

    if resultado.deleted_count == 0:
        print(" Usuário não encontrado.")
    else:
        print("\n Usuário excluído com sucesso!")
        print("\nUsuários restantes:")
        for usuario in usuarios.find():
            pprint(usuario)


while True:
    print("\n" + "=" * 60)
    print("MENU")
    print("1 - Inserir usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Excluir usuário")
    print("0 - Sair")
    print("=" * 60)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        inserir_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        atualizar_usuario()
    elif opcao == "4":
        excluir_usuario()
    elif opcao == "0":
        print("\nEncerrando aplicação...")
        break
    else:
        print("\n Opção inválida. Tente novamente.")
