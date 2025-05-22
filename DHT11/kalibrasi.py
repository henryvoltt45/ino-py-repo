import math
import math

sensor_suhu = 0.2
sensor_kelembapan = 1.5
kalibrasi_data = [1.1, 0.9, 1.3, 1.0, 1.2]

def set_kalibrasi_data(data_baru):
    global kalibrasi_data
    kalibrasi_data = data_baru

def kalibrasi():
    mean = sum(kalibrasi_data) / len(kalibrasi_data)
    simpangan_baku = math.sqrt(sum((x - mean)**2 for x in kalibrasi_data) / (len(kalibrasi_data)-1))
    u_suhu = math.sqrt(sensor_suhu**2 + simpangan_baku**2)
    u_kelembapan = sensor_kelembapan
    return u_suhu, u_kelembapan# Data kalibrasi contoh
kalibrasi_data = [1.1, 0.9, 1.3, 1.0, 1.2]
sensor_suhu = 0.2
sensor_kelembapan = 1.5

def kalibrasi():
    # Contoh: hitung ketidakpastian suhu dan kelembapan
    mean = sum(kalibrasi_data) / len(kalibrasi_data)
    simpangan_baku = math.sqrt(sum((x - mean)**2 for x in kalibrasi_data) / (len(kalibrasi_data)-1))
    u_suhu = math.sqrt(sensor_suhu**2 + simpangan_baku**2)
    u_kelembapan = sensor_kelembapan
    return u_suhu, u_kelembapan

if __name__ == "__main__":
    print(kalibrasi())