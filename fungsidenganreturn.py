# fungsi dengan return

# def nama_fungsi(argument):
#   badan fungsi
#   return output

# fungsi kuadrat

def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat 

y = kuadrat(5)
print(y)

# fungsi tambah 

def fungsi_tambah(angka1,angka2):
    return angka1 + angka2

a = fungsi_tambah(4,8)
print(a)


# fungsi dengan return banyak

def operasi_matematika(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)

print(f'hasil tambah = {k}')
print(f'hasil kurang = {l}')
print(f'hasil kali = {m}')
print(f'hasil bagi = {n}')