class Personagem:
    def __init__(self, nome, vida=5):
        self._nome = nome
        self._vida = vida

    def atack(self):
        print(f'{self._nome} está atacando.')


class Jogador(Personagem):
    def __init__(self, nome, raca, vida=5):
        super().__init__(nome, vida)
        self._raca = raca
        self._inventario = []

    def usarHabilidade(self, poder):
        self._poder = poder
        print(f'{self._nome}: {self._poder}')

    def coletarItem(self, item):
        self._inventario.append(item)

        print('Item adicionado.')
        print(self._inventario)


class Monstro(Personagem):
    def __init__(self, nome, tipo, forca, vida=20):
        super().__init__(nome, vida)
        self._tipo = tipo
        self._forca = forca

    def infoMonstro(self):
        print(
            f'Nome do Monstro: {self._nome}\nTipo: {self._tipo}\nVida: {self._vida}\nForça: {self._forca}')

    def invocarAliado(self, nomeAliado, tipoAliado):
        print(f'Foi chamado um aliado.\nNome do aliado: {nomeAliado}\nTipo: {tipoAliado}')

    def defender(self):
        self._vida -= 1
        print(f'{self._nome} se defendeu. Vida atual: {self._vida}')
