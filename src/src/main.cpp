#include <Arduino.h>
#include <DHT.h>

// Definições dos pinos
#define PIN_SENSOR_FOSFORO  13  // Botão para fósforo (P)
#define PIN_SENSOR_POTASSIO 12  // Botão para potássio (K)
#define PIN_SENSOR_PH       34  // LDR conectado no ADC1_CH6 (GPIO34)
#define PIN_SENSOR_UMIDADE  27  // DHT22 data pin
#define PIN_RELE            14  // Relé para bomba de irrigação (ativo em LOW)
#define LED_STATUS          2   // LED embutido para status

// Configuração do sensor DHT22
#define DHTTYPE DHT22
DHT dht(PIN_SENSOR_UMIDADE, DHTTYPE);

// Variáveis para debounce dos botões
unsigned long lastDebounceTimeFosforo = 0;
unsigned long lastDebounceTimePotassio = 0;
const unsigned long debounceDelay = 50;  // 50 ms debounce

bool lastButtonStateFosforo = HIGH;
bool lastButtonStatePotassio = HIGH;

bool fosforoPresente = false;
bool potassioPresente = false;

void setup() {
  Serial.begin(115200);

  pinMode(PIN_SENSOR_FOSFORO, INPUT_PULLUP);
  pinMode(PIN_SENSOR_POTASSIO, INPUT_PULLUP);
  pinMode(PIN_RELE, OUTPUT);
  pinMode(LED_STATUS, OUTPUT);

  dht.begin();

  // Inicializa o relé desligado (nível HIGH)
  digitalWrite(PIN_RELE, HIGH);
  digitalWrite(LED_STATUS, LOW);

  Serial.println("Sistema de Irrigação FarmTech Solutions iniciado.");
}

bool debounceButton(int pin, bool &lastButtonState, unsigned long &lastDebounceTime) {
  bool reading = digitalRead(pin);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // Se o estado mudou após o debounce
    if (reading != lastButtonState) {
      lastButtonState = reading;
    }
  }
  return (lastButtonState == LOW);  // Botão pressionado (LOW)
}

float lerPH() {
  int phValorRaw = analogRead(PIN_SENSOR_PH);
  float phValor = (phValorRaw / 4095.0) * 14.0;
  return phValor;
}

bool lerSensores(bool &fosforo, bool &potassio, float &ph, float &umidade, float &temperatura) {
  fosforo = debounceButton(PIN_SENSOR_FOSFORO, lastButtonStateFosforo, lastDebounceTimeFosforo);
  potassio = debounceButton(PIN_SENSOR_POTASSIO, lastButtonStatePotassio, lastDebounceTimePotassio);
  ph = lerPH();

  umidade = dht.readHumidity();
  temperatura = dht.readTemperature();

  if (isnan(umidade) || isnan(temperatura)) {
    Serial.println("Falha na leitura do sensor DHT22");
    return false;
  }
  return true;
}

void controlarBomba(bool ligar) {
  // Relé ativo em LOW
  digitalWrite(PIN_RELE, ligar ? LOW : HIGH);
  digitalWrite(LED_STATUS, ligar ? HIGH : LOW);
}

void imprimirStatus(bool fosforo, bool potassio, float ph, float umidade, bool bomba) {
  Serial.print("Fósforo: ");
  Serial.print(fosforo ? "Sim" : "Não");
  Serial.print(" | Potássio: ");
  Serial.print(potassio ? "Sim" : "Não");
  Serial.print(" | pH: ");
  Serial.print(ph, 2);
  Serial.print(" | Umidade: ");
  Serial.print(umidade, 2);
  Serial.print("% | Bomba: ");
  Serial.println(bomba ? "Ligada" : "Desligada");
}

void loop() {
  bool fosforo, potassio;
  float ph, umidade, temperatura;

  if (!lerSensores(fosforo, potassio, ph, umidade, temperatura)) {
    delay(3000);  // Tenta ler novamente após 3 segundos
    return;
  }

  bool ligarBomba = (umidade < 40.0) && fosforo && potassio && (ph >= 6.0) && (ph <= 8.0);

  controlarBomba(ligarBomba);

  imprimirStatus(fosforo, potassio, ph, umidade, ligarBomba);

  delay(3000);
}
