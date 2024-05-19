def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f'The text contains {num_words} words.')

count_words("Hello, this is a demonstration text")

def count_words(text):
    words = text.split()
    num_words = len(words)
    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    print(f'The text contains {num_words} words.')
    print(f'Word frequencies: {word_frequency}')

count_words("Hello, this is a demonstration text.")
