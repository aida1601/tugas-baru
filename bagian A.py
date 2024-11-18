import numpy as np
import matplotlib.pyplot as plt

# Kecepatan konstan
v = 20  # dalam m/s

# Waktu total dalam detik
total_time = 300  # 5 menit = 300 detik

# List untuk menyimpan waktu dan posisi
time_values = []
position_values = []

# Looping untuk menghitung posisi setiap detik
for t in range(total_time + 1):  # dari 0 hingga 300 detik
    s = v * t  # Menghitung posisi
    time_values.append(t)  # Menyimpan waktu
    position_values.append(s)  # Menyimpan posisi

# Visualisasi
plt.figure(figsize=(10, 5))
plt.plot(time_values, position_values, label='Posisi (s) terhadap Waktu (t)', color='blue')
plt.title('Grafik Posisi Benda terhadap Waktu')
plt.xlabel('Waktu (detik)')
plt.ylabel('Posisi (meter)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.xlim(0, total_time)
plt.ylim(0, max(position_values) + 100)
plt.show()