import sqlite3

def conectar_banco(nome_banco='farmtech.db'):
    """Estabelece conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect(nome_banco)
    return conexao

def criar_tabelas():
    """Cria as tabelas necessárias no banco de dados."""
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Exemplo de tabela para sensores (ajuste conforme seu projeto real)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            localizacao TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id INTEGER,
            data_hora TEXT NOT NULL,
            valor REAL,
            FOREIGN KEY(sensor_id) REFERENCES sensores(id)
        )
    ''')

    conexao.commit()
    conexao.close()

if __name__ == '__main__':
    criar_tabelas()
    print("Tabelas criadas com sucesso!")
