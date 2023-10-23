with open("/Users/shamukhimran/PycharmProjects/ For Her/transcript.txt"):
    text = file.read()

words = text.split()
total_words = len(words)

total_characters = sum(len(word) for word in words)

average_word_length = total_characters / total_words

word_frequencies = {}
for word in words:
    word = word.strip('.,!?(-"').lower()
    if word not in word_frequencies:
        word_frequencies[word] = 1
    else:
        word_frequencies[word] += 1



    print(f"Total number of words: {total_words}")
    print(f"Total number of characters (excluding whitespaces): {total_characters}")
    print(f"Average word length: {average_word_length}")
    print(f"\nWord_frequencies:")
    for frequency in word_frequencies.items():
        print(f"{word}: {frequency}")

