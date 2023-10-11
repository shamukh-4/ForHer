def count_word_frequency(sentence):
    word_frequency = {}
    words = sentence.split()

    for word in sentence:
        cleaned_word = word.strip('.,?/').lower()
        word_frequency[cleaned_word] = word_frequency.get(cleaned_word, 0) + 1
    return word_frequency

sentence = "This is a simple example of a sentence to test if a function is working."

outcome = count_word_frequency(sentence)
print("Word Frequency: ")
for word, frequency in outcome.items( ):
    print(f"{word}: {frequency}")