class Pessoa:
    #criando o método construtor
    def __init__(self, nome, hobby, endereco):
        #criando atributos da classe utilizando o método cosntrutor.                                                                                                        Nesse caso, precisamos passar os dados dos parâmetros como nomes dos atributos.
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco
    
    def exibirDados(self):
        print(f'Olá {self.nome}, seu hobby é {self.hobby} e seu endereço é {self.endereco}.')
        
#criando objetos        
pessoa1 = Pessoa('Geraldo', 'Correr', 'Rua 10, Cohab')
pessoa1.exibirDados() #chamando o método da classe

pessoa2 = Pessoa('Karla', 'Artes Maciais', 'Av 12 Renascenca')
pessoa2.exibirDados()