
# CONSULTAS COM WHERE E LIKE 

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM customers WHERE address = 'Brasília, DF'"
sql = "SELECT * FROM customers WHERE address LIKE '%MG%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
