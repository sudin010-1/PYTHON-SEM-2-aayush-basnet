sentence = input("Enter a sentence: ")

sentence = sentence.lower()
words = sentence.split()

count = {}
for w in words:
    if w in count:
        count[w] = count[w] + 1
    else:
        count[w] = 1

for w in count:
    print(w, ":", count[w])
