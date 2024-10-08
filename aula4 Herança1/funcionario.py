class Pessoa:
    def __init__(self, nome, cargo):
        self.__nome = nome
        self.__cargo = cargo
        
    def informacoes(self):
        print(f'Olá {self.__nome}, na empresa, seu cargo é {self.__cargo}.')

#criando classe filha
class Engenheiro(Pessoa):
    def exibirDados(self):
        print(f'Olá, eu sou {self.__nome} e sou um engenheiro.')
        
class Secretario(Pessoa):
    def relatorio(self):
        print(f'Olá, meu cargo é {self.__cargo}.')