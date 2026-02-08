def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print(book_text)


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


main()
