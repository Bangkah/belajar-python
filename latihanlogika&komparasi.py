# latihan logika dan komparasi

# input angka
# soal 1
# ----0++++5----8++++11----
inputuser = float(input("masukkan angka = "))

lebihdari_0 = inputuser > 0
print(f"lebih dari 0 = {lebihdari_0}")

kurangdari_5 = inputuser < 5
print(f"kurang dari 5 = {kurangdari_5}")

lebihdari_8 = inputuser > 8
print(f"lebih dari 8 = {lebihdari_8}")

kurangdari_11 = inputuser < 11
print(f"kurang dari 11 = {kurangdari_11}")

isbenar = (lebihdari_0 and kurangdari_5) or (lebihdari_8 and kurangdari_11)
print(f"angka yang anda masukkan memenuhi kondisi = {isbenar}")

# soal 2
# ++++0----5++++8----11++++
inputuser = float(input("masukkan angka = "))

kurangdari_0 = inputuser < 0
print(f"kurang dari 0 = {kurangdari_0}")

lebihdari_5 = inputuser > 5
print(f"lebih dari 5 = {lebihdari_5}")

kurangdari_8 = inputuser < 8
print(f"kurang dari 8 = {kurangdari_8}")

lebihdari_11 = inputuser > 11
print(f"lebih dari 11 = {lebihdari_11}")

isbenar = (kurangdari_0 or lebihdari_5) and (kurangdari_8 or lebihdari_11)
print(f"angka yang anda masukkan memenuhi kondisi = {isbenar}")

# soal 3
# -----(-10)+++++(-5)----
inputuser = float(input("masukkan angka = "))

lebihdari = inputuser > -10
print(f"lebih dari -10 = {lebihdari}")

kurangdari = inputuser < -5
print(f"kurang dari -5 = {kurangdari}")

isbenar = lebihdari and kurangdari
print(f'angka yang anda masukkan memenuhi kondisi = {isbenar}')

