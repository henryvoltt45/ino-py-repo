const int lampu = 13;

void setup() {
  pinMode(lampu, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String perintah = Serial.readStringUntil('\n');
    perintah.trim(); // hapus spasi/enter

    if (perintah == "ON") {
      digitalWrite(lampu, HIGH);
    } else if (perintah == "OFF") {
      digitalWrite(lampu, LOW);
    }
  }
}
