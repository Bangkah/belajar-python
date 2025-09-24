# continue & pass

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass # ini tidak akan dieksekusi
    print(angka)

# continue ->

angka = 0

print(f'angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print(f'angka sekarang -> {angka}')
    
    if angka == 3:
        print('nice!')
        continue # akan meloncat ke step selanjutnya/ meng cut kode di bawah 

    print("whatsup")

print('akhir program')