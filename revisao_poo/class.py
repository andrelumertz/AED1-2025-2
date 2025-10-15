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

pessoa1 = Pessoa("Joao",20)
pessoa1.falar()


pessoa2 = Pessoa("Maria", 30)

pessoa2 = Pessoa("Joao", 20)
pessoa2.falar()

