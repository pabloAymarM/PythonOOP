from produto import Produto, Livro

p1 = Produto('Mesa', 859.99)
l1 = Livro('Memórias Póstumas', 51.56, 'Machado de Assis')

p1.descrever()
l1.descrever()
l1.calcularDescontos(0.1)