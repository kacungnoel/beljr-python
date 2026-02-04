#perulangan dengan range dan len
buah_buahan =["apel", "pisang", "jeruk","mangga" ]

#perulangan dengan data
for buah in buah_buahan:
    print (buah)
    
print ("===============================================")

# perulangan dengan index
for index in range (len(buah_buahan)):
    print (f"buah ke {index+1} adalah {buah_buahan[index]}")


#perulangan dengan while
count = 0 
while count < len (buah_buahan):
    print (f"buah ke-{count+1} adalah {buah_buahan[count]}")
    count +=1 

print ("================break=============================") 
# perulangan dengan break
for buah  in buah_buahan:
    if buah == "mangga":
        print(f"ditemukan buah {buah}, menghentikan perulangan.")
        break
    print (f"buah: {buah}")

    print ("=============continue============")

#melanjutkan perulangan dengan continue
for buah in buah_buahan:
    if buah == "jeruk":
        # print (f"melewati buah {buah}.")
        continue
    print (f"buah")

print ("==============while break==============")

# while dengan break
count = 0
while count < len (buah_buahan):
    if buah_buahan (count) == "jeruk":
        print (f"ditemukan buah {buah_buahan[count]}, menghentikan perulangan.")
        break
    print (f"buah ke-{count+1}adalah {buah_buahan[count]}")
    count += 1

#studi kasus: mencari angka genap dalam daftar

angka = (1, 3, 6, 8, 10)

for num in angka:
    if num % 2 != 0:
        print (f"semua angka genap: {num}")
        
