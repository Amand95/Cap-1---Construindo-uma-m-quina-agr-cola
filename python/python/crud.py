def inserir_sensor(conn, tipo, valor):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sensores (tipo, valor) VALUES (?, ?)", (tipo, valor))
        conn.commit()
        print("Dados inseridos com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

def buscar_sensores(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sensores")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []

def atualizar_sensor(conn, sensor_id, novo_valor):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE sensores SET valor = ? WHERE id = ?", (novo_valor, sensor_id))
        conn.commit()
        print("Dados atualizados com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar dados: {e}")

def deletar_sensor(conn, sensor_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sensores WHERE id = ?", (sensor_id,))
        conn.commit()
        print("Dados deletados com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar dados: {e}")
