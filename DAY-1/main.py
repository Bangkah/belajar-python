nama = "Atha"             # str
umur = 18                 # int
tinggi = 165.0            # float
is_mahasiswa = True       # bool
hobi = ["membaca", "olahraga"] # list
alamat = "Lhoksemawe"     # str
tempat_lahir = "Meulaboh" # str
tanggal_lahir = "20-02-2007" # str

print("Contoh Variabel dan Tipe Data:")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa:", is_mahasiswa)
print("Hobi:", ", ".join(hobi))
print("Alamat:", alamat)
print("Tempat Lahir:", tempat_lahir)
print("Tanggal Lahir:", tanggal_lahir)

print("\n=== Perulangan FOR ===")
# menampilkan semua hobi dengan for
for h in hobi:
    print("Hobi saya:", h)

print("\n=== Perulangan WHILE ===")
# menghitung dari 1 sampai umur dengan while
i = 1
while i <= 5:
    print("Hitungan ke-", i)
    i += 1
