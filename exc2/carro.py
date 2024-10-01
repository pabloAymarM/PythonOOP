class Carro:
    def __init__(self, marca, modelo, ano, precoDiaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precoDiaria = precoDiaria
        
    def exibirDetalhes(self):
        print(f'O carro da marca {self.marca}, no modelo {self.modelo}, do ano {self.ano} tem o preço da sua diária em R${self.precoDiaria:.2f}')
    
    def calcularPreco(self):
        diaAluguel = int(input('Informe quantos dias você quer ficar com o carro: '))
        soma = self.precoDiaria * diaAluguel
        
        print(f'O preço do aluguel é de R${soma}.')