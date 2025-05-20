import sqlite3

def create_connection(db_file):
    """
    Cria uma conexão com o banco de dados SQLite especificado por db_file.
    Retorna o objeto conexão.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Conexão com banco de dados SQLite estabelecida.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

def create_tables(conn):
    """
    Cria as tabelas necessárias para armazenar as leituras dos sensores e o estado da bomba.
    """
    try:
        cursor = conn.cursor()

        # Tabela para armazenar as leituras dos sensores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leituras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                umidade REAL NOT NULL,
                ph REAL NOT NULL,
                fosforo BOOLEAN NOT NULL,
                potassio BOOLEAN NOT NULL,
                estado_rele BOOLEAN NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        print("Tabelas criadas com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabelas: {e}")
