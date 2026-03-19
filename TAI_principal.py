from TAI_classes1 import UsuarioAdm, Livro,  Genero, Emprestimo, Fornecedor, UsuarioCliente

from flask import Flask 
from flask import request
from flask import jsonify 

#curl -X POST http://127.0.0.1:5000/adm/add -H "Content-Type: application/json" -d "{\"cpf\":\"11111111111\",\"nome\":\"fulano\",\"nome_usu\":\"fulano67\",\"data_nasc\":\"06071967\",\"ende\":\"casa\",\"email\":\"gmail\",\"senha\":\"1234\"}"
#curl http://127.0.0.1:5000/adm

app = Flask("meu site")

fornecedores = []
livros = []
generos = []
emprestimos = []
administradores = []
clientes = []

@app.route("/adm/add", methods=["POST"])
def post_pessoa():
    cpf=request.json["cpf"]
    nome=request.json["nome"]
    nome_usu=request.json["nome_usu"]
    data_nasc=request.json["data_nasc"]
    ende=request.json["ende"]
    email=request.json["email"]
    senha=request.json["senha"]

    novo_adm = UsuarioAdm(cpf,nome,nome_usu,data_nasc,ende,email,senha)
    administradores.append(novo_adm)
    
    return "cadastrado com sucesso!"

@app.route("/adm")
def adm():
    lista = ""
    for f in administradores:
        lista += f"{f}"
    return f"Esses são os administradores:{lista}"



@app.route("/forn/add", methods=["POST"])
def post_pessoa():
    razao=request.json["razao"]
    cnpj=request.json["cnpj"]
    tele=request.json["tele"]
    email=request.json["email"]

    novo_forn = UsuarioAdm(razao,cnpj,tele,email)
    fornecedores.append(novo_forn)
    
    return "cadastrado com sucesso!"

@app.route("/forn")
def forn():
    lista = ""
    for f in fornecedores:
        lista += f"{f}"
    return f"Esses são os fornecedores:{lista}"

@app.route("/liv/add", methods=["POST"])
def post_pessoa():
    cod=request.json["cod"]
    titulo=request.json["titulo"]
    autor=request.json["autor"]
    sinopse=request.json["sinopse"]
    isbn=request.json["isbn"]
    edicao=request.json["edicao"]
    cnpj=request.json["cnpj"]
    valor=request.json["valo"]
    data=request.json["edicao"]


    novo_liv = Livro(cod,titulo,autor,sinopse,isbn,edicao,cnpj,valor,data)
    livros.append(novo_liv)
    
    return "cadastrado com sucesso!"

@app.route("/liv")
def liv():
    lista = ""
    for f in livros:
        lista += f"{f}"
    return f"Esses são os l:{lista}"

'''
@app.route("/clientes")
def cli():
    return jsonify(clientes)

@app.route("/generos")
def gen():
    return jsonify (generos)

@app.route("/emprestimos")
def emp():
   return jsonify(emprestimos)
'''

# adm1 = UsuarioAdm("123.456.789-00", "João da Silva", "João_Open", "23/04/2000", "Rua Santa Catarina, Garopaba", "joaodasilva@gmail.com", "joao@1234")
# adm2 = UsuarioAdm("123.456.789-01", "José da Silva", "José_Open", "23/04/2000", "Rua Santa Catarina, Garopaba", "josédasilva@gmail.com", "josé@1234")

# administradores.append(adm1)
# administradores.append(adm2)
# adm_junto = adm1,adm2

# while True:
#     print("1.cadastrar \n 0.sair")
#     opc = int(input("escolha a opcao"))
#     if opc ==1:
#         adms=input("digite um nome")
#         administradores.append(adms)
#         adm_junto = adm_junto, adms
#     else:
#         break

# cliente1 = UsuarioCliente("234.456.678-99", "Bea Rosa", "beatriz", "02/05/2008", "Garopaba", "beatriz@ifsc", "beatriz1234")
# clientes.append(cliente1)
# print(clientes)

# livro1 = Livro(1, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Uma história mágica", "978-85-99901-09-0", 1, "11.111.111/0001-11", 25.50, "01/01/2024")
# livros.append(livro1)
# print(livros)


# genero1 = Genero(1, "Fantasia")
# generos.append(genero1)
# print(generos)

# fornecedor1 = Fornecedor ("ltda", "12345678912435", "48 9966-6017", "fornecedor@gmail")
# fornecedores.append (fornecedor1)
# print(fornecedores)

# emprestimo1 = Emprestimo ("01", "111.111.111-11", "67", "25/03/2026","25/04/2026")
# emprestimos.append (emprestimo1)
# print(emprestimos)


app.run()

