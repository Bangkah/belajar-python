#  Manual Iterasi Newton-Raphson
# Diberikan:
# - Fungsi: f(x) = \cos(x) - x
# - Turunan: f'(x) = -\sin(x) - 1
# - Rumus iterasi:
# x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}- Tebakan awal: x_0 = 1
# - Toleransi: 0.0001
# Iterasi 1:
# x_0 = 1 \\


# f(x_0) = \cos(1) - 1 \approx 0.5403 - 1 = -0.4597 \\


# f'(x_0) = -\sin(1) - 1 \approx -0.8415 - 1 = -1.8415 \\


# x_1 = 1 - \frac{-0.4597}{-1.8415} \approx 1 - 0.2496 = 0.7504
# Iterasi 2:
# x_1 = 0.7504 \\


# f(x_1) = \cos(0.7504) - 0.7504 \approx 0.7317 - 0.7504 = -0.0187 \\


# f'(x_1) = -\sin(0.7504) - 1 \approx -0.6810 - 1 = -1.6810 \\


# x_2 = 0.7504 - \frac{-0.0187}{-1.6810} \approx 0.7504 - 0.0111 = 0.7393
# Iterasi 3:
# x_2 = 0.7393 \\


# f(x_2) = \cos(0.7393) - 0.7393 \approx 0.7391 - 0.7393 = -0.0002 \\


# f'(x_2) = -\sin(0.7393) - 1 \approx -0.6736 - 1 = -1.6736 \\


# x_3 = 0.7393 - \frac{-0.0002}{-1.6736} \approx 0.7393 - 0.0001 = 0.7391
# Setelah 3 iterasi, nilai sudah mendekati konvergen di sekitar 0.7391.

import math

def f(x):
    return math.cos(x) - x

def f_prime(x):
    return -math.sin(x) - 1

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
newton_raphson(1)