const int buzzer = 11;

void setup() {
    pinMode(buzzer, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        char input = Serial.read();
        int freq = 0;
        if (input == 'C') freq = 261;
        else if (input == 'D') freq = 294;
        else if (input == 'E') freq = 329;
        else if (input == 'F') freq = 349;
        else if (input == 'G') freq = 392;
        else if (input == 'A') freq = 440;
        else if (input == 'B') freq = 493;
        else if (input == 'c') freq = 523; // do tinggi

        if (freq > 0) {
            tone(buzzer, freq);
            delay(500);           // Bunyikan selama 200 ms
            noTone(buzzer);       // Matikan buzzer
        } else if (input == 'X') {
            noTone(buzzer);       // Stop nada jika ada perintah X
        }
    }
}

