# 🌱 Capítulo 1 – Construindo uma Máquina Agrícola Inteligente

Este projeto tem como objetivo criar a modelagem de um banco de dados relacional voltado à automação agrícola com foco em sensores de monitoramento e irrigação. Utilizando conceitos de IoT, os dados coletados serão usados para melhorar o processo de tomada de decisão na irrigação de plantações, otimizando recursos como água e nutrientes.

---

## 👩‍💻 Alunos

- **Nome:** Amanda Silva  
- **RM:** 553038
- - **Nome:** Amanda Silva  
- **RM:** 553038
- - **Nome:** Amanda Silva  
- **RM:** 553038
- - **Nome:** Amanda Silva  
- **RM:** 553038
- - **Nome:** Amanda Silva  
- **RM:** 553038
- **Repositório GitHub:** [Cap-1---Construindo-uma-maquina-agricola](https://github.com/Amand95/Cap-1---Construindo-uma-m-quina-agr-cola)

---

## 🎯 Objetivo do Projeto

Desenvolver a modelagem lógica e física de um sistema de banco de dados relacional para apoiar uma solução agrícola inteligente baseada em sensores, com foco em:

- Monitoramento ambiental em plantações (temperatura, umidade, luminosidade)
- Controle de irrigação
- Registro e análise de leituras para tomada de decisão

---

## 🧰 Tecnologias Utilizadas

- 💾 Oracle SQL Developer Data Modeler (.dmd)
- 🗃️ Modelo Relacional com tabelas e relacionamentos
- 🧮 Modelagem com foco em relacionamentos 1:N e N:N
- 🖼️ Diagrama DER (.png)
- 📌 GitHub para versionamento

---

## 🧩 Modelagem do Banco de Dados

O modelo proposto contempla as principais entidades e seus relacionamentos:

| Entidade     | Descrição                                                                 |
|--------------|---------------------------------------------------------------------------|
| Sensor       | Representa o dispositivo físico instalado na plantação                    |
| Leitura      | Registro dos dados captados pelos sensores                                |
| Cultura      | Informações sobre o tipo de plantação (milho, soja, etc.)                 |
| Irrigação    | Ações realizadas automaticamente ou manualmente para irrigação da cultura |
| Ajuste       | Dados que indicam alterações manuais nos parâmetros de irrigação          |

---

## 🗺️ Diagrama Entidade-Relacionamento (DER)

O DER abaixo foi construído com base nas entidades listadas e nos relacionamentos exigidos pela disciplina.

### 📷 Visualização (PNG)
![DER - FarmTech](./entrega1/diagrama_der.png)

### 📦 Arquivo .dmd
- [Clique aqui para baixar o arquivo .dmd](./entrega1/modelo_farmtech.dmd)

> **Observação:** Ambos os arquivos estão disponíveis na pasta `/entrega1` deste repositório.

---

## 📌 Conclusão

Este projeto representa a base de dados que irá apoiar um sistema completo de irrigação inteligente, promovendo sustentabilidade e uso eficiente da água nas lavouras. A estrutura proposta é escalável, podendo ser adaptada para diferentes culturas e integrações com dispositivos IoT em fases futuras.

---


