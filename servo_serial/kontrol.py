import time
import serial
import tkinter as tk

arduino = serial.Serial('COM3', 9600)
time.sleep(2)  

def servo_kiri():
    arduino.write(b'KIRI\n')
    # print("Servo Kiri Aktif")

def servo_kanan():
    arduino.write(b'KANAN\n')
    # print("Servo Kanan Aktif")

# GUI
root = tk.Tk()
root.title("Kontrol Servo")

btn_on = tk.Button(root, text="BUKA", command=servo_kiri, bg="green", fg="white", width=10, height=2)
btn_on.pack(pady=10)

btn_on = tk.Button(root, text="TUTUP", command=servo_kanan, bg="red", fg="white", width=10, height=2)
btn_on.pack(pady=10)

root.mainloop()