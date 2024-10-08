class Conta:
    def __init__(self, numConta, titular, saldo, limite=200):
        self.__numConta = numConta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def exibirDetalhes(self):
        print(f'Olá {self.__titular}, seu saldo atual é R${self.__saldo}.')
    
    #o método irá retornar o valor do limite
    def getLimite(self):
        return self.__limite
    
    #método que irá alterar o valor do limite
    # 0 '__' deita o atributo privado, evitando que pessoas acessem fora da pasta
    def setLimite(self, valor):
        if valor < 0:
            print('Informe um valor positivo para o limite.')
        else:
            self.__limite = valor        
            
    def depositar(self, valor):
        if valor < 0:
            print('Informe um valor positivo.')
        else:
            self.__saldo += valor
    
    def saque(self, valor):
        if self.__saldo <= 0 or valor >= self.__saldo:
            print('Saldo Insuficiente.')
        else:
            self.__saldo -= valor