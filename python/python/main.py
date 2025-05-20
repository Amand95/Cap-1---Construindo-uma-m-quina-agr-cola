from database import create_connection, create_tables
from crud import inserir_leitura, consultar_leituras, atualizar_leitura, deletar_leitura

def main():
    # Caminho do banco SQLite (arquivo local)
    database = "sensores.db"

    # Cria conexão com o banco
    conn = create_connection(database)

    if conn is not None:
        # Cria as tabelas, caso não existam
        create_tables(conn)

        # Simula inserção de dados recebidos do monitor serial
        inserir_leitura(conn, umidade=45.6, ph=6.8, fosforo=True, potassio=False, estado_rele=True)
        inserir_leitura(conn, umidade=50.2, ph=7.1, fosforo=False, potassio=True, estado_rele=False)

        # Consulta e imprime todas as leituras
        leituras = consultar_leituras(conn)
        print("\nLeituras armazenadas:")
        for leitura in leituras:
            print(leitura)

        # Atualiza um registro específico (exemplo id = 1)
        atualizar_leitura(conn, 1, umidade=47.0, ph=6.9, fosforo=True, potassio=True, estado_rele=False)

        # Deleta um registro (exemplo id = 2)
        deletar_leitura(conn, 2)

        # Consulta novamente após as operações
        leituras_atualizadas = consultar_leituras(conn)
        print("\nLeituras após atualizações:")
        for leitura in leituras_atualizadas:
            print(leitura)

        # Fecha a conexão ao final
        conn.close()
    else:
        print("Erro! Não foi possível criar conexão com o banco de dados.")

if __name__ == "__main__":
    main()


