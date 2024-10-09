from personagem import Personagem, Jogador, Monstro

personagem = Personagem('aymar007', 5)
jogador = Jogador('aymar007', 'Humano', 5)
monstro = Monstro('Vorath, o Devastador', 'Orc', 160, 20)

personagem.atack()
jogador.usarHabilidade('Resistência Mental')
jogador.coletarItem('Espada Longa')
monstro.infoMonstro()
monstro.invocarAliado('Nexos, o Criador de Pesadelos', 'Fantasma')
monstro.defender()
jogador.coletarItem('Escudo de Madeira')