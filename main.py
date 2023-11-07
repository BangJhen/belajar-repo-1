# Kalkulator sederhana

print("""Kalkulator Sederhana
      1. Penambahan
      2. Pengurangan
      3. Perkalian
      4. Pembagian""")
op = int(input("Masukkan Angka Operator Aritmatika : "))


match op:
    case 1:
        n1 += n2 
    case 2:
        n1 -= n2 
    case 3:
        n1 *= n2 
    case 4:
        n1 /= n2 

print(n1)