try:
    # masukkan usia
    usia = int(input("Masukkan usia kamu: "))
    print(f"Usia kamu adalah {usia} tahun.")

# error jika yang dimasukkan bukan angka
except ValueError:
    print("Input tidak valid! Masukkan angka saja.")
