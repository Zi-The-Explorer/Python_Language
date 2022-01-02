# Conotoh sederhana pembuatan list di python
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [1,'a',2,'b',3,'c']


# Akses nilai dalam list
print(list1[0])
print(list2[1:4])

# Update nilai pada list
list = ['fisika', 'kimia', 1993, 2017]
print ("Nilai ada pada index 2 : ", list[2])

list[2] = 2001
print ("Nilai baru ada pada index 2 : ", list[2])

# Hapus nilai dalam list
list = ['fisika', 'kimia', 1993, 2017]

print (list)
del list[2]
print ("Setelah dihapus nilai pada index 2 : ", list)