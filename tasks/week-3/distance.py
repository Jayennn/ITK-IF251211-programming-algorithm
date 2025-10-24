jarak = int(input("Masukkan jarak (km): "))

if jarak <= 2:
    tarif = 10000
elif jarak <= 5:
    tarif = 20000
else:
    tarif = 20000 + ((jarak - 5) * 3000)

print("Total tarif: Rp", tarif)