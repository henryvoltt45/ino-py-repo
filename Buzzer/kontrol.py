import tkinter as tk
import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

def nada_c():
    ser.write(b'C\n')
def nada_d():
    ser.write(b'D\n')
def nada_e():
    ser.write(b'E\n')
def nada_f():
    ser.write(b'F\n')
def nada_g():
    ser.write(b'G\n')
def nada_a():
    ser.write(b'A\n')
def nada_b():
    ser.write(b'B\n')
def nada_c_high():
    ser.write(b'c\n')
def nada_x():
    ser.write(b'X\n')  # misal untuk stop atau diam

# GUI setup
root = tk.Tk()
root.title("Buzzer Control")

# Mapping tombol ke fungsi
tombol_nada = [
    ("C", nada_c),
    ("D", nada_d),
    ("E", nada_e),
    ("F", nada_f),
    ("G", nada_g),
    ("A", nada_a),
    ("B", nada_b),
    ("c", nada_c_high),
    ("X", nada_x)
]

for label, func in tombol_nada:
    btn = tk.Button(root, text=label, width=5, height=2, command=func)
    btn.pack(side=tk.LEFT, padx=5, pady=10)

root.mainloop()
ser.close()