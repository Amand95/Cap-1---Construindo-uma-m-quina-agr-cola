# 🌱 Sistema de Irrigação Inteligente - FarmTech Solutions

Este projeto simula um sistema de irrigação inteligente voltado para a agricultura de precisão, utilizando sensores conectados ao ESP32. A proposta visa controlar automaticamente uma bomba de irrigação com base na leitura de dados do solo e do ambiente, promovendo uso sustentável da água e aumento da produtividade.

---

## 🎯 Objetivo

Automatizar o processo de irrigação com base em sensores conectados ao ESP32, coletando dados sobre:

- Presença de fósforo e potássio
- pH do solo
- Temperatura e umidade

Além disso, o projeto visa:

- Monitoramento ambiental em plantações (temperatura, umidade, luminosidade)
- Controle automatizado de irrigação
- Registro e análise de leituras em banco de dados
- Visualização em dashboards para apoio à decisão

---

## 📦 Componentes Utilizados

- ESP32 (simulado no [Wokwi](https://wokwi.com))
- Sensor DHT22 (temperatura e umidade)
- LDR (simulando medição de pH)
- Botões (simulando presença de fósforo e potássio)
- Relé (acionamento da bomba)
- LED (indicador de status)

---

## 💧 Lógica de Irrigação Inteligente

A lógica do sistema decide o acionamento da bomba com base nas seguintes condições:

- **Fósforo presente:** botão correspondente pressionado
- **Potássio presente:** botão correspondente pressionado
- **pH adequado:** entre 6,0 e 8,0 (simulado com LDR)
- **Umidade do solo:** menor que 40% (via DHT22)

✅ **Se todas as condições forem satisfeitas**, a bomba é acionada automaticamente.  
❌ Caso contrário, permanece desligada para evitar desperdícios.

---

## 🧠 Diagrama de Arquitetura

O diagrama abaixo representa o fluxo geral de dados entre os sensores, ESP32, lógica de controle, banco de dados e dashboards:

![Arquitetura](docs/arquitetura.png)

---

## 🧰 Tecnologias Utilizadas

- 💾 Oracle SQL Developer Data Modeler (.dmd)
- 🗃️ Modelo Relacional com tabelas e relacionamentos
- 🧮 Modelagem com foco em relacionamentos 1:N e N:N
- 📊 Python para integração com banco de dados e visualização
- 📈 Dashboards com Streamlit
- 🌐 GitHub para versionamento

---

## 🧩 Modelagem do Banco de Dados

O modelo contempla as principais entidades e seus relacionamentos:

| Entidade   | Descrição                                                                 |
|------------|---------------------------------------------------------------------------|
| Sensor     | Representa o dispositivo instalado na plantação                          |
| Leitura    | Registro dos dados captados pelos sensores                               |
| Cultura    | Informações sobre o tipo de plantação (milho, soja, etc.)                |
| Irrigação  | Ações automáticas ou manuais de irrigação                                |
| Ajuste     | Alterações manuais nos parâmetros de irrigação                           |

---

## 🗺️ Diagrama Entidade-Relacionamento (DER)

### 📷 Visualização
![DER - FarmTech](./entrega1/diagrama_der.png)

### 📥 Arquivo .dmd
- [Clique aqui para baixar o arquivo .dmd](./entrega1/modelo_farmtech.dmd)

> Os arquivos estão localizados na pasta `/entrega1`.

---

## 👨‍🏫 Alunos

| Nome                          | RM      |
|-------------------------------|---------|
| Amanda da Silva Barros        | 564759  |
| Bruno Gambarini               | 561517  |
| João Victor Cope Moreira      | 565958  |
| Karina Jesus dos Santos       | 559268  |
| Lucas Fagundes                | 565179  |

🔗 [Repositório no GitHub](https://github.com/Amand95/Cap-1---Construindo-uma-m-quina-agr-cola)

---

## ✅ Conclusão

Este projeto representa uma solução prática e escalável para o controle inteligente da irrigação em plantações. A arquitetura desenvolvida combina sensores, microcontroladores, banco de dados e dashboards para entregar uma ferramenta eficiente, sustentável e de fácil expansão futura para outras culturas ou integrações com APIs meteorológicas.

---

