# soal 1
angka = [3, 6, 1, 9, 2]
total = sum(angka)
print(total)

# soal 2
buah = ['apel', 'pisang', 'jeruk', 'apel', 'mangga']
while 'apel' in buah:
    buah.remove('apel')
print(f"list setelah di hapus : {buah}")

# soal 3
huruf = ['a', 'b', 'c', 'd', 'e']
hurufterbalik = huruf[::-1]
print(f"list terbalik : {hurufterbalik}")

# soal 4
nilaiasli = [70,80,90]
nilaicopy = nilaiasli.copy()

for i in range(len(nilaicopy)):
    nilaicopy[i] += 5
print(f"nilai asli : {nilaiasli}")
print(f"nilai setelah dimodifikasi : {nilaicopy}")

# soal 5
data = [1, 3, 5, 7, 9]
n = int(input('masukkan angka : '))
if n in data:
    print('ada')
else:
    print('tidak ada')

