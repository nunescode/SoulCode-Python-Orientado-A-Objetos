class Animal():
    def __init__(self, especie, nome, idade):
        self.especie = especie
        self.nome = nome
        self.idade = idade

class Cachorro(Animal):
    def __init__(self, especie, nome, idade, raca, cor):
        super().__init__(especie, nome, idade)
        self.raca = raca
        self.cor = cor

cachorro1 = Cachorro('Mamífero', 'Bill', '9 meses', 'Pinscher', 'Marrom')
cachorro2 = Cachorro('Mamífero', 'Paçoca', '5 meses', 'Labrador', 'Galega')

print(vars(cachorro1))
print(vars(cachorro2))

