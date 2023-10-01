class Veiculo():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Aviao():
    def __init__(self, tipo_veiculo, motor, linha_aerea, modelo, ano):
        self.tipo = tipo_veiculo
        self.motor = motor
        self.linha_aerea = linha_aerea
        self.modelo = modelo
        self.ano = ano

carro = Veiculo('carro', '8ASDALEMENACO80', 'KFlyers', 'JK-0001', '2023')
print(vars(carro))
objeto_aviao = Aviao('Carga', 'Quadrimotor', 'SoulCode Airlines', 'NunesBus H365', '2012')
print(vars(objeto_aviao))

