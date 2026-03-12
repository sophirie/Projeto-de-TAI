from TAI_classes1 import UsuarioAdm, Livro,  Genero, Emprestimo, Fornecedor, UsuarioCliente

fornecedores = []
livros = []
generos = []
emprestimos = []
administradores = []
clientes = []

adm1 = UsuarioAdm("123.456.789-00", "João da Silva", "João_Open", "23/04/2000", "Rua Santa Catarina, Garopaba", "joaodasilva@gmail.com", "joao@1234")
administradores.append(adm1)
print(administradores)

cliente1 = UsuarioCliente("234.456.678-99", "Bea Rosa", "beatriz", "02/05/2008", "Garopaba", "beatriz@ifsc", "beatriz1234")
clientes.append(cliente1)
print(clientes)

livro1 = Livro(1, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Uma história mágica", "978-85-99901-09-0", 1, "11.111.111/0001-11", 25.50, "01/01/2024")
livros.append(livro1)
print(livros)


genero1 = Genero(1, "Fantasia")
generos.append(genero1)
print(generos)

fornecedor1 = Fornecedor ("ltda", "12345678912435", "48 9966-6017", "fornecedor@gmail")
fornecedores.append (fornecedor1)
print(fornecedores)

emprestimo1 = Emprestimo ("01", "111.111.111-11", "67", "25/03/2026","25/04/2026")
emprestimos.append (emprestimo1)
print(emprestimos)