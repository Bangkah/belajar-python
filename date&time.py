import datetime as dt

print('masukkan tanggal lahir kamu')

tanggal = int(input("masukkan tanggal lahir : \t"))
bulan = int(input("masukkan bulan lahir : \t\t"))
tahun = int(input("masukkan tahun lahir : \t\t"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f'tanggal lahir kamu adalah : {tanggal_lahir}')

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
umur_minggu = ((umur_hari.days % 365) // 30) // 7
print(f'umur kamu adalah :{umur_tahun} tahun, {umur_bulan} bulan, {umur_minggu} minggu.')
print(f'kamu lahir pada hari {tanggal_lahir:%A}')