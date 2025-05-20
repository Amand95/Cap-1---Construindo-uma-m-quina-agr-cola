import sqlite3

def criar_conexao(db_file='farmtech.db'):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Conexão ao banco de dados SQLite estabelecida.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

def criar_tabelas(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        conn.commit()
        print("Tabelas criadas com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabelas: {e}")
