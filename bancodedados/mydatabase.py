

## INSERINDO DADOS NA TABELA ##


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

# val = ("Pedro", "Brasília, DF")
# mycursor.execute(sql, val)

val = [
    ('Walesca', 'Bahia, BA'),
    ('Letícia', 'Palmas, TO'),
    ('Lara', 'Vitória, ES'),
    ('Raynara', 'Unaí, MG'),
    ('Eloá', 'Brasília, DF'),
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "linha(s) alterada(s)!")
