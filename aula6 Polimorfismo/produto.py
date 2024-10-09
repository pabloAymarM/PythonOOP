class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    def descrever(self):
        print(f'O produto {self._nome} custa R${self._preco}.')
    
    def calcularDescontos(self):
        pass #este método na classe mãe, não terá nenhum conteúdo, mas deverá ser utilizado pela classe filha
    
class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self._autor = autor
    
    def descrever(self):
        print(f'O livro {self._nome} foi escrito por {self._autor}.')
    
    def calcularDescontos(self, desconto):
        precoNovo = self._preco * (1 - desconto)
        
        print(f'O novo preço do livro será R${precoNovo:.2f}.')