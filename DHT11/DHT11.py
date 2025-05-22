import serial
import tkinter as tk
from threading import Thread
import time
from kalibrasi import kalibrasi, set_kalibrasi_data


# Variabel COM3
ser = serial.Serial('COM3', 9600)
# Variabel ketidakpastian
u_suhu, u_kelembapan = kalibrasi()  # Pastikan fungsi kalibrasi mengembalikan dua nilai

def update_data():
    while True:
        if ser.in_waiting:
            try:
                line = ser.readline().decode().strip()
                suhu, kelembapan = line.split("|")
                suhu_label.config(text=f"Suhu: {suhu} °C")
                kelembapan_label.config(text=f"Kelembapan: {kelembapan} %")
            except:
                pass
        time.sleep(1)

# Setup GUI
root = tk.Tk()
root.title("Sensor Suhu dan Kelembapan")
root.geometry("300x150")

suhu_label = tk.Label(root, text="Suhu: -- °C", font=("Helvetica", 20))
suhu_label.pack(pady=10)

kelembapan_label = tk.Label(root, text="Kelembapan: -- %", font=("Helvetica", 20))
kelembapan_label.pack(pady=10)

# Tambahkan label ketidakpastian suhu
label_ketidakpastian_suhu = tk.Label(root, text=f"Ketidakpastian suhu: ±{u_suhu:.2f} °C", font=("Roboto", 14))
label_ketidakpastian_suhu.pack(pady=2)

# Tambahkan label ketidakpastian kelembapan
label_ketidakpastian_kelembapan = tk.Label(root, text=f"Ketidakpastian kelembapan: ±{u_kelembapan:.2f} %", font=("Roboto", 14))
label_ketidakpastian_kelembapan.pack(pady=2)

# Mulai thread pembaca data
t = Thread(target=update_data, daemon=True)
t.start()

root.mainloop()