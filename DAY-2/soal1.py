def f(x):
    return x**3 - 2*x - 5

def f_prime(x):
    return 3*x**2 - 2

def newton_raphson(x0, tolerance=1e-3, max_iter=100):
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
newton_raphson(2)

# - Fungsi f(x) dan f_prime(x) masing-masing adalah fungsi utama dan turunannya.
# - Iterasi dilakukan hingga perubahan nilai antar iterasi kurang dari toleransi 10^{-3}.
# - Hasilnya akan menampilkan setiap langkah iterasi dan akar yang ditemukan.
