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
  
  def to_dict (self):
    return {
        "cpf": self.cpf,
        "nome_completo": self.nome_completo,
        "nome_usuario": self.nome_usuario,
        "data_nasc": self.data_nasc,
        "endereco": self.endereco,
        "email": self.email,
        "senha": self.senha
    }

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
  
  def to_dict (self):
    return {
        "cod_exemplar": self.cod_exemplar,
        "titulo": self.titulo,
        "autor": self.autor,
        "sinopse": self.sinopse,
        "isbn": self.isbn,
        "edicao": self.edicao,
        "cnpj_fornecedor": self.cnpj_fornecedor,
        "valor": self.valor,
        "data_aquisicao": self.data_aquisicao
    }
  
class Genero:
  def __init__(self, cod_genero, nome ):
    self.cod_genero = cod_genero
    self.nome = nome
  
  def __repr__ (self):
    return f"Gênero {self.cod_genero}: {self.nome}"
  
  def to_dict (self):
      return {
          "cod_genero": self.cod_genero,
          "nome": self.nome
      }

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
  
  def to_dict (self):
    return {
        "id": self.id,
        "cpf_cliente": self.cpf_cliente,
        "cod_exemplar": self.cod_exemplar,
        "data_emp": self.data_emp,
        "data_dev": self.data_dev,
        "devolvido": self.devolvido
    }

class Fornecedor:
  def __init__(self, razao_social, cnpj, telefone, email ):
    self.razao_social = razao_social
    self.cnpj = cnpj
    self.telefone = telefone
    self.email = email
    
  def __repr__ (self):
    return f"Nome: {self.razao_social}, CNPJ: {self.cnpj}, Tel: {self.telefone}, Email: {self.email}"
  
  def to_dict (self):
    return {
        "razao_social": self.razao_social,
        "cnpj": self.cnpj,
        "telefone": self.telefone,
        "email": self.email
    }

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
    
  def to_dict (self):
    return {
      "cpf": self.cpf,
      "nome_completo": self.nome_completo,
      "nome_usuario": self.nome_usuario,
      "data_nasc" : self.data_nasc,
      "endereco" : self.endereco,
      "email" : self.email,
      "senha": self.senha
    }
