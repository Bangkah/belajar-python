# Latihan perulangan membuat segitiga

# 1. dengan for 
# sisi = int(input('masukkan jumlah baris bintang : '))

# # dummy variable
# count = 1
# for i in range(sisi):
#     print("*"*count)
#     count += 1

# 2. menggunakan while

# banyak = int(input('banyak baris : '))
# count = 1  
# while True:
#     print('*'*count)
#     count += 1

#     if count > banyak:
#         break

# print('akhir while')

# 3. hanya ganjil saja

# banyak = int(input('masukkan banyak baris : '))
# count = 1
# while True:
#     print("*"*count)
#     count += 2
#     if count > banyak : 
#         break
# print('akhir dari program')


# 4. segitiga sama kaki

banyak = int(input('masukkan banyak baris : '))
count = 1
while count <= banyak:
    spasi = ' ' * (banyak - count)
    bintang = '*' * (2 * count - 1)
    print(spasi + bintang)
    count += 1

count -= 2

while count > 0:
    spasi = ' ' * (banyak - count)
    bintang = '*' * (2 * count - 1)
    print(spasi + bintang)
    count -= 1



print('akhir dari program')