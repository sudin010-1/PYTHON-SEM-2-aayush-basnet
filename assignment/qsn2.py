text = input("Please enter a four character string: ")

a = ord(text[0]) - 32
b = ord(text[1]) - 32
c = ord(text[2]) - 32
d = ord(text[3]) - 32

a = chr(a)
b = chr(b)
c = chr(c)
d = chr(d)

print("The string capitalized is", a + b + c + d)