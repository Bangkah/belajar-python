# ---------- 1. data (sesuai tabel di gambar) ----------
import numpy as np, pandas as pd, matplotlib.pyplot as plt

x = np.array([3.28, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9])
f = np.array([4.12, 2.359, 2.48, 1.72, 2.36, 0.32, -0.32, -0.92, -1.48, -2.3, -2.3])
mid = np.array([np.nan, 2.35, 2.38, 2.37, 2.36, 2.35, 2.34, 2.33, 2.32, 2.31, 2.3])
bot = np.array([np.nan, 2.3509, 2.3508, 2.3507, 2.3506, 2.3505,
                2.3504, 2.3503, 2.3502, 2.3501, 2.3499])

df = pd.DataFrame({'x': x, 'f(x)': f, 'mid': mid, 'bot': bot})
print(df.head())

# ---------- 2. plot ----------
plt.figure(figsize=(8,4))
plt.plot(df.x, df['f(x)'], '-o', label='f(x)')
plt.plot(df.x, df.mid, '-s', label='mid')
plt.plot(df.x, df.bot, '-^', label='bot')
plt.title('Hasil tabel LibreOffice'), plt.legend(), plt.show()