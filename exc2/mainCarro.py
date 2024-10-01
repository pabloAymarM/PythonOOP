from carro import Carro

marca = input('Informe a Marca do Carro: ')
modelo = input('Informe o Modelo da Marca: ')
ano = input('Informe o Ano do Carro: ')
precoDiaria = float(input('Informe o Preço da Diária: '))

carro = Carro(marca, modelo, ano, precoDiaria)
carro.exibirDetalhes()
carro.calcularPreco()