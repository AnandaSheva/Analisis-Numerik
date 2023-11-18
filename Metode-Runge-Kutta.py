#Metode Runge Kutta

def f(x, y):
    return (y - x**2 * y) / 2

def runge_kutta_3(x0, y0, x, h):
    n = int((x - x0) / h)
    for _ in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h, y0 - k1 + 2*k2)
        y0 = y0 + (k1 + 4*k2 + k3) / 6
        x0 = x0 + h
    return y0

def runge_kutta_4(x0, y0, x, h):
    n = int((x - x0) / h)
    for _ in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 = x0 + h
    return y0

# Contoh penggunaan
x0 = 0
y0 = 0
x = 3.0
h = 0.3

print("Hasil dengan metode Runge-Kutta orde 3:", runge_kutta_3(x0, y0, x, h))
print("Hasil dengan metode Runge-Kutta orde 4:", runge_kutta_4(x0, y0, x, h))
