def contrario(nome):
    print(f"O seu nome é: {nome}")
    invertido = ''.join(palavra[::-1] for palavra in nome.split())
    print(f"O seu nome ao contrário é: {invertido}")