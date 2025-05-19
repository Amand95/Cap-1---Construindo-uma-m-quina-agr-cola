import sqlite3
import time
import random

# Cria ou conecta ao banco de dados SQLite
conn = sqlite3.connect('farmtech_data.db')
cursor = conn.cursor()

# Cria a tabela para armazenar as leituras, se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    fosforo BOOLEAN,
    potassio BOOLEAN,
    ph REAL,
    umidade REAL,
    bomba_ligada BOOLEAN
)
''')
conn.commit()

def simular_leitura():
    # Simula os valores que viriam do ESP32
    fosforo = random.choice([True, False])
    potassio = random.choice([True, False])
    ph = round(random.uniform(5.5, 8.5), 2)
    umidade = round(random.uniform(20, 60), 2)
    bomba_ligada = umidade < 40 and fosforo and potassio and 6 <= ph <= 8
    return fosforo, potassio, ph, umidade, bomba_ligada

def salvar_leitura(fosforo, potassio, ph, umidade, bomba_ligada):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
    INSERT INTO leituras (timestamp, fosforo, potassio, ph, umidade, bomba_ligada)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, fosforo, potassio, ph, umidade, bomba_ligada))
    conn.commit()
    print(f"[{timestamp}] Dados salvos: P={fosforo}, K={potassio}, pH={ph}, Umidade={umidade}, Bomba={bomba_ligada}")

if __name__ == '__main__':
    print("Simulação de leituras FarmTech Solutions iniciada.")
    try:
        while True:
            fosforo, potassio, ph, umidade, bomba_ligada = simular_leitura()
            salvar_leitura(fosforo, potassio, ph, umidade, bomba_ligada)
            time.sleep(5)  # espera 5 segundos entre leituras
    except KeyboardInterrupt:
        print("Simulação encerrada.")
        conn.close() 
