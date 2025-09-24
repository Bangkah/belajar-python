# manipulasi data list

# operasi
# index    0      1     2   
data = ["raja","rico","kiel"]

# mengambil data dari list
data0 = data[0]
print(f'data pertama(index nol) adalah : {data0}')

# data terakhir
dataterakhir = data[-1]
print(f'data terakhir adalah : {dataterakhir}')

# mengambil info jumlah data dalam list
jumlahdata = len(data)
print(f'panjang data adalah : {jumlahdata}')

## manipulasi data list

# menambahkan item pada list sesuai dengan posisi
print(f"data sebelum di tambahkan : \n{data}")

# menambah di tengah list
data.insert(1,"bima")
print(f"data setelah di tambahkan : \n{data}")

# menambah di akhir list
data.append("gatpan")
print(f"data setelah di tambahkan : \n{data}")

# menambahkan list dengan list
databaru = ["sean","asep","dudung"]
data.extend(databaru)
print(f"data gabungan adalah : \n{data}")

# merubah data
data[2] = "jelek"
print(f"data sesudah di rubah : \n{data}")

# menghapus data
data.remove("bima")
print(f"data sesudah di hapus : \n{data}")

# menghapus data paling belakang
dataakhir = data.pop()
print(f"data terakhir sesudah di hapus : \n{data}")

# mengambil data akhir saja
print(dataakhir)