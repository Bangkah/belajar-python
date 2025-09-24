# list/array

# kumpulan data numbers
dataangka = [1,2,3,4,5]
print(dataangka)

# kumpulan data str
datastr = ['ucup','otong','raja','rico',]
print(datastr)

# kumpulan data boolean
databoolean = [True, False, True, True]
print(databoolean)

# kumpulan campuran
campuran = [1,"bakwan",2,"pisang goreng","raja",True,"rico",False]
print(campuran)

# alternatif membuat list
datarange = range(0,10,2) # start,stop,step
print(datarange)
datalist = list(datarange)
print(datalist)

# list denga =n for loop, list comprehension
datafor = [i for i in range(0,10)]
print(datafor)

# bisa di kuadratkan/dengan operator math lainnya
datafor = [i**2 for i in range(0,10)]
print(datafor)

# list dengan for if
dataforif = [i for i in range(0,10) if i != 5]
print(dataforif)

# angka genap saja
dataforif = [i for i in range(0,10) if i % 2 == 0]
print(dataforif)
# angka ganjil saja
dataforif = [i for i in range(0,10) if i % 2 != 0]
print(dataforif)

