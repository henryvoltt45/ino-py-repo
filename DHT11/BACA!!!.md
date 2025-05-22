# Proyek Monitoring Suhu dan Kelembapan DHT11

Proyek ini membaca data suhu dan kelembapan dari sensor DHT11 yang terhubung lewat Arduino, lalu menampilkannya secara realtime menggunakan GUI Python dengan Tkinter. Selain itu, proyek ini juga menghitung dan menampilkan ketidakpastian pengukuran untuk memberikan gambaran keakuratan data sensor.

## Fitur Utama

- Membaca data suhu (°C) dan kelembapan (%) via serial port (PySerial)
- Menampilkan data realtime di GUI dengan font yang mudah dibaca
- Menghitung ketidakpastian pengukuran berdasarkan simpangan baku data dan toleransi sensor DHT11
- Update data setiap 1 detik untuk respons yang cepat

## Cara Menjalankan

1. Hubungkan Arduino yang sudah diupload kode sensor DHT11 ke komputer
2. Jalankan script Python `main_gui.py`
3. Pastikan COM port sesuai dengan Arduino yang terhubung (bisa diubah di script)
4. Lihat tampilan GUI yang menunjukkan suhu, kelembapan, dan ketidakpastian

## Catatan Penting

- Sensor DHT11 memiliki ketidakpastian bawaan sekitar ±2°C untuk suhu dan ±5% untuk kelembapan
- Ketidakpastian yang dihitung juga mempertimbangkan variasi data hasil pembacaan real-time
- Pastikan kabel dan sensor tidak terkena air langsung untuk menghindari kerusakan
- Pastikan komunikasi terhubung ke USB COM, baik itu dimana aja bisa di ganti kok di program

## Penutup

- Alhamdulillah dan terimakasih kepada tuhan yang maha esa karena telah memberikan kesempatan membuat repo DHT11 ini
- Terimakasih kepada chatgpt dan github co-pilot, yang telah membantu saya
- Dan video video tutorial di youtube yang tak bisa saya sebutkan satu persatu
- Repo DHT11 merupakan hasil proyekan pertama author selama beli arduino

Terima kasih sudah mencoba proyek ini!
