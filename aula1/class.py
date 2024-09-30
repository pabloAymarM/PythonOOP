class Pessoas:
    #atributos - características da classe
    nome = 'Pablo'
    idade = 18
    altura = 1.85
    
    #métodos - comportamentos da classe
    def falar (self, texto): 
        #self é um parâmetro obrigatório do python que                                                                                                                 informa que o método pertence à própria classe que foi criada.
        print(f'Tenho algo pra te falar: {texto}')
    
pessoa1 = Pessoas() #criando um objeto do tipo 'Pessoas'

print(pessoa1.nome)