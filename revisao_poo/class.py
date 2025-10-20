'''
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instancias) que podem ter seus proprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados internos
para realizar varias açoes
Por convenção, usamos PascalCase para nomes de classes.
'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade                                     
    
    def falar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
    
    def escutar(self):
        print(f'O {self.nome} está escutando bem!')
        

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def apresentar(self):
        print(f'Olá pessoal! O meu nome é {self.nome} e tenho {self.idade} e minha matricula na faculdade é {self.matricula}. ')
        

pessoa1 = Pessoa("Joao", 20)
pessoa1.falar()

aluno1 = Aluno("Gloria", 32, 1234567)
aluno1.apresentar()

pessoa2 = Pessoa("Maria", 30)

pessoa2.falar()
pessoa1.escutar()

