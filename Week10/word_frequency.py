def word_frequency(sentence):
    words = sentence.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    return word_counts
sentence = input("Enter a sentence: ")
result = word_frequency(sentence)
for word in result:
    print(word, ":", result[word])