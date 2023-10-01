"""
Fornece operações básicas matemáticas como adição, subtração, divisão e multiplicação. Também imprime variáveis passadas por argumentos.
"""
def somar(a, b):
    print(a + b)

def subtrair(a, b):
    print(a - b)

def dividir(a, b):
    print(a / b)

def multiplicar(a, b):
    print(a * b)
def imprimir(val):
    print(val)


def contrario(nome):
    nome = input("Digite o seu nome")
    print(f"O seu nome é {nome}")
    invertido = ''.join(palavra[::-1] for palavra in nome.split())
    print(f"O seu nome ao contrário é: {invertido}")
