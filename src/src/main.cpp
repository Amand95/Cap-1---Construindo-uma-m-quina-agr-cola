#include <Arduino.h>
#include <DHT.h>

// Definições dos pinos
#define PIN_SENSOR_FOSFORO  13  // Botão para fósforo (P)
#define PIN_SENSOR_POTASSIO 12  // Botão para potássio (K)
#define PIN_SENSOR_PH       34  // LDR conectado no ADC1_CH6 (GPIO34)
#define PIN_SENSOR_UMIDADE  27  // DHT22 data pin
#define PIN_RELE            14  // Relé para bomba de irrigação
#define LED_STATUS          2   // LED embutido para status

// Configuração do sensor DHT22
#define DHTTYPE DHT22
DHT dht(PIN_SENSOR_UMIDADE, DHTTYPE);

void setup() {
  Serial.begin(115200);

  pinMode(PIN_SENSOR_FOSFORO, INPUT_PULLUP);
  pinMode(PIN_SENSOR_POTASSIO, INPUT_PULLUP);
  pinMode(PIN_RELE, OUTPUT);
  pinMode(LED_STATUS, OUTPUT);

  dht.begin();

  Serial.println("Sistema de Irrigação FarmTech Solutions iniciado.");
}

void loop() {
  // Leitura dos sensores digitais (botões)
  bool fosforoPresente = digitalRead(PIN_SENSOR_FOSFORO) == LOW;  // botão pressionado = LOW
  bool potassioPresente = digitalRead(PIN_SENSOR_POTASSIO) == LOW;

  // Leitura analógica do pH (LDR)
  int phValorRaw = analogRead(PIN_SENSOR_PH);
  // Converte valor ADC (0-4095) para uma escala aproximada de pH (0-14)
  float phValor = (phValorRaw / 4095.0) * 14.0;

  // Leitura do sensor de umidade DHT22
  float umidade = dht.readHumidity();
  float temperatura = dht.readTemperature();

  if (isnan(umidade) || isnan(temperatura)) {
    Serial.println("Falha na leitura do sensor DHT22");
  }

  // Lógica para ligar ou desligar a bomba
  // Exemplo simples: ligar se umidade abaixo de 40% e fósforo e potássio presentes e pH entre 6 e 8
  bool ligarBomba = false;
  if (umidade < 40.0 && fosforoPresente && potassioPresente && phValor >= 6.0 && phValor <= 8.0) {
    ligarBomba = true;
  }

  digitalWrite(PIN_RELE, ligarBomba ? HIGH : LOW);
  digitalWrite(LED_STATUS, ligarBomba ? HIGH : LOW);

  // Impressão dos dados no monitor serial para captura
  Serial.print("Fósforo: ");
  Serial.print(fosforoPresente ? "Sim" : "Não");
  Serial.print(" | Potássio: ");
  Serial.print(potassioPresente ? "Sim" : "Não");
  Serial.print(" | pH: ");
  Serial.print(phValor, 2);
  Serial.print(" | Umidade: ");
  Serial.print(umidade, 2);
  Serial.print("% | Bomba: ");
  Serial.println(ligarBomba ? "Ligada" : "Desligada");

  delay(3000); // aguarda 3 segundos antes da próxima leitura
}
