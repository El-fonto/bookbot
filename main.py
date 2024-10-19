def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    words = count_words(text)
    print(text)
    print(f"this is the # of words in {book_path}: {words}")
    print(f"this are the characters:")

def get_book_path(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(words):
    characters = {}
    lowered_text = words.lower()
    # TODO - split the text into characters and count with if statements add one per encounter; if not add to dictionary with a key. Similar to grocery list
    


main()
