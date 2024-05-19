def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f'The text contains {num_words} words.')

count_words("Hello, this is a demonstration text")
