from bank import Conta

conta = Conta(12, 'Pablo', 4000)
conta.exibirDetalhes()

# alterando o valor do limite
conta.setLimite(3000)
print(f'O limite atual é {conta.getLimite()}')

conta.depositar(500)
conta.saque(100)

conta.exibirDetalhes()
