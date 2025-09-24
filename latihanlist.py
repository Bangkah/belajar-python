# program list buku

list_buku = []
while True:
    print('masukkan data buku')
    judul = input("masukkan judul buku\t:")
    nama = input("masukkan nama penulisi\t:")

    databuku = [judul,nama]
    list_buku.append(databuku)

    print("no.\t | \tjudul\t\t\t | \tpenulis\t")
    for index,buku in enumerate(list_buku):
        print(f"{index+1}\t | \t{buku[0]}\t | \t{buku[1]}\t ")
    
    tanya = input('apakah ingin lanjut ? (y/t)')
    if tanya != 'y':
        break