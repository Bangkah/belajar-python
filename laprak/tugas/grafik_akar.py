import matplotlib.pyplot as plt

# --- DATA dari gambar ---

# Data 1
x1 = [-3, -2, -1, 0, 1, 2, 3]
f1 = [37, 5, -1, -2, 1, 10, 23]

# Data 2
x2 = [-2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2.2, -2.1]
f2 = [4.12, 3.24, 2.48, 1.72, 1.00, 0.32, -0.32, -0.92, -1.48]

# Data 3
x3 = [-2.4, -2.39, -2.38, -2.37, -2.36, -2.35, -2.34, -2.33, -2.32, -2.31, -2.3]
f3 = [0.32, 0.188, 0.129, 0.0939, 0.0634, 0.0379, 0.0207, 0.0122, 0.00781, 0.00578, -0.005]

# Data 4
x4 = [-2.36, -2.355, -2.354, -2.353, -2.352, -2.351, -2.35, -2.349]
f4 = [0.0592, 0.0276, 0.02063, 0.01422, 0.00781, 0.0014, -0.005, -0.01114]

# Data 5
x5 = [-2.351, -2.3509, -2.3507, -2.3506, -2.3504, -2.3503, -2.3501, -2.35, -2.3499]
f5 = [0.0014, 0.00076, 0.000252, 0.00012, -0.00024, -0.00204, -0.0036, -0.005, -0.00564]


# --- FUNGSI bantu untuk cari akar paling dekat (f(x) ≈ 0) ---
def cari_akar(x, f):
    closest = min(zip(x, f), key=lambda t: abs(t[1]))
    return closest


# --- GRAFIK ---
datasets = [(x1, f1), (x2, f2), (x3, f3), (x4, f4), (x5, f5)]
plt.figure(figsize=(12, 6))

for i, (x, f) in enumerate(datasets, start=1):
    akar = cari_akar(x, f)
    plt.subplot(1, 5, i)
    plt.plot(x, f, marker='o')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.title(f"f{i}(x)\nAkar ≈ {akar[0]:.5f}")
    plt.grid(True)

plt.tight_layout()
plt.show()

# --- CETAK hasil akar ---
print("=== Perkiraan akar dari setiap dataset ===")
for i, (x, f) in enumerate(datasets, start=1):
    akar = cari_akar(x, f)
    print(f"Data {i}: x ≈ {akar[0]:.5f}, f(x) = {akar[1]:.5f}")
