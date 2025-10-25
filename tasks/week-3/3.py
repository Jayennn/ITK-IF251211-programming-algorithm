"""
Sebuah aplikasi transportasi online ingin menentukan tarif perjalanan berdasarkan jarak tempuh:
--> Jika jarak ≤ 2 km → tarif Rp10.000
--> Jika jarak > 2 km dan ≤ 5 km → tarif Rp20.000
--> Jika jarak > 5 km → tarif Rp20.000 + Rp3.000 untuk setiap km tambahan di atas 5 km
"""

jarak = int(input("Masukkan jarak (km): "))

if jarak <= 2:
    tarif = 10000
# tulis kode di sini (tambahkan elif dan else untuk kondisi lainnya)

print("Total tarif: Rp", tarif)
