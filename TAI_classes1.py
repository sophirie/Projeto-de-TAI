class UsuarioAdm:
  def __init__(self, cpf, nome_completo, nome_usuario, data_nasc, endereco, email, senha):
    self.cpf = cpf
    self.nome_completo = nome_completo
    self.nome_usuario = nome_usuario
    self.data_nasc = data_nasc
    self.endereco = endereco
    self.email = email
    self.senha = senha

  def __repr__ (self):
    return self.nome_usuario

class Livro:
  def __init__(self, cod_exemplar, titulo, autor, sinopse, isbn, edicao, cnpj_fornecedor, valor, data_aquisicao):
    self.cod_exemplar = cod_exemplar
    self.titulo = titulo
    self.autor = autor
    self.sinopse = sinopse
    self.isbn = isbn
    self.edicao = edicao
    self.cnpj_fornecedor = cnpj_fornecedor
    self.valor = valor
    self.data_aquisicao = data_aquisicao

  def __repr__ (self):
     return f"Livro: {self.titulo}, Autor:{self.autor}"
  
class Genero:
  def __init__(self, cod_genero, nome ):
    self.cod_genero = cod_genero
    self.nome = nome
  
  def __repr__ (self):
    return f"Gênero {self.cod_genero}: {self.nome}"

class Emprestimo:
  def __init__(self, id, cpf_cliente, cod_exemplar, data_emp, data_dev):
    self.id = id
    self.cpf_cliente = cpf_cliente
    self.cod_exemplar = cod_exemplar
    self.data_emp = data_emp
    self.data_dev = data_dev
    self.devolvido = False
  

  def devolver(self):
    self.devolvido = True
    
  def __repr__ (self):
    status = "DEVOLVIDO" if self.devolvido else "PENDENTE"
    return f"Empréstimo ID {self.id} (Livro {self.cod_exemplar}) - Devolução {self.data_dev} - Status: {status}"

class Fornecedor:
  def __init__(self, razao_social, cnpj, telefone, email ):
    self.razao_social = razao_social
    self.cnpj = cnpj
    self.telefone = telefone
    self.email = email
    
  def __repr__ (self):
    return f"Nome: {self.razao_social}, CNPJ: {self.cnpj}, Tel: {self.telefone}, Email: {self.email}"

class UsuarioCliente:
  def __init__(self,cpf, nome_completo, nome_usuario, data_nasc, endereco, email, senha):
    self.cpf = cpf
    self.nome_completo = nome_completo
    self.nome_usuario = nome_usuario
    self.data_nasc = data_nasc
    self.endereco = endereco
    self.email = email
    self.senha = senha

  def __repr__ (self):
    return f"Cliente: {self.nome_completo} (Usuário: {self.nome_usuario}, CPF: {self.cpf}, Email: {self.email})"
# FIM DAS CLASSES
