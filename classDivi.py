class Pessoas:
    def __init__(self, nome, idade, pratoFav):
        self.nome = nome
        self.idade = idade
        self.pratoFav = pratoFav
        
    def mostrarComida(self):
        print(f'{self.nome} gosta de comer {self.pratoFav}')