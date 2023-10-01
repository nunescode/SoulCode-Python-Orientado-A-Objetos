
## EXERCÍCIO PRÁTICO 2 ##
    ## SOUL CODE ##

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_escolar_soul_on"
)

'''
##  QUESTÃO 1 ##
#   Crie uma base de dados chamada sistema_escolar_soul_on #

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE sistema_escolar_soul_on")
print("Banco criado com sucesso!")
'''

'''
##  QUESTÃO 2 ##
#   Crie uma tabela alunos com os campos id, nome, matricula, turma. #

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), matricula VARCHAR(255), turma VARCHAR(255))")
print("Tabela criada com sucesso!")
'''
'''
#excluindo dado que não era pra ser criado
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE alunos DROP idade")
print("Coluna excluída!")
'''

'''
##  QUESTÃO 3 ##
#   INSERINDO VALORES NA TABELA #

mycursor = mydb.cursor()
sql = "INSERT INTO alunos (nome, matricula, turma) VALUES(%s, %s, %s)"
val = [
    ('José Lima', 'MAT90551', 'BCW22'),
    ('Carlos Augusto', 'MAT90552', 'BCW22'),
    ('Lívia Lima', 'MAT90553', 'BCW22'),
    ('Sandra Gomes', 'MAT90554', 'BCW23'),
    ('João Augusto', 'MAT90555', 'BCW23'),
    ('Breno Lima', 'MAT90556', 'BCW24'),
    ('José Vinícius', 'MAT90557', 'BCW25')
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Valor(es) Adicionado(s)!")
'''

'''
##  QUESTÃO 4 ##

#   Liste todos os registros de sua tabela. #
mycursor = mydb.cursor()
sql = 'SELECT * FROM alunos'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Liste apenas nome e matrícula dos alunos do BCW23. #
mycursor = mydb.cursor()
sql = "SELECT nome, matricula FROM alunos WHERE turma LIKE '%BCW23%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Liste apenas o nome dos alunos que tiverem o sobrenome Lima. #
mycursor = mydb.cursor()
sql = "SELECT nome FROM alunos WHERE nome LIKE '%Lima%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

'''

'''
##  QUESTÃO 5 ##
#   O aluno Carlos Augusto está na turma errada. Matricule o mesmo no BCW25. #

mycursor = mydb.cursor()
sql = "UPDATE alunos SET turma = 'BCW25' WHERE nome LIKE '%Carlos Augusto%'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "Linha(s) Alterada(s)!")
'''

##  QUESTÃO 6 ##
#   O aluno José Vinicius desistiu do curso, ele deve ser excluído do sistema. #

mycursor = mydb.cursor()
sql = "DELETE FROM alunos WHERE nome LIKE '%José Vinícius%'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "Linha(s) excluída(s)!")
