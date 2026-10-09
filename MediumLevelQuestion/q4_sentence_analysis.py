# 4. Sentence Analysis

sentence = input("Enter a sentence: ")

# Remove unnecessary spaces and convert to lowercase
clean_sentence = " ".join(sentence.split()).lower()
words = clean_sentence.split()

print("Cleaned sentence:", clean_sentence)
print("Total number of words:", len(words))
print('Number of times "python" appears:', words.count("python"))

if words:
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)
else:
    print("Longest word: (sentence is empty)")
