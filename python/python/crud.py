def inserir_leitura(conn, umidade, ph, fosforo, potassio, estado_rele):
    """
    Insere uma nova leitura na tabela leituras.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO leituras (umidade, ph, fosforo, potassio, estado_rele)
            VALUES (?, ?, ?, ?, ?)
        ''', (umidade, ph, fosforo, potassio, estado_rele))
        conn.commit()
        print("Leitura inserida com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir leitura: {e}")

def consultar_leituras(conn):
    """
    Retorna todas as leituras armazenadas no banco.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leituras")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"Erro ao consultar leituras: {e}")
        return []

def atualizar_leitura(conn, id, umidade, ph, fosforo, potassio, estado_rele):
    """
    Atualiza uma leitura existente pelo seu id.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE leituras
            SET umidade = ?, ph = ?, fosforo = ?, potassio = ?, estado_rele = ?
            WHERE id = ?
        ''', (umidade, ph, fosforo, potassio, estado_rele, id))
        conn.commit()
        print(f"Leitura de id {id} atualizada com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar leitura: {e}")

def deletar_leitura(conn, id):
    """
    Remove uma leitura pelo seu id.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM leituras WHERE id = ?', (id,))
        conn.commit()
        print(f"Leitura de id {id} deletada com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar leitura: {e}")
