from stats import   count_words, char_text


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    number = count_words(book_text)
    characters = char_text(book_text)
    print(f"Found {number} total words.")
    print(f"{characters}")

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


main()
