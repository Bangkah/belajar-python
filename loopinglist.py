# looping dari list

# for loop
kumpulanangka = [3,4,2,5,8,9,3,4]

print('ini for loop')
for angka in kumpulanangka:
    print(f"angka = {angka}")

# peserta = ["dadang","diding",'dudung','asep','rahmat']

# for nama in peserta:
#     print(f"nama : {nama}")

# for loop dan range

print('\nini for loop dan range')
kumpulanangka = [10,5,7,3,8]

panjang = len(kumpulanangka)

for i in range(panjang):
    print(f"angka = {kumpulanangka[i]}")

# while

print('\nini while loop')
kumpulanangka = [10,5,7,3,8]
panjang = len(kumpulanangka)
i = 0

while i < panjang:
    print(f"angka = {kumpulanangka[i]}")
    i += 1

# list compherhension

print('\nini list compherhension')
data = ['ucup',1,2,3,'dadang']

[print(f"data = {i}") for i in data]

angka = [10,5,7,3,8]

angkakuadrat = [i**2 for i in angka]
print(angkakuadrat)

# enumerat
print('\nini enumeret')
datalist = ['ucup',1,2,3,'dadang']

for index,data in enumerate(datalist):
    print(f"index = {index}, data = {data}")

