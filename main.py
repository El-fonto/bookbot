def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    words = count_words(text)
    print(text)
    print(f"this is the # of words in {book_path}: {words}")

def get_book_path(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)
    


main()
