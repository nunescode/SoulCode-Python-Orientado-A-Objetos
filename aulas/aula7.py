class Veiculo():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada

veiculo = Veiculo('carro', 'ASDUINJ2B39X', 'Chevrolet', 'Caravan 95', '1995')
print(vars(veiculo))

motocicleta = Motocicleta('motocicleta', 'S8D87ASXNJDE-987', 'Honda', 'XJ6', '2016', 470)
print(vars(motocicleta))