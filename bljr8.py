#belajar tentang fungsi dalam bahasa python
#fungsi adalah blok kode yang dpt digunakan kembali untuk melakukan tugas tertentu.

def sapa():
    print("Halo! selamat datang di progam kami.")

def nama():
    print("nama saya adalah noel ")

nama()

#fungsi dengan paramer
def sapa_nama(nama):
    print(f"halo, {nama}! selamat datang di progam kami.")


sapa_nama("noel")
sapa_nama("budi")

print("================Fungsi dengan parameter=================")

#fungsi dengan nilai kembalian (return)

buah_buahan = ["apel", "mangga" "anggur", "kiwi"]
def total_buah (buah_list):
    total = 0
    for buah in buah_list:
     return total

jumlah_buah = total_buah(buah_buahan)
print("jumlah buah dalam list:", jumlah_buah)

belanjaan = ["sayur", "daging", "ikan"]
jumlah_belanjaan = total_buah (belanjaan)
print ("jumlah belanjaan dalam list:",jumlah_belanjaan)

print("====================fungsi dengan nilai default================")
#fungsi dengan nilai default
def sapa_pengguna (nama="rendi"):
   print(f"halo, {nama}! selamat datang di progam kami.")

sapa_pengguna()
sapa_pengguna("noel")

print("===========latian list dan fungsi==========")
#latian pengguna list dan fungsi
def tambah_buah(buah_list, buah_baru):
   buah_list.append(buah_baru)
   return buah_list

daftar_buah = ["apel", "mangga", "anggur"]

print("daftar buah awal:", daftar_buah)

daftar_buah = tambah_buah(daftar_buah, "kiwi")
print("setelah menambahkan kiwi:", daftar_buah)
daftar_buah = tambah_buah(daftar_buah, "pisang")
print("setelah menambahkan pisang:", daftar_buah)


print("==============latihan fungsi perhitungan============")
#latihan fungsi untuk perhitungan sederhana
def hitung_luas_persegi(sisi):
   return sisi * sisi

def hitung_luas_segitiga(alas, tinggi):
   return 0.5 * alas * tinggi

sisi_persegi = 4
luas_persegi = hitung_luas_persegi(sisi_persegi)
print(f"luas persegi dengan sisi {sisi_persegi} adalah: {luas_persegi}")

luas_segitiga = 5
tinggi_segitiga = 10
luas_persegi = hitung_luas_segitiga(luas_segitiga, tinggi_segitiga)
print(f"luas segitiga dengan alas {luas_segitiga} dan tinggi {tinggi_segitiga} adalah: {luas_segitiga}")