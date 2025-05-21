#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float suhu = dht.readTemperature();
  float kelembapan = dht.readHumidity();
  if (!isnan(suhu) && !isnan(kelembapan)) {
    // Format kiriman: suhu|kelembapan
    Serial.print(suhu);
    Serial.print("|");
    Serial.println(kelembapan);
  }
  delay(2000);
}

