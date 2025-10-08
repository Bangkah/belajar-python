import numpy as np

# Fungsi f(x)
def f(x):
    return 2*x**2 + 3*x - 4

# Input batas awal dan akhir
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))

# Pastikan f(a) dan f(b) berlawanan tanda
if f(a) * f(b) > 0:
    print(" f(a) dan f(b) memiliki tanda yang sama. Ganti interval.")
    exit()

# Iterasi metode biseksi
tol = 1e-6  # toleransi error
max_iter = 50
print("\nIterasi\t\ta\t\tb\t\tx\t\tf(x)\t\tError")

for i in range(max_iter):
    x = (a + b) / 2                   # Rumus (a + b)/2
    fx = f(x)                         # Hitung f(x)
    error = abs(b - a) / abs(b)       # Rumus mirip (D4 - C4)/D4

    print(f"{i+1}\t{a:.6f}\t{b:.6f}\t{x:.6f}\t{fx:.6f}\t{error:.6f}")

    # Cek konvergensi
    if abs(fx) < tol:
        print(f"\n Akar ditemukan: x ≈ {x:.6f}, f(x) ≈ {fx:.6f}")
        break

    # Update interval
    if f(a) * fx < 0:
        b = x
    else:
        a = x
else:
    print("\n Iterasi maksimum tercapai tanpa konvergensi.")
