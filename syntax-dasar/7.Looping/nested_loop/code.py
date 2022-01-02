# Contoh penggunaan nested loop
# Catatan : Penggunaan modulo pada kondisional mengasumsikan nilai selain nol sebagai True(benar) dan nol sebagai false(salah)

i = 2
while i < 10:
    
    j = 2
    
    while j <= (i/j): # j <= (i/j)
        if not i%j: # i%j
            break
        j = j + 1
        
    if j > i/j:
        print(i, "is a prime number")
    i = i + 1
    
print("Good bye!")