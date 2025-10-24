# Program daftar nilai mahasiswa (List Paralel)

# Input jumlah mahasiswa
n = int(input("Masukkan jumlah mahasiswa: "))

# Inisialisasi dua list kosong
list_nama = []
list_nilai = []

# Input data mahasiswa
for i in range(n):
    print(f"\nMahasiswa ke-{i + 1}")
    nm = input("Nama: ")
    nl = float(input("Nilai: "))
    # >>> Lengkapi bagian untuk menambahkan nama dan nilai ke list <<<
    # list_nama.append(_____)
    # list_nilai.append(_____)

# Tampilkan daftar nilai
print("\nDaftar Nilai:")
# >>> Lengkapi bagian untuk menampilkan data dari kedua list <<<
# for i in range(_____):
#     print(f"{list_nama[i]} : {list_nilai[i]}")

# Hitung rata-rata
# >>> Lengkapi rumus rata-rata menggunakan fungsi sum() dan len() <<<
# rata = _____

# Cari nilai tertinggi
# >>> Gunakan fungsi max() dan index() untuk mencari nama dan nilai tertinggi <<<
# maks = _____
# indeks = _____
# nama_maks = _____

# Tampilkan hasil akhir
print(f"\nRata-rata nilai: {rata:.2f}")
print(f"Nilai tertinggi: {nama_maks} ({maks})")
