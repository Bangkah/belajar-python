def search_array(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return f"Elemen {target} ditemukan pada indeks {i}"
    return f"Elemen {target} tidak ditemukan dalam array"

def delete_element(arr, target):
    if target in arr:
        arr.remove(target)
        return f"Elemen {target} telah dihapus. Array baru: {arr}"
    else:
        return f"Elemen {target} tidak ditemukan dalam array"

# Contoh penggunaan
array = [10, 20, 30, 40, 50]
target = int(input("Masukkan angka yang ingin dicari: "))
result = search_array(array, target)
print(result)

delete_target = int(input("Masukkan angka yang ingin dihapus: "))
delete_result = delete_element(array, delete_target)
print(delete_result)