try:
    # terima input angka pertama
    angka1 = int(input("Masukkan angka pertama: "))

    # terima input angka kedua
    angka2 = int(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2
    print(f"Hasil pembagian: {hasil}")

# error jika yang dimasukan bukan angka
except ValueError:
    print("Terjadi kesalahan: Input harus berupa angka!")

# eror jika yang dimasukkan angka2 adalah 0
except ZeroDivisionError:
    print("Terjadi kesalahan: Tidak bisa membagi dengan nol!")
