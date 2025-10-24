
total = 0
jumlah_siswa = 5

for i in range(1, jumlah_siswa + 1):
  nilai = int(input(f"Masukkan nilai siswa ke-{i}: "))
  total += nilai


rata_rata = total / jumlah_siswa
print(f"Total nilai = {total}")
print(f"Rata-rata = {rata_rata}")