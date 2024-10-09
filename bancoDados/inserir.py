import sqlite3

#1.estabelecendo conexão com oo banco de dados
conexao = sqlite3.connect('departamento.db')

#2.verificar se a tabela existe ou não
tabela = """  
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""

#3.acessar objeto da biblioteca sqlite3 para manipular o banco
consulta = conexao.cursor() #o objeto cursor() é responsável por manipular dados do banco 

#4.executar o comando de criação da tabela
consulta.execute(tabela)

#5.solicitar dados
nome = input('Informe o nome do funcionário: ')
salario = input('Informe o salário do funcionário: ')
cargo = input('Informe o cargo do funcionario: ')

#6.criando comando SQL para inserir os dados
sql = 'INSERT INTO funcionario VALUES(?,?,?,?)' #as ??? no lugar dos dados evitam que haja algum ataque e alguém pegue esses dados (SQL INJECTION). Isso é uma implementação da biblioteca sqlite3.

#7.organizar os dados que irão substituir a '?' no comando SQL para inserir os dados
campos = (None, nome, salario, cargo) #criando uma tupla que não muda seu valor

#8.executar o comando SQL e substituir ? pelos campos
consulta.execute(sql, campos)

#9.gravar os dados do banco
conexao.commit()

print(consulta.rowcount, 'linha(s) inseridas com sucesso.')

#10.finalizar conexão
conexao.close()