# Kelompok 1 B_UAS.ipynb

import matplotlib.pyplot as plt
import numpy as np

# Mendefinisikan fungsi dy/dx
def dy_dx(x, y):
    return x + y

# Metode deret Taylor orde pertama
def taylor_order_1(x, y, delta_x):
    return y + dy_dx(x, y) * delta_x

# Inisialisasi nilai awal
x_0 = 0
y_0 = 1
delta_x = 0.2

#Hitung nilai y(0.2) dengan deret Taylor orde pertama
result = taylor_order_1(x_0, y_0, delta_x)

#Menampilkan hasil y(0.2)
print(f"Hasil aproksimasi y(0.2) dengan metode deret Taylor orde ke-1: {result}")

# Inisialisasi array untuk menyimpan hasil
x_values = [x_0]
y_values = [y_0]

# Iterasi menggunakan metode deret Taylor
while x_values[-1] < 0.2:
    x_new = x_values[-1] + delta_x
    y_new = taylor_order_1(x_values[-1], y_values[-1], delta_x)

    x_values.append(x_new)
    y_values.append(y_new)

# Plot grafik dengan marker titik koordinat
plt.plot(x_values, y_values, marker='o', linestyle='-', label='Metode Deret Taylor Orde Pertama')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik Hasil Aproksimasi dengan Deret Taylor')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

#Persamaan solusi pertumbuhan populasi tikus
def laju_pertumbuhan (t, C):
  return C * np.exp(0.10 * t)

#Parameter
C = 100

#Waktu (bulan)
t_values = np.arange (0, 13, 1)

#Menghitung laju dari pertumbuhan tikus perbulannya
population_values = laju_pertumbuhan(t_values, C)

#Plot grafik dari pertumbuhan populasi
plt.plot(t_values, population_values, marker= 'o')
plt.title('Pertumbuhan Populasi Tikus')
plt.xlabel('Bulan')
plt.ylabel('Populasi Tikus')
plt.grid(True)
plt.show()
