import sqlite3

def conectar():
    return sqlite3.connect("irrigacao.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            umidade REAL,
            temperatura REAL,
            status_bomba TEXT
        )
    ''')
    conn.commit()
    conn.close()
