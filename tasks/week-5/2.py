"""
Kembangkan program pada Soal 1, tetapi kali ini gunakan list 2 dimensi untuk menyimpan data mahasiswa dan nilainya.
Setiap elemen list utama berisi data mahasiswa dalam bentuk: [nama, nilai]
Program harus menampilkan:
--> Seluruh daftar mahasiswa dan nilainya
--> Nilai rata-rata kelas
--> Mahasiswa dengan nilai tertinggi
"""

# Input jumlah mahasiswa
n = int(input("Masukkan jumlah mahasiswa: "))

# Inisialisasi list 2D
data = []  # tiap elemen: [nama, nilai]

# Input data mahasiswa
for i in range(n):
    print(f"\nMahasiswa ke-{i + 1}")
    nm = input("Nama: ")
    nl = float(input("Nilai: "))
    # Tambahkan data ke dalam list 2D
    # tulis kode di sini

# Tampilkan daftar nilai
print("\nDaftar Nilai Mahasiswa:")
# tulis kode di sini

# Hitung rata-rata
total = 0
# tulis kode di sini

# Cari nilai tertinggi
# tulis kode di sini

# Tampilkan hasil akhir
print(f"\nRata-rata nilai: {rata:.2f}")
print(f"Nilai tertinggi: {tertinggi[0]} ({tertinggi[1]})")
