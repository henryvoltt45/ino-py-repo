import tkinter as tk 
import time
import serial

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

def led_on():
    arduino.write(b'ON\n')
    print("LED HIDUP")

def led_off():
    arduino.write(b'OFF\n')
    print("LED MATI")

# GUI setup
root = tk.Tk()
root.title("LED Control")

btn_on = tk.Button(root, text="ON", command=led_on, bg="green", fg="white", width=10, height=2)
btn_on.pack(pady=10)

btn_off = tk.Button(root, text="OFF", command=led_off, bg="red", fg="white", width=10, height=2)
btn_off.pack(pady=10)

root.mainloop()