from TAI_classes1 import UsuarioAdm, Livro,  Genero, Emprestimo, Fornecedor, UsuarioCliente

from flask import Flask 
from flask import request
from flask import Response 
from flask import jsonify

app = Flask("OpenBook ALPHA")

fornecedores = []
livros = []
generos = []
emprestimos = []
administradores = []
clientes = []


#Rota para listar administradores
@app.route("/adm")
def adm():
    lista = []
    for f in administradores:
        lista.append (f.to_dict())
    return jsonify(lista)


#Rota para adicionar administradores
@app.route("/adm/add", methods=["POST"])
def post_adm():
    cpf=request.json["cpf"]
    nome_completo=request.json["nome_completo"]
    nome_usuario=request.json["nome_usuario"]
    data_nasc=request.json["data_nasc"]
    endereco=request.json["endereco"]
    email=request.json["email"]
    senha=request.json["senha"]

    novo_adm = UsuarioAdm(cpf,nome_completo,nome_usuario,data_nasc,endereco,email,senha)
    administradores.append(novo_adm)
    
    return Response("cadastrado com sucesso!", 201)


#Rota para remover administradores
@app.route("/adm/del", methods=["DELETE"])
def remov_adm():

    cpf=str(request.json["cpf"])

    for i in administradores:
        if str(i.cpf) == cpf:         
            administradores.remove(i)
            return Response("Removido com sucesso!", 200)
       
    return Response("Usuário não encontrado.", 404)


#Rota para listar fornecedores
@app.route("/forn")
def forn():
    lista = []
    for f in fornecedores:
        lista.append (f.to_dict())
    return jsonify(lista)


#Rota para adicionar fornecedores
@app.route("/forn/add", methods=["POST"])
def post_forn():
    razao_social=request.json["razao_social"]
    cnpj=request.json["cnpj"]
    telefone=request.json["telefone"]
    email=request.json["email"]

    novo_forn = Fornecedor(razao_social,cnpj,telefone,email)
    fornecedores.append(novo_forn)
    
    return Response ("cadastrado com sucesso!",201)


#Rota para remover fornecedores
@app.route("/forn/del", methods=["DELETE"])
def remov_forn():

    cnpj=str(request.json["cnpj"])

    for i in fornecedores:
        if str(i.cnpj) == cnpj:         
            fornecedores.remove(i)
            return Response("Removido com sucesso!", 200)
       
    return Response("Fornecedor não encontrado.", 404)


#Rota para listar livros
@app.route("/liv")
def liv():
    lista = []
    for f in livros:
        lista.append (f.to_dict())
    return jsonify(lista)


#Rota para adicionar livros
@app.route("/liv/add", methods=["POST"])
def post_liv():
    cod_exemplar=request.json["cod_exemplar"]
    titulo=request.json["titulo"]
    autor=request.json["autor"]
    sinopse=request.json["sinopse"]
    isbn=request.json["isbn"]
    edicao=request.json["edicao"]
    cnpj_fornecedor=request.json["cnpj_fornecedor"]
    valor=request.json["valor"]
    data_aquisicao=request.json["data_aquisicao"]

    novo_liv = Livro(cod_exemplar,titulo,autor,sinopse,isbn,edicao,cnpj_fornecedor,valor,data_aquisicao)
    livros.append(novo_liv)
    
    return Response ("cadastrado com sucesso!",201)


#Rota para remover livros
@app.route("/liv/del", methods=["DELETE"])
def remov_livro():

    cod_exemplar=str(request.json["cod_exemplar"])

    for i in livros:
        if str(i.cod_exemplar) == cod_exemplar:         
            livros.remove(i)
            return Response("Removido com sucesso!", 200)
       
    return Response("livro não encontrado.", 404)


#Rota para listar clientes
@app.route("/cli")
def cli():
    lista = []
    for f in clientes:
        lista.append (f.to_dict())
    return jsonify(lista)


#Rota para adicionar clientes
@app.route("/cli/add", methods=["POST"])
def post_cli():
    cpf=request.json["cpf"]
    nome_completo=request.json["nome_completo"]
    nome_usuario=request.json["nome_usuario"]
    data_nasc=request.json["data_nasc"]
    endereco=request.json["endereco"]
    email=request.json["email"]
    senha=request.json["senha"]

    novo_cli = UsuarioCliente(cpf,nome_completo,nome_usuario,data_nasc,endereco,email,senha)
    clientes.append(novo_cli)
    
    return Response ("cadastrado com sucesso!",201)


#Rota para remover clientes
@app.route("/cli/del", methods=["DELETE"])
def remov_cli():

    cpf=str(request.json["cpf"])

    for i in clientes:
        if str(i.cpf) == cpf:         
            clientes.remove(i)
            return Response("Removido com sucesso!", 200)
       
    return Response("Usuário não encontrado.", 404)


#Rota para listar emprestimos
@app.route("/emp")
def emp():
    lista = []
    for f in emprestimos:
        lista.append (f.to_dict())
    return jsonify(lista)


#Rota para adicionar emprestimos
@app.route("/emp/add", methods=["POST"])
def post_emp():
    id=request.json["id"]
    cpf_cliente=request.json["cpf_cliente"]
    cod_exemplar=request.json["cod_exemplar"]
    data_emp=request.json["data_emp"]
    data_dev=request.json["data_dev"]
    

    novo_emp = Emprestimo(id,cpf_cliente,cod_exemplar,data_emp, data_dev)
    emprestimos.append(novo_emp)
    
    return Response ("cadastrado com sucesso!",201)


#Rota para remover emprestimos
@app.route("/emp/del", methods=["DELETE"])
def del_emp():

    id=str(request.json["id"])

    for i in emprestimos:
        if str(i.id) == id:         
            emprestimos.remove(i)
            return Response("Removido com sucesso!", 200)
       
    return Response("Emprestimo não encontrado.", 404)

#Rota para devolver emprestimo
@app.route("/emp/dev", methods=["PATCH"])
def dev_emp():

    id = str(request.json["id"])
    for i in emprestimos:
        if str(i.id) == id:
            i.devolver()
            return Response("Livro devolvido com sucesso!", 200)
        
    return Response("Emprestimo não encontrado.", 404)

#Rota para listar generos
@app.route("/gen")
def gen():
    lista = []
    for f in generos:
        lista.append (f.to_dict())
    return jsonify(lista)


#Rota para adicionar generos
@app.route("/gen/add", methods=["POST"])
def post_gen():
    cod_genero=request.json["cod_genero"]
    nome=request.json["nome"]
   
    novo_gen = Genero(cod_genero,nome)
    generos.append(novo_gen)
    
    return Response ("cadastrado com sucesso!",201)


#Rota para remover generos
@app.route("/gen/del", methods=["DELETE"])
def remov_gen():

    cod_genero=str(request.json["cod_genero"])

    for i in generos:
        if str(i.cod_genero) == cod_genero:         
            generos.remove(i)
            return Response("Removido com sucesso!", 200)

    return Response("Genero não encontrado.", 404)

app.run()


# Json para adm:
# {
#    "cpf":1234,
#    "nome_completo":"joao",
#    "nome_usuario": "joazinho",
#    "data_nasc": "01/01/2001",
#    "endereco":"casa",
#    "email":"joao@gmail",
#    "senha":1234
# }

# Json para livro:
# {
#     "cod_exemplar": 1,
#     "titulo": "O Pequeno Príncipe",
#     "autor": "Antoine de Saint-Exupéry",
#     "sinopse": "Um piloto que sofre uma pane...",
#     "isbn": 101012001,
#     "edicao": 2007,
#     "cnpj_fornecedor": 2222222222,
#     "valor": 25,
#     "data_aquisicao": "23/08/2025"
# }


# Json para cliente:
# {
#     "cpf": 4444,
#     "nome_completo":"Fulano",
#     "nome_usuario":"Fulaninho",
#     "data_nasc": "01/01/2001",
#     "endereco":"predio",
#     "email":"fulano@gmail",
#     "senha": 123456
# }

# Json para emprestimo:
# {
#     "id": 1,
#     "cpf_cliente": 4444,
#     "cod_exemplar": 1,
#     "data_emp": "01/01/2026",
#     "data_dev": "10/01/2026",
#     "devolvido": false
# }

# Json para genero:
# {
#     "cod_genero": 123,
#     "nome": "fantasia"
# }

#Json para fornecedor:
#{
#     "razao_social": "exportadora xyz",
#     "cnpj": 12345,
#     "telefone": 4899999,
#     "email": "exportadora@gmail"
#}