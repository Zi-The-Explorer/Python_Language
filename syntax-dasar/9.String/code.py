# mengakses nilai dalam string
name = 'John Doe' 
message = "John Doe belajar bahasa python di Belajarpython"
print ("name[0]: ", name[0])
print ("message[1:4]: ", message[1:4])


# Mengupdate string
message = 'Hello World'
print ("Updated String :- ", message[:6] + 'Python')


# String multi line
kutipantiga = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (kutipantiga)