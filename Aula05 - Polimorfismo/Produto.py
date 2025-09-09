#construir a casse Produto, que possui o atributo nome.
#Criar uma instancia de Produto e printar esta instancia
class Produto:
    def __init__(self, nome):
        self.nome= nome  #atributo da classe

    def imprimir(self):
        print(f'O produto é o {self.nome}')
    
    
p1 = Produto("Notebook") 

p1.imprimir()


