from pymongo import MongoClient

# Conexão com o MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Criação (ou acesso) ao banco de dados
db = client["ecommerce"]

# Criação (ou acesso) à coleção
usuarios = db["usuarios"]

print("Conexão com MongoDB realizada com sucesso!")