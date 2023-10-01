class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def get_salario(self):        
        print("Meu salário é: ", self.salario)

    def get_bonificacao(self):
        return self.salario * 0.15
    
pedro = Funcionario('Pedro', '02433601120', 1000)
pedro.get_salario()
print('A bonificação é: ', pedro.get_bonificacao())