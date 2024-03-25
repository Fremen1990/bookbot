path_to_file="books/frankenstein.txt"

with open(path_to_file) as bookText:
    file_contents=bookText.read()

    print(file_contents)

    words = file_contents.split()
    print(len(words))