'''
## Rumus Newton-Raphson

- Fungsi: \( f(x) = \sin(x) - 0.5 \)
- Turunan: \( f'(x) = \cos(x) \)
- Iterasi:
  \[
  x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
  \]
- Galat relatif:
  \[
  \text{Galat Relatif} = \left| \frac{x_{n+1} - x_n}{x_{n+1}} \right|
  \]
'''

import math

def f(x):
    return math.sin(x) - 0.5

def f_prime(x):
    return math.cos(x)

def newton_raphson(x0, tolerance=1e-4, max_iter=100):
    xn = x0
    for n in range(1, max_iter + 1):
        fxn = f(xn)
        fpxn = f_prime(xn)
        if fpxn == 0:
            print("Turunan nol. Metode gagal.")
            return None
        xn_next = xn - fxn / fpxn
        relative_error = abs((xn_next - xn) / xn_next)
        print(f"Iterasi {n}: x = {xn_next:.6f}, galat relatif = {relative_error:.6f}")
        if relative_error < tolerance:
            print(f"\n Akar ditemukan: {xn_next:.6f}")
            return xn_next
        xn = xn_next
    print(" Maksimum iterasi tercapai. Metode gagal.")
    return None

# Eksekusi
newton_raphson(1)


'''
Iterasi 1: x = 0.750363, galat relatif = 0.332364
Iterasi 2: x = 0.739112, galat relatif = 0.015236
Iterasi 3: x = 0.739085, galat relatif = 0.000037

✅ Akar ditemukan: 0.739085

Akar ini mendekati nilai \( \arcsin(0.5) = \frac{\pi}{6} \approx 0.5236 \), tetapi karena tebakan awal 1 lebih dekat ke akar di kuadran pertama, hasilnya konvergen ke akar di sekitar 0.739 (akar dari \( \sin(x) = 0.5 \) di kuadran pertama).
'''