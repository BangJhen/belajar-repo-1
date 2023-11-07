# Kalkulator sederhana
opList = {1 : "+", 2 : "-", 3 : "/",4 : "x"}


print("""Kalkulator Sederhana
      1. Penambahan
      2. Pengurangan
      3. Perkalian
      4. Pembagian""")
op = int(input("Masukkan Angka Operator Aritmatika : "))
n1 = float(input("Masukkan Pembilang : "))
n2 = float(input("Masukkan Penyebut : "))

match op:
    case 1:
        hasil = n1 + n2 
    case 2:
        hasil = n1 - n2 
    case 3:
        hasil = n1 * n2 
    case 4:
        hasil = n1 / n2 

print(f"{n1} {opList[op]} {n2} = {hasil} ")