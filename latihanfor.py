# ini adalah latihan for

# # nomor 1
# for i in range(1,11):
#     print(i)
# print('akhir program')

# # nomor 2
# for i in range(2,21,2):
#     print(i)

# # nomor 3
# teks = input('masukkan kata : ')
# for huruf in teks:
#     print(huruf)

# # nomor 4
# angka = [2,4,5,7,9,10]
# total = 0
# for i in angka:
#     total += i
# print(f'angka: {total}')

# # nomor 5
# angka = int(input('angka yang ingin di faktorialkan : '))
# faktorial = 1
# for i in range(1, angka + 1):
#     faktorial *= i
# print(f'faktorial : {faktorial}')

# # nomor 6
# n = int(input('masukkan jumlah baris : '))
# for i in range(1, n+1):
#     print('*' * i)

# nomor 7
# n = int(input('masukkan baris : '))
# for i in range(n,0,-1):
#     print('*'*i)

# nomor 8
# n = int(input('masukkan batas : '))
# for num in range(2,n+1):
#     prima = True
#     for i in range(2,num):
#         if num % i == 0:
#             prima = False
#             break
#     if prima:
#         print(num, end=(" "))

# # nomor 9
# n = int(input('masukkan jumlah baris : '))
# for i in range(1, n + 1):
#     spasi = ' ' * (n - i)
#     bintang = '*' * (2 * i - 1)
#     print(spasi + bintang)

# for i in range(n-1,0,-1):
#     spasi = ' ' * (n - i)
#     bintang = '*' * (2 * i - 1)
#     print(spasi + bintang)

