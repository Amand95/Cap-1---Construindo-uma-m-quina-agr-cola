from database import criar_conexao, criar_tabelas
from crud import inserir_sensor, buscar_sensores, atualizar_sensor, deletar_sensor

def main():
    conn = criar_conexao()
    if conn is not None:
        criar_tabelas(conn)

        # Inserir dados
        inserir_sensor(conn, 'Umidade', 45.2)
        inserir_sensor(conn, 'pH', 6.8)
        
        # Buscar e mostrar dados
        sensores = buscar_sensores(conn)
        print("Sensores no banco:")
        for s in sensores:
            print(s)
        
        # Atualizar um dado
        if sensores:
            atualizar_sensor(conn, sensores[0][0], 50.0)
        
        # Deletar um dado
        if sensores:
            deletar_sensor(conn, sensores[0][0])
        
        # Mostrar dados atualizados
        sensores = buscar_sensores(conn)
        print("Sensores após alterações:")
        for s in sensores:
            print(s)
        
        conn.close()

if __name__ == '__main__':
    main()

