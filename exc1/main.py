from funcionario import Funcionarios

for cont in range(1, 3):
    nome = input(f'({cont})Informe o seu nome: ')
    cargo = input(f'({cont})Informe o seu cargo: ')
    salario = float(input(f'({cont})Informe o seu salário: R$'))
    f = Funcionarios(nome, cargo, salario)
    f.exibirDados()
    f.verificaSalario()