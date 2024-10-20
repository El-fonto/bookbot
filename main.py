def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    words = count_words(text)
    characters = count_characters(text)
    print(f"this is the # of words in {book_path}: {words}")
    print(f"this are the characters:{characters}")

def get_book_path(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # to save things
    characters = {

    }
    # revisar variables aquí. Tienen una lógica incompleta. Es necesario, primero separar en palabras y separar el texto en palabras y luego en caracteres y después hacer un pretty print de lo que quiero.
    lowered_text = text.lower().split()

    for word in lowered_text:
        if word in characters:
            characters[word] += 1
        else:
            characters[word] = 1

    return characters
    # TODO - split in characters with a for loop to iterate over a big string
    


main()
