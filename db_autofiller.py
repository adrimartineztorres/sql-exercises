from db_connection import DatabaseConnector

db = DatabaseConnector(
    host='localhost',
    user='root',
    password='',
    database='juego'
)

db.connect()

# Crear tablas
queries = [
    '''CREATE TABLE IF NOT EXISTS jugadores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        nivel INT NOT NULL
    );''',
    '''CREATE TABLE IF NOT EXISTS partidas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fecha DATE NOT NULL,
        mapa VARCHAR(50) NOT NULL
    );''',
    '''CREATE TABLE IF NOT EXISTS resultados (
        id INT AUTO_INCREMENT PRIMARY KEY,
        jugador_id INT,
        partida_id INT,
        bajas INT,
        muertes INT,
        puntuacion INT,
        FOREIGN KEY (jugador_id) REFERENCES jugadores(id),
        FOREIGN KEY (partida_id) REFERENCES partidas(id)
    );'''
]

for query in queries:
    db.execute_query(query)

# Insertar datos de ejemplo
jugadores = [
    ("Ghost", 45),
    ("Soap", 38),
    ("Price", 50),
    ("Roach", 29)
]
for nombre, nivel in jugadores:
    db.execute_query("INSERT INTO jugadores (nombre, nivel) VALUES (%s, %s);", (nombre, nivel))

partidas = [
    ("2025-05-01", "Terminal"),
    ("2025-05-02", "Rust"),
    ("2025-05-03", "Nuketown")
]
for fecha, mapa in partidas:
    db.execute_query("INSERT INTO partidas (fecha, mapa) VALUES (%s, %s);", (fecha, mapa))

resultados = [
    (1, 1, 20, 5, 2000),
    (2, 1, 15, 7, 1500),
    (3, 2, 25, 10, 2500),
    (4, 2, 10, 12, 900),
    (1, 3, 30, 8, 3000),
    (2, 3, 18, 9, 1700)
]
for jugador_id, partida_id, bajas, muertes, puntuacion in resultados:
    db.execute_query(
        "INSERT INTO resultados (jugador_id, partida_id, bajas, muertes, puntuacion) VALUES (%s, %s, %s, %s, %s);",
        (jugador_id, partida_id, bajas, muertes, puntuacion)
    )

db.close()
print("Base de datos rellenada con datos de ejemplo.")
