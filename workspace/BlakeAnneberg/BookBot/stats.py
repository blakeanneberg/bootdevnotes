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

def sort_on(d):
    return d["num"]
def chars_dict_to_sorted_list(chars_dict):
    sorted_list =[]
    for ch, count in chars_dict.items():
        sorted_list.append({"char": ch, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 
