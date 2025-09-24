# membuat fungsi

# fungsi tanpa argument
# def hello_world():
#     print('hello world')

# hello_world()

# fungsi dengan argument

'''
def namafungsi(argumen):
    badan fungsi
'''

def hello_world(nama):
    print(f'selamat datang di dunia wahai {nama}')

hello_world('raja')

# program tambah

def tambah(angka1,angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(3,5)

def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'yang terhormat {peserta}')

anggota = ['ucup','nando','asep']

say_hi(anggota)