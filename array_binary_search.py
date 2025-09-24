def pencarian_biner(A, x):
    low = 0  # Indeks awal
    high = len(A) - 1  # Indeks akhir

    while low <= high:
        mid = low + (high - low) // 2  # Hitung titik tengah

        if A[mid] < x:
            low = mid + 1  # Cari di bagian kanan
        elif A[mid] > x:
            high = mid - 1  # Cari di bagian kiri
        else:
            return mid  # Nilai ditemukan

    return -1  # Nilai tidak ditemukan


def output_pencarian(A, x):
    hasil = pencarian_biner(A, x)
    if hasil != -1:
        print(f"Nilai {x} ditemukan pada indeks {hasil}")
    else:
        print(f"Nilai {x} tidak ditemukan dalam array")


# Contoh penggunaan
A = [10, 20, 30, 40, 50]  # Daftar harus dalam keadaan terurut
x = 30
output_pencarian(A, x)