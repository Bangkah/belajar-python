'''
### Langkah-langkah:

#### 1. Tentukan turunan fungsi:
\[
f'(x) = 3x^2 - 9
\]

#### 2. Rumus iterasi Newton-Raphson:
\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

#### 3. Tebakan awal:
\[
x_0 = 0.5,\quad \text{toleransi} = 0.001
\]

---

### Iterasi Manual (Beberapa Langkah Pertama)

#### Iterasi 1:
\[
x_0 = 0.5 \\
f(x_0) = (0.5)^3 - 9(0.5) + 3 = 0.125 - 4.5 + 3 = -1.375 \\
f'(x_0) = 3(0.5)^2 - 9 = 0.75 - 9 = -8.25 \\
x_1 = 0.5 - \frac{-1.375}{-8.25} \approx 0.5 - 0.1667 = 0.3333
\]

#### Iterasi 2:
\[
x_1 = 0.3333 \\
f(x_1) \approx (0.037) - 3 + 3 = 0.037 - 2.9997 = -2.9627 \\
f'(x_1) = 3(0.3333)^2 - 9 \approx 0.3333 - 9 = -8.6667 \\
x_2 = 0.3333 - \frac{-2.9627}{-8.6667} \approx 0.3333 - 0.3417 = -0.0084
\]

#### Iterasi 3:
\[
x_2 = -0.0084 \\
f(x_2) \approx (-0.0000006) + 0.0756 + 3 = 3.0756 \\
f'(x_2) = 3(-0.0084)^2 - 9 \approx 0.0002 - 9 = -8.9998 \\
x_3 = -0.0084 - \frac{3.0756}{-8.9998} \approx -0.0084 + 0.3417 = 0.3333
\]
'''

def f(x):
    return x**3 - 9*x + 3

def f_prime(x):
    return 3*x**2 - 9

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
newton_raphson(0.5)
