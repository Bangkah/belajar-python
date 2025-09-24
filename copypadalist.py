# copy di list

a = ['ucup','otong','dudung']
print(f"a = {a}")

b = a
print(f"b = {b}")

# merubah member dari a
# akan merubah kedua data
a[1] = "asep"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# menduplicat list dengan copy
print('membuat list c dengan a.copy()')
c = a.copy() 

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}") #addres c berbeda dengan a dan b

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print('mengubah data 0')
c[0] = "dadang"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
