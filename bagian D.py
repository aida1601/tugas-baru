import numpy as np
import matplotlib.pyplot as plt

# Parameter gerak
v0 = 60  # kecepatan awal dalam m/s
a = -2.25  # perlambatan dalam m/s^2
total_time = 20  # total waktu dalam detik

# List untuk menyimpan waktu dan posisi
time_values = []
position_values = []

# Looping untuk menghitung posisi setiap detik
for t in range(total_time + 1):  # dari 0 hingga 20 detik
    s = v0 * t + 0.5 * a * t**2  # Menghitung posisi
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
plt.ylim(min(position_values) - 10, max(position_values) + 10)
plt.show()