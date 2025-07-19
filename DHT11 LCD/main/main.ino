#include <DHT.h>
#include <LiquidCrystal.h>

#define DHTPIN 13     // Ganti sesuai pin data DHT11 kamu
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);
  lcd.clear();
  Serial.begin(9600);
  dht.begin();
}

void loop() {
    float suhu = dht.readTemperature();
    float kelembapan = dht.readHumidity();
    lcd.setCursor(0, 0);
    lcd.print("Suhu: ");
    lcd.print(suhu);
    lcd.print(" C");

    lcd.setCursor(0, 1);
    lcd.print("Kelembapan: ");
    lcd.print(kelembapan);
    lcd.print(" %");
    delay(1000);

}