class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome # _ protegido
        self._idade = idade
    
    def info(self):
        print(f'Nome: {self._nome}. Idade: {self._idade}.')

class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade) #utilizando o construtor da classe mãe
        self._serie = serie #utilizando atributos exclusivos da classe filha

    def estudar(self):
        print(f'O aluno {self.nome} está estudando na série {self._serie}.')
        
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina
    
    def ensinar(self):
        print(f'{self._nnome}, professor(a) da disciplina {self._disciplina}, está ensinando.')        
