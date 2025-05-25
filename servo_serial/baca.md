Terima kasih udah mampir ke proyek ini 🙏
Proyek ini sederhana, tapi punya potensi buat jadi awal dari alat monitoring yang lebih kompleks — misalnya kayak monitoring tempat sampah, sistem tombol otomatis, atau kontrol jarak jauh lainnya.

🧰 Bahan-Bahan yang Dipakai
2 buah LED (sebagai indikator)
1 buzzer
1 servo motor (bisa SG90)
Arduino (Uno/Nano)
Kabel jumper secukupnya
Breadboard
Python + PySerial (buat komunikasi serial)

🔌 Rangkaian & Pin
LED 1 → pin 10
LED 2 → pin 11
Buzzer → pin 12
Servo → pin 13
Semua dikontrol lewat serial dari Python. Ketika Python kirim perintah, Arduino akan nyalakan/matikan LED, buzzer, dan gerakkan servo sesuai instruksi.

🎯 Tujuan Proyek
Proyek ini dibuat untuk latihan dasar komunikasi antara Python dan Arduino. Tapi lebih dari itu, aku pengen suatu saat bisa dikembangkan jadi:
Sistem monitoring tempat sampah
Misalnya, servo buka otomatis kalau ada sampah, dan LED/buzzer sebagai notifikasi penuh.
Tombol multifungsi
Misalnya buat alarm, notifikasi tugas, atau alat bantu lainnya.
Kontrol jarak jauh
Bisa pakai GUI atau web, terus nyambungin ke alat fisik yang beneran responsif.

🙌 Penutup
Makasih udah baca sampai sini
