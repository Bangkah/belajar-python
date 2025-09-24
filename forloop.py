# Perulangan (Loop)

# for kondisi:
#     aksi

# dengan array
angkalist = [2,5,7,9,11]

for i in angkalist:
    print(f'i sekarang => {i}')

print('akhir dari program 1\n')

# dengan range
angkarange = range(5)

for i in angkarange:
    print(f'i sekarang => {i}')

print('akhir dari program 2\n')

angkarange = range(3,5)

for i in angkarange:
    print(f'i sekarang => {i}')

print('akhir dari program 3\n')


# menggunakan string

datastr = 'aku ganteng'

for huruf in datastr:
    print(huruf)