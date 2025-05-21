#include <Servo.h>

const int merahPin = 13;
const int biruPin = 12;
Servo myservo;

void setup() {
  pinMode(merahPin, OUTPUT);
  pinMode(biruPin, OUTPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);    // mulai komunikasi serial
  myservo.attach(9);     // sambungkan servo ke pin 9
}

void loop() {
  myservo.write(0);
  digitalWrite(merahPin, HIGH);
  Serial.println("Servo nutup");
  delay(3000);
  digitalWrite(merahPin, LOW);

  myservo.write(90);
  digitalWrite(biruPin, HIGH);
  digitalWrite(8, HIGH);
  delay(100);
  digitalWrite(8, LOW);
  Serial.println("servo buka");
  delay(3000);
  digitalWrite(biruPin, LOW);

}
