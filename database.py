#instalar el paquete de conexion de mysql en la terminal
#pip install mysql-connector-python==8.0.29
import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crud-python-1'
)
#ir a app.py e importar este archivo de conexion ---> 5