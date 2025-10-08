import numpy as np
import matplotlib.pyplot as plt

# === Definisi fungsi ===
def f(x):
    return 2*x**2 + 3*x - 4   # Ubah fungsi ini sesuai kebutuhanmu

# === Data x ===
x = np.arange(-3, 3.5, 0.5)  # dari -3 ke 3 dengan step 0.5
fx = f(x)

# === Cetak tabel nilai ===
print("x\tf(x)")
print("-" * 20)
for xi, fi in zip(x, fx):
    print(f"{xi:.2f}\t{fi:.4f}")

# === Cari akar paling mendekati 0 ===
akar_index = np.argmin(np.abs(fx))
akar_x = x[akar_index]
akar_fx = fx[akar_index]

print("\n=== Perkiraan akar fungsi ===")
print(f"x ≈ {akar_x:.5f}, f(x) ≈ {akar_fx:.5f}")

# === Tampilkan grafik ===
plt.figure(figsize=(7, 5))
plt.plot(x, fx, 'bo-', label='f(x) = 2x² + 3x - 4')
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(akar_x, color='red', linestyle=':', label=f"Akar ≈ {akar_x:.3f}")
plt.title("Grafik Fungsi f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
