# operasi aritmatika

a= int(input("masukkan angka pertama : "))
b= int(input("masukkan angka kedua : "))

# tambah

hasil = a + b 
print(a,'+',b,'=',hasil) 

# kurang

hasil = a - b
print(a,'-',b,'=',hasil)

# kali

hasil = a * b
print(a,'*',b,'=',hasil)

# bagi

hasil = a / b
print(a,'/',b,'=',hasil)

# pangkat

hasil = a ** b
print(a,'**',b,'=',hasil)

# modulus

hasil = a % b
print(a,'%',b,'=',hasil)

#  floor divisiom

hasil = a // b
print(a,'//',b,'=',hasil)



c= int(input("masukkan huruf pertama : "))
d= int(input("masukkan huruf kedua : "))
e= int(input("masukkan huruf ketiga : "))

# priotitas operasi

hasil2= c ** d * e + c / d - d % e // c 

print(c,'**',d,'*',e,'+',c,'/',d,'-',d,'%',e,'//',c,'=',hasil2)

