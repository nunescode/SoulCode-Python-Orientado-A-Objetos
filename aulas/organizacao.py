import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

''' 
### ORDENAR ###
# sql = "SELECT name FROM customers ORDER BY name"
'''

# ORDEM DESCENDENTE

'''
sql = "SELECT name FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''

'''
### EXCLUSÃO DE DADOS ###
sql = "DELETE FROM customers WHERE address = 'Bahia, BA'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, 'linha(s) deletada(s)!')
'''

'''
### ATUALIZAÇÃO DE DADOS ###
sql = "UPDATE customers SET address = 'Natalândia, MG' WHERE address = 'Cruzeiro, DF'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "linha(s) alterada(s)!")
'''

'''
### EXCLUSÃO DE TABELAS ###
mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)
print("Tabela excluída com sucesso!")
'''
