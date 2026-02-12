def count_words(book_text):
    words = book_text.split()
    return len(words)

def char_text(book_text):
    characters = {
            }
    for letter in book_text:
        letter = letter.lower()
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters
