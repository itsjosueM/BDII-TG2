# CRUD Interativo com MongoDB (NoSQL) + Python

## Visão Geral

Este projeto consiste no desenvolvimento de um **CRUD interativo em Python**, utilizando o **MongoDB (SGBD NoSQL orientado a documentos)** como banco de dados. A aplicação funciona em **modo texto no terminal** e permite a manipulação completa de usuários e seus pedidos.

O projeto foi desenvolvido para fins **acadêmicos**, com o objetivo de demonstrar na prática o uso de bancos NoSQL orientados a documentos, operações CRUD e a integração entre aplicação e banco de dados.

## Objetivos do Projeto

* Compreender o funcionamento de bancos de dados NoSQL orientados a documentos
* Utilizar o MongoDB para persistência de dados
* Implementar operações CRUD completas
* Desenvolver uma aplicação interativa em modo texto
* Realizar consultas, filtros e contagens em documentos

## Tecnologias Utilizadas

* **Python 3.11**
* **MongoDB**
* **PyMongo**
* **MongoDB Compass / mongosh** (para visualização dos dados)

---

## Estrutura dos Dados (Modelo de Documento)

A coleção `usuarios` armazena documentos no seguinte formato:

```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "endereco": {
    "cidade": "Marabá",
    "estado": "PA"
  },
  "pedidos": [
    {
      "descricao": "Compra de notebook",
      "status": "Enviado"
    }
  ]
}
```

Este modelo evidencia características importantes do MongoDB:

* Estrutura flexível (schema-less)
* Documentos com campos aninhados
* Uso de arrays de subdocumentos

## Execução do Projeto 

### Iniciar o MongoDB

O MongoDB deve estar em execução localmente.

### Instalar dependências

```bash
pip install pymongo
```

---

### Executar o CRUD

```bash
python mongodb_crud.py
```

Ao executar, o menu interativo será exibido no terminal.

## Conexão com o Banco de Dados

A aplicação realiza a conexão com o MongoDB local através da seguinte string:

```python
client = MongoClient("mongodb://localhost:27017/")
```

Isso significa que:

* O MongoDB está acessível localmente
* O CRUD roda separado do Banco

## Funcionalidades Implementadas

### Inserir Usuário

* Cadastra novos usuários
* Valida campos obrigatórios
* Impede duplicidade de emails

### Listar Usuários

* Lista todos os documentos da coleção `usuarios`

### Buscar Usuário por Email

* Localiza um usuário específico

### Atualizar Endereço

* Atualiza cidade e estado do usuário

### Excluir Usuário

* Remove o documento do banco de dados

### Adicionar Pedido

* Adiciona pedidos vinculados ao usuário

### Listar Usuários por Cidade

* Filtra usuários por campo aninhado

### Contar Usuários

* Retorna o total de usuários cadastrados

## Menu Interativo

```text
MENU
1 - Inserir usuário
2 - Listar usuários
3 - Buscar usuário por email
4 - Atualizar endereco
5 - Excluir usuário
6 - Adicionar pedido
7 - Listar usuários por cidade
8 - Contar usuários
0 - Sair
```

## Acesso Direto ao MongoDB

### Via MongoDB Compass

* String de conexão: `mongodb://localhost:27017`
* Banco: `ecommerce`
* Coleção: `usuarios`

## Considerações Finais

Este projeto demonstra de forma prática a utilização de um banco de dados NoSQL orientado a documentos, destacando a flexibilidade do MongoDB e a facilidade de integração com aplicações Python.

A aplicação CRUD em modo texto permite compreender claramente o funcionamento das operações básicas de manipulação de dados, atendendo aos objetivos acadêmicos propostos.

## Projeto Acadêmico

Desenvolvido para a disciplina de Banco de Dados, com foco em SGBD NoSQL – MongoDB.
