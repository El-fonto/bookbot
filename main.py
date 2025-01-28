def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()

        characters = character_counter(words)
        char_list = alphabet_counter(characters)
        char_list.sort(reverse=True, key=sort_on)

        # print(file_contents)
        print(f"======Report of {file_path} =====")
        print()
        for item in char_list:
            char = item["char"]
            number = item["num"]
            print(f"{char.title()} was found {number} times ")

        print()
        print(f"{len(words)} total words")
        print("======End report=====")


# it takes a list of words and returns a String -> Integer dict
def character_counter(list):
    counter_dict = {}
    joined_string = "".join(list).lower()

    for c in joined_string:
        if c in counter_dict:
            counter_dict[c] += 1
        else:
            counter_dict[c] = 1
    return counter_dict


def alphabet_counter(dict):
    alpha_list = []

    for character in dict:
        repetition = dict[character]
        if character.isalpha():
            c_dict = {"char": character, "num": repetition}
            alpha_list.append(c_dict)
    return alpha_list


def sort_on(dict):
    return dict["num"]


main()
