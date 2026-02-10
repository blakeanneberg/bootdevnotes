from stats import   count_words

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    number = count_words(book_text)
    print(f"Found {number} total words")

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


main()
