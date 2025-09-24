# operasi list

dataangka = [2,3,5,7,2,4,6,7,4,9,1,0]
print(f"data angka = {dataangka}")

# count data
jumlah_data_4 = dataangka.count(4)
jumlah_data_3 = dataangka.count(3)

print(f"jumlah angka 4 : {jumlah_data_4}")
print(f"jumlah angka 3 : {jumlah_data_3}")

# ambil posisi data (index)
data = ['ryan','rasyid','arsyad','ziyad']

print(f"data = {data}")

indexrasyid = data.index('rasyid')
indexziyad = data.index('ziyad')

print(f"index si rasyid : {indexrasyid}")
print(f"index si ziyad : {indexziyad}")

# mengurutkan list
print(f"data angka sebelum di urutkan : \n{dataangka}")
dataangka.sort()
print(f"data angka sesudah di sort : \n{dataangka}")

print(f"data : {data}")
data.sort()
print(f"data sort : {data}")

dataangka.reverse()
data.reverse()
print(f"data sesudah di reverse : \n{dataangka} \n{data}")