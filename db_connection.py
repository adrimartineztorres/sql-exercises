import mysql.connector
from mysql.connector import Error

class DatabaseConnector:
    def __init__(self, host='localhost', user='root', password='', database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print('Conexión exitosa a la base de datos')
        except Error as e:
            print(f'Error al conectar a la base de datos: {e}')

    def execute_query(self, query, params=None):
        if self.connection is None:
            self.connect()
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            if query.strip().lower().startswith('select') or query.strip().lower().startswith('show'):
                result = cursor.fetchall()
                cursor.fetchall()  # Consumir todos los resultados pendientes
                return result
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(f'Error al ejecutar la consulta: {e}')
            return None
        finally:
            try:
                while cursor.nextset():
                    cursor.fetchall()
            except Exception:
                pass
            cursor.close()

    def close(self):
        if self.connection:
            self.connection.close()
            print('Conexión cerrada')
