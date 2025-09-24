# break
# contoh 1
angka = 0 

while angka < 5:
    angka += 1
    print(f'count -> {angka}')

    if angka == 3:
        print('nice!')
        break

    print('wassup')
print('cukupp')

# contoh 2
angkaint = int(input('ingin menghitung sampai : '))
angka = 0 

while True:
    angka += 1
    print(f'count -> {angka}')

    if angka == angkaint:
        print('nice!')
        break

    print('wassup')
print('cukupp')