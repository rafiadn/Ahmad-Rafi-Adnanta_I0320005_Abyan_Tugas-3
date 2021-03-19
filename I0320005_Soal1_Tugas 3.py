#Mengisi list sebanyak 10
list = ['Rahmat', 'Rifqi', 'Deadila', 'Afnan', 'Anisa', 'Zaki', 'Bagus', 'Attar', 'Adhi', 'Alif']

#Menampilkan isi list indeks nomor 4, 6, 7
print("list indeks[4,6,7]: ", list[4], list[6], list[7])

#Mengganti nama teman yang berada di list 3, 5, 9
print("Nama pada indeks[3,5,9]: ", list[3], list[5], list[9])
list[3] = "Rio"
list[5] = "Ojat"
list[9] = "Hani"
print("Nama baru pada indeks[3,5,9]: ", list[3], list[5], list[9])

#Mambahkan 2 nama teman
list.append ("Candrika")
list.append ("Agus")
print("List dengan 2 nama tambahan: ", list)

#Menampilkan semua nama teman dengan perulangan
for p in list:
    print(p)

# Menampilkan panjang list
print ("Panjang list teman = ", len(list))