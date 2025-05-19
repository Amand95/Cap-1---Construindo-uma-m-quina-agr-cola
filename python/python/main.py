import sqlite3
import time
import random
import logging

class FarmTechSimulator:
    def __init__(self, db_name='farmtech_data.db', intervalo=5,
                 ph_min=6.0, ph_max=8.0, umidade_limite=40.0):
        """
        Inicializa o simulador com parâmetros configuráveis.
        """
        self.db_name = db_name
        self.intervalo = intervalo
        self.ph_min = ph_min
        self.ph_max = ph_max
        self.umidade_limite = umidade_limite
        
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._criar_tabela()
        
        logging.basicConfig(level=logging.INFO,
                            format='[%(asctime)s] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("Simulador iniciado.")

    def _criar_tabela(self):
        """Cria a tabela leituras no banco, se não existir."""
        self.cursor.execute('''
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
        self.conn.commit()

    def simular_leitura(self):
        """
        Simula uma leitura dos sensores.
        Retorna uma tupla (fosforo, potassio, ph, umidade, bomba_ligada).
        """
        fosforo = random.choice([True, False])
        potassio = random.choice([True, False])
        ph = round(random.uniform(5.5, 8.5), 2)
        umidade = round(random.uniform(20, 60), 2)
        bomba_ligada = (
            fosforo and potassio and
            self.ph_min <= ph <= self.ph_max and
            umidade < self.umidade_limite
        )
        return fosforo, potassio, ph, umidade, bomba_ligada

    def salvar_leitura(self, fosforo, potassio, ph, umidade, bomba_ligada):
        """
        Salva uma leitura no banco de dados.
        """
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
        INSERT INTO leituras (timestamp, fosforo, potassio, ph, umidade, bomba_ligada)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (timestamp, fosforo, potassio, ph, umidade, bomba_ligada))
        self.conn.commit()
        logging.info(f"Dados salvos: P={fosforo}, K={potassio}, pH={ph}, Umidade={umidade}, Bomba={bomba_ligada}")

    def consultar_leituras(self, limite=10):
        """
        Consulta as últimas leituras salvas.
        """
        self.cursor.execute('''
        SELECT * FROM leituras ORDER BY id DESC LIMIT ?
        ''', (limite,))
        return self.cursor.fetchall()

    def run(self):
        """
        Executa o loop principal da simulação.
        """
        try:
            while True:
                dados = self.simular_leitura()
                self.salvar_leitura(*dados)
                time.sleep(self.intervalo)
        except KeyboardInterrupt:
            logging.info("Simulação encerrada pelo usuário.")
        finally:
            self.conn.close()
            logging.info("Conexão com banco de dados fechada.")

if __name__ == '__main__':
    sim = FarmTechSimulator()
    sim.run()

