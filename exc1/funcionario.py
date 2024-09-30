class Funcionarios:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def exibirDados(self):
        print(f'{self.nome} tem o cargo: {self.cargo} e ganha R${self.salario}')
        
    def verificaSalario(self):
        if self.salario <= 2000:
            print('Direito a bônus.')
        else:
            print('Sem direito a bônus.')
            