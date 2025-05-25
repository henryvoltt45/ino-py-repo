#include <Servo.h>
const int LED  = 11;
const int LED1 = 10;
const int BUZZER = 12;
Servo myservo;

void setup() {
  myservo.attach(13);
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(LED1, OUTPUT);
  pinMode(BUZZER, OUTPUT);

}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim(); // Remove any leading or trailing whitespace

    if (input == "KANAN") {
      digitalWrite(LED, LOW);
      myservo.write(90);
      digitalWrite(LED1, HIGH);
      digitalWrite(BUZZER, HIGH);
      delay(100);
      digitalWrite(BUZZER, LOW);
    } else {
      myservo.write(0);
      digitalWrite(LED1, LOW);
      digitalWrite(LED, HIGH);
      digitalWrite(BUZZER, HIGH);
      delay(100);
      digitalWrite(BUZZER, LOW);
    }
  }
}