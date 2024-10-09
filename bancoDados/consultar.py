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

#5.criar comando SQL para consultar oos dados
sql = 'SELECT * FROM funcionario'

#6.executar o comando SQL e substituir ? pelos campos
consulta.execute(sql)

#7.exibir dados do banco
resultado = consulta.fetchall() #ftchall irá trazes todos os registros do banco de dados

print(resultado)

print('='*30)
for itens in resultado:
    print(f'Código: {itens[0]}, Nome: {itens[1]}')

#8.finalizar conexão
conexao.close()