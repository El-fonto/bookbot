def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    words = count_words(text)
    character_dict = count_characters(text)
    # print(f"this is the # of words in {book_path}: {words}")
    report = order(character_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for char, count in report:
        print(f"The {char} character was found {count} times")
    # print(f"these are the characters:{characters}")
    print(f"--- End report---")

def order(dict):
    letters = []
    for char, repeats in dict.items():
        if char.isalpha():
            letters.append((char, repeats))
    # sort first, before returning the list
    letters.sort(key=lambda item: item[1], reverse=True) 
    return letters


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # to save things
    characters = {}

    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters
    
def get_book_path(path):
    with open(path) as f:
        return f.read()

main()
