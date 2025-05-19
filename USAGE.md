# USAGE - Sistema de Irrigação Inteligente FarmTech Solutions

Este documento explica como utilizar o sistema de sensores simulados com ESP32 no Wokwi, bem como o script Python para armazenamento e manipulação dos dados em banco SQL.

---

## 1. Simulação do Circuito no Wokwi

### Passos para executar a simulação:

1. Acesse o projeto no [Wokwi](https://wokwi.com/) (link do seu projeto Wokwi).
2. Abra o arquivo do código-fonte em C/C++ (`src/main.cpp`).
3. Inicie a simulação clicando em **Start Simulation**.
4. Observe os dados do monitor serial, que mostrarão os valores dos sensores e o status do relé (bomba de irrigação).
5. Utilize os botões para simular a presença/ausência de fósforo (P) e potássio (K).
6. Observe as leituras do sensor de umidade (DHT22) e do sensor de pH (LDR).
7. O LED indicador mostrará quando a bomba estiver ligada.

---

## 2. Coleta de Dados e Armazenamento

### Passos para usar o script Python:

1. Copie os dados exibidos no monitor serial da simulação.
2. Salve esses dados em um arquivo texto ou cole diretamente no script Python.
3. Execute o script Python (`python src/python/database_script.py`) para inserir os dados no banco SQL.
4. O script realiza operações CRUD básicas:
   - Inserção de novos dados.
   - Consulta dos dados armazenados.
   - Atualização de registros.
   - Remoção de registros, se necessário.

---

## 3. Pré-requisitos

- Python 3.x instalado.
- Bibliotecas necessárias instaladas (exemplo: `sqlite3` já incluída no Python padrão).
- Acesso ao Wokwi para simulação do hardware.

---

## 4. Personalização

- O código do ESP32 pode ser modificado para ajustar a lógica de controle da bomba.
- O script Python pode ser adaptado para trabalhar com bancos de dados reais, caso desejado.
- O circuito pode ser expandido para incluir mais sensores conforme necessidade.

---

## 5. Contato

Para dúvidas ou sugestões, entre em contato com o time FarmTech Solutions.

---

Obrigado por usar nosso sistema de irrigação inteligente!

