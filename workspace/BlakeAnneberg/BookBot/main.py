import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import   count_words, char_text, chars_dict_to_sorted_list


def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    number = count_words(book_text)
    characters = char_text(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(characters)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {number} total words.")
    print(f"--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

main()
