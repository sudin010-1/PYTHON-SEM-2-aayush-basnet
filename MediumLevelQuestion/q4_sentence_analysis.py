sentence = input("Enter a sentence: ")

sentence = sentence.strip()
words = sentence.split()
sentence = " ".join(words)
sentence = sentence.lower()
words = sentence.split()

print("Sentence:", sentence)
print("Total words:", len(words))
print("Python appears:", words.count("python"), "times")

longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w

print("Longest word:", longest)
