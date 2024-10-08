from pessoa import Pessoa, Aluno, Professor

p1 = Pessoa('Gerúlio', 65)
aluno = Aluno('Kali', 16, '2º Ano')
prof = Professor('Bruno', 35, 'Desenvolvimento de Sistemas')

p1.info()
aluno.estudar()
prof.ensinar()