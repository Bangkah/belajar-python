'''

## ✍️ Langkah-langkah Manual

### 1. Fungsi dan Turunan
- \( f(x) = e^x + x^2 - 3 \)
- \( f'(x) = e^x + 2x \)

### 2. Rumus Iterasi
\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

### 3. Tebakan Awal
- \( x_0 = 0 \)

### Iterasi 1:
\[
f(0) = e^0 + 0^2 - 3 = 1 - 3 = -2 \\
f'(0) = e^0 + 2 \cdot 0 = 1 \\
x_1 = 0 - \frac{-2}{1} = 2
\]

### Iterasi 2:
\[
f(2) = e^2 + 4 - 3 \approx 7.389 + 1 = 8.389 \\
f'(2) = e^2 + 4 \approx 7.389 + 4 = 11.389 \\
x_2 = 2 - \frac{8.389}{11.389} \approx 2 - 0.7365 = 1.2635
\]

### Iterasi 3:
\[
f(1.2635) \approx e^{1.2635} + (1.2635)^2 - 3 \approx 3.536 + 1.596 - 3 = 2.132 \\
f'(1.2635) \approx e^{1.2635} + 2 \cdot 1.2635 \approx 3.536 + 2.527 = 6.063 \\
x_3 = 1.2635 - \frac{2.132}{6.063} \approx 1.2635 - 0.3516 = 0.9119
\]
'''
import math

def f(x):
    return math.exp(x) + x**2 - 3

def f_prime(x):
    return math.exp(x) + 2*x

def newton_raphson(x0, tolerance=1e-4, max_iter=100):
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        fpxn = f_prime(xn)
        if fpxn == 0:
            print("Turunan nol. Metode gagal.")
            return None
        xn_next = xn - fxn / fpxn
        print(f"Iterasi {n+1}: x = {xn_next:.6f}")
        if abs(xn_next - xn) < tolerance:
            print(f"Akar ditemukan: {xn_next:.6f}")
            return xn_next
        xn = xn_next
    print("Maksimum iterasi tercapai. Metode gagal.")
    return None

# Eksekusi
newton_raphson(0)
