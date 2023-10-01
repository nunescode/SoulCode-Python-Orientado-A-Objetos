from abc import ABC, abstractmethod

class letras():
    @abstractmethod
    def mostrarTipo(self):
        print('Isto é uma classe abstrata.')

class A(letras):
    def __init__(self, descricao):
        self.descricao = descricao

    def imprimir(self):
        print("Método diferente.")

letraa = A("Letra A")
letraa.mostrarTipo()
letraa.imprimir()