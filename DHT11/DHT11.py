import serial
import tkinter as tk
from threading import Thread
import time

# Ganti 'COM3' sesuai port Arduino kamu
ser = serial.Serial('COM3', 9600)

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
root.title("Pembaca DHT11")
root.geometry("300x150")

suhu_label = tk.Label(root, text="Suhu: -- °C", font=("Helvetica", 16))
suhu_label.pack(pady=10)

kelembapan_label = tk.Label(root, text="Kelembapan: -- %", font=("Helvetica", 16))
kelembapan_label.pack(pady=10)

# Mulai thread pembaca data
t = Thread(target=update_data, daemon=True)
t.start()

root.mainloop()
