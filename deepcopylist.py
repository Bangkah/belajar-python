data0 = [1,2]
data1 = [3,4]

data2d = [data0,data1]
data2dcopy = data2d.copy()

print(f"data : {data2d}")
print(f"data copy : {data2dcopy}")


# mengambil data dari nested list
data = data2d[0][1]
print(f"data : {data}")

# address semuanya

print(f"addres asli : {hex(id(data2d))}")
print(f"addres copy : {hex(id(data2dcopy))}")

print(f"address dari member ke 1")
print(f"addres asli : {hex(id(data2d[0]))}")
print(f"addres copy : {hex(id(data2dcopy[0]))}\n")

# menggunakan deepcopy

from copy import deepcopy

data2d = [data0,data1,10]
data2ddeepcopy = deepcopy(data2d)

print(f"addres asli : {hex(id(data2d))}")
print(f"addres copy : {hex(id(data2ddeepcopy))}")


print(f"address dari member ke 1")
print(f"addres asli : {hex(id(data2d[0]))}")
print(f"addres copy : {hex(id(data2ddeepcopy[0]))}\n")