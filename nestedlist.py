# cara membuat list di dalam list
data0 =[1,2]
data1 =[3,4]

list2d = [data0,data1] #bisa beberapa data list yang lain, dan juga langsung menambahkan data
print(f"list 2D : {list2d}")

# contoh penggunaan
peserta0 = ["ucup",21,"pria"]
peserta1 = ["akbar",10,"pria"]
peserta2 = ["riza",50,"wanita"]

listpeserta = [peserta0,peserta1,peserta2]

print(f"peserta : {listpeserta}")
for peserta in listpeserta:
    print(f"nama \t: {peserta[0]}")
    print(f"umur \t: {peserta[1]}")
    print(f"gender \t: {peserta[2]}\n")