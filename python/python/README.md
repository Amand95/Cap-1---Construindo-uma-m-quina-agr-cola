# Banco de Dados e Operações CRUD - FarmTech Solutions

Este diretório contém os scripts Python que simulam o armazenamento e manipulação dos dados coletados pelo sistema de sensores agrícolas da FarmTech Solutions.

---

## Estrutura dos Arquivos

- `database.py`  
  Define a criação e configuração da conexão com o banco de dados SQLite (simulado).

- `crud.py`  
  Implementa as operações CRUD (Create, Read, Update, Delete) para as tabelas do banco.

- `main.py`  
  Script principal que exemplifica o uso das operações CRUD, simulando a inserção e manipulação de dados dos sensores.

---

## Modelo de Dados

O banco de dados armazena informações referentes a sensores que monitoram:

- Fósforo (P) — valor booleano (True/False) representando presença ou ausência.
- Potássio (K) — valor booleano.
- pH do solo — valor analógico (float) representando o nível de acidez/alkalinidade.
- Umidade do solo — valor analógico (float) em porcentagem.
- Status da bomba de irrigação — booleano indicando se a bomba está ligada (True) ou desligada (False).

Esses dados simulam o modelo ER criado na fase 2 do projeto.

---

## Operações CRUD

### 1. Inserção (Create)

Insere uma nova leitura dos sensores no banco.

Exemplo de uso:

```python
from crud import insert_sensor_data

data = {
    'fosforo': True,
    'potassio': False,
    'ph': 6.8,
    'umidade': 55.3,
    'bomba_ligada': True
}

insert_sensor_data(data)
print("Dados inseridos com sucesso!")
