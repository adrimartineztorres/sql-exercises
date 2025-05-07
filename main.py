from db_connection import DatabaseConnector

# Conexión a la base de datos local de Laragon (MariaDB)
db = DatabaseConnector(
    host='localhost',
    user='root',
    password='',
    database='juego'
)

db.connect()

# Ejemplo: mostrar las tablas existentes en la base de datos
resultado = db.execute_query('SHOW TABLES;')
print('Tablas en la base de datos:', resultado)

db.close()
