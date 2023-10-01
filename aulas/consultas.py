import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Exibir todos os valores da tabela
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Retornar apenas um valor da tabela
myresult = mycursor.fetchone()
print(myresult)