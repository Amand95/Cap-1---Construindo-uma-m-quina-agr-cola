import sqlite3
from datetime import datetime

# Função para criar a tabela
def criar_tabela():
    conn = sqlite3.connect('dados_irrigacao.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            umidade INTEGER,
            temperatura REAL,
            data_hora TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir nova leitura
def inserir_leitura(umidade, temperatura):
    conn = sqlite3.connect('dados_irrigacao.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO leituras (umidade, temperatura, data_hora)
        VALUES (?, ?, ?)
    ''', (umidade, temperatura, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# Função para listar as leituras
def listar_leituras():
    conn = sqlite3.connect('dados_irrigacao.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leituras')
    dados = cursor.fetchall()
    for linha in dados:
        print(linha)
    conn.close()

# Executar para testar
if __name__ == "__main__":
    criar_tabela()
    inserir_leitura(58, 23.1)
    listar_leituras()
