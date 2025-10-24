for i in range(1, 31):
  if i % 3 == 0 and i % 5 == 0:
    print(f"Pelanggan {i}: Diskon 50%")
  elif i % 3 == 0:
    print(f"Pelanggan {i}: Diskon 10%") 
  elif i % 5 == 0:
    print(f"Pelanggan {i}: Diskon 20%")
  else:
    print(f"Pelanggan {i}: Tidak ada diskon")

  

  