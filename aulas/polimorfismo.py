from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, mensagem):
        pass

class B(A):
    def fala(self, mensagem):
        print(f'B está falando... {mensagem}')

class C(A):
    def fala(self, mensagem):
        print(f'C está falando... {mensagem}')

b = B()
c = C()
b.fala('de Bicicleta')
c.fala('de Vôlei')