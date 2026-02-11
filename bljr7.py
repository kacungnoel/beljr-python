# belajar 7 - list dan perulangan lanjutan di pyhton
# funsi dalam list seperti append, insert, remove,pop,clear,index,count,sort,reverse,copy

#contoh penggunaan append 
buah_buahan = ["apel", "mangga","anggur"]
print ("list awal :",buah_buahan)

print ("============Append===============")

#menambahkan elemen baru ke dalam list 
buah_buahan. append ('kiwi')
print ("setelah append kiwi:",buah_buahan)

print ("============Insert=================")
#menyisipkan elemen pada indeks tertentu
buah_buahan.insert(1,'pisang')
print ("setelah insert pisang pada indeks 1:, buah_buahan")

print ("===========pop==================")
#menghapus elemen tertentu dari list
#buah_buahan = ["apel", "mangga", "anggur", "kiwi"] 
buah_buahan.pop ()
print ("setelah pop:",buah_buahan)

print("============Remove===============")
buah_buahan.remove("pisang")
print ("setelah remove pisang:", buah_buahan)

print("============index============")
#menghitung jumlah kemunculan elemen tertentu

# buah_buahan = ["apel", "mangga", "anggur", "kiwi", "apel"]
buah_buahan.append("apel")  
jumlah_buah_apel = buah_buahan.count("apel")
print("jumlah buah apel dalam list:", jumlah_buah_apel)

jumlah_semua_apel = len(buah_buahan)
print("jumlah buah dalam list:", jumlah_semua_apel)

print("==============Clear=============")
#menghapus semua elemen dari list
buah_buahan.clear()
print("setelah clear:",buah_buahan)


#latihan logic kasir sederhana
print("==============latihan kasir=========")
kataloog_buah = {"apel": 5000, "mangga": 7000, "anggur": 6000, "kiwi": 8000 }
keranjang_belanja = []
total_harga_belanja = 0 

while True:
    nama_buah = input ("masukan nama buah yang dibeli (atau ketik selesai dan keluar): ")
    if nama_buah == "selesai":
        break
    elif nama_buah in kataloog_buah:
        keranjang_belanja.append(nama_buah)
        total_harga_belanja += kataloog_buah [nama_buah]
        print (f"buah {nama_buah}ditambahkan ke keranjang, dengan harga: {kataloog_buah[nama_buah]}")
    else:
        print ("maaf buah tidak tersedia atau salah perintah")

print("keranjang belanja buah:", keranjang_belanja)
print("total belanja buah:",total_harga_belanja)
print("terimakasih sudah belanja!")
