# Banco de Dados e Operações CRUD em Python

Este diretório contém scripts Python que simulam o armazenamento e manipulação dos dados coletados pelo sistema de sensores agrícolas da FarmTech Solutions.

---

## Estrutura dos Arquivos

- `database.py`  
  Define a criação e configuração da conexão com o banco de dados SQLite (simulado).

- `crud.py`  
  Implementa as operações CRUD (Create, Read, Update, Delete) para as tabelas do banco.

- `main.py`  
  Script principal que exemplifica o uso das operações CRUD, simulando a inserção e manipulação de dados dos sensores.

---

## Banco de Dados

O banco de dados simula o armazenamento dos dados dos sensores de:

- Fósforo (P) - representado por valores booleanos
- Potássio (K) - representado por valores booleanos
- pH do solo - valor analógico (float)
- Umidade do solo - valor analógico (float)
- Status da bomba de irrigação (relé) - ligado ou desligado (booleano)

A estrutura das tabelas segue o modelo ER definido na fase 2 do projeto.

---

## Operações CRUD

### 1. Inserção (Create)

Exemplo: inserir uma nova leitura de sensor no banco.

```python
from crud import insert_sensor_data

# Exemplo de dados simulados
data = {
    'fosforo': True,
    'potassio': False,
    'ph': 6.8,
    'umidade': 55.3,
    'bomba_ligada': True
}

insert_sensor_data(data)
