
kelas = "python"
siswa  = 2

# logika if (jika)
if siswa ==2:
    print(f"kelasnya adalah: {kelas}")

#logika if dan else (jika atau lainnya)
if siswa >= 2:
    print(F"kelasnya besar")
else:
    print(f"kelasnya kecil")

   # logika is atau elif atau else (jika atau jika lainnya atau lainnya)
if siswa < 1:
    print(f"siswa sedikit sekali")
elif siswa >= 2:
    print(f"siswa seimbang ")
elif siswa !=1:
    print(f"siswa kuranng")
else: 
    print(f"siswa lainnya")

    #LATIHAN : buatlaj penggunaan if atau elif atau else dari variabel berikut
tinggi = 160
tinggi_sekali = "tinggi sekali"
pendek_sekali = "pendek sekali"
tinggi_sedang = "tinggi sedang"

if tinggi <160:
    print (f"tinggi: {tinggi_sekali}")
elif tinggi >=99:
    print(f"tinggi:{pendek_sekali}")
else:
    print(f"tinggi{tinggi_sekali}:")

