# Latihan kalkulator sederhana


print(20*'=')
print('Kalkulator Sederhana')
print(20*'=')

bil1= float(input('masukkan angka pertama : \t'))
oper= input('operator (+,-,*,/) : \t\t')
bil2= float(input('masukkan angka kedua : \t\t'))

if oper == '+':
    hasil = bil1 + bil2
    print(f'{bil1} + {bil2} = {hasil}')

elif oper == '-':
    hasil = bil1 - bil2
    print(f'{bil1} - {bil2} = {hasil}')

elif oper == '*' or oper == 'x':
    hasil = bil1 * bil2
    print(f'{bil1} * {bil2} = {hasil}')

elif oper == '/':
    if bil2 != 0:
        hasil = bil1 / bil2
        print(f'{bil1} / {bil2} = {hasil}')
    else:
        print('division by zero')
    
else:
    print('anda memasukkan pilihan yang salah')