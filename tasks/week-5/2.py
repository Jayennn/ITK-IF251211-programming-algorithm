# Program daftar nilai mahasiswa (List 2 Dimensi)

# Input jumlah mahasiswa
n = int(input("Masukkan jumlah mahasiswa: "))

# Inisialisasi list 2D
data = []  # tiap elemen: [nama, nilai]

# Input data mahasiswa
for i in range(n):
    print(f"\nMahasiswa ke-{i + 1}")
    nm = input("Nama: ")
    nl = float(input("Nilai: "))
    # >>> Lengkapi bagian untuk menambahkan data ke dalam list 2D <<<
    # data.append([_____, _____])

# Tampilkan daftar nilai
print("\nDaftar Nilai Mahasiswa:")
# >>> Lengkapi bagian untuk menampilkan isi list data <<<
# for i in range(len(data)):
#     print(f"{i+1}. {_____} - {_____}")

# Hitung rata-rata
# >>> Gunakan perulangan untuk menjumlahkan semua nilai <<<
total = 0
# for d in _____:
#     total += _____
# rata = total / _____

# Cari nilai tertinggi
# >>> Gunakan logika percabangan untuk membandingkan nilai tertinggi <<<
# tertinggi = data[0]
# for d in data:
#     if _____ > _____:
#         tertinggi = _____

# Tampilkan hasil akhir
print(f"\nRata-rata nilai: {rata:.2f}")
print(f"Nilai tertinggi: {tertinggi[0]} ({tertinggi[1]})")
