# 🌾 Entrega 1 – Sistema de Sensores com ESP32

## 📘 Descrição
Este projeto simula um sistema de irrigação inteligente para plantações, utilizando sensores conectados a um microcontrolador ESP32. A lógica do sistema avalia condições de umidade do solo, presença de nutrientes e nível de pH para acionar ou desligar a irrigação automaticamente.

## 🔧 Componentes Simulados
- ESP32
- Sensor de Umidade (DHT22)
- Sensor de pH (LDR simulando entrada analógica)
- Botões representando sensores de:
  - Fósforo (pino 2)
  - Potássio (pino 4)
- LED/Relé (simula bomba de irrigação)

## 🧠 Lógica de Funcionamento
A irrigação será ativada se qualquer uma das seguintes condições for **verdadeira**:
- Umidade do solo < 50%
- Sem presença de fósforo (botão desligado)
- Sem presença de potássio (botão desligado)
- pH < 5.5 ou pH > 7.5

## 📄 Arquivos
- `src/main.cpp`: Código-fonte do ESP32 com lógica comentada
- `platformio.ini`: Arquivo de configuração do PlatformIO
- `circuito_wokwi.png`: Imagem do circuito montado no Wokwi
- `README.md`: Este documento

## ▶️ Simulação no Wokwi
A simulação foi feita no [Wokwi](https://wokwi.com/), ambiente online para simular circuitos com ESP32.  
A imagem abaixo mostra a montagem do circuito:

![Circuito Simulado no Wokwi](circuito_wokwi.png)

## 🖥️ Código (resumo)
```cpp
if (umidade < 50 || !fosforo || !potassio || ph < 5.5 || ph > 7.5) {
  ligarBomba = true;
} else {
  ligarBomba = false;
}
