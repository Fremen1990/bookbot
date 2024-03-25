path_to_file="books/frankenstein.txt"


def count_letters(s):
    # Initialize an empty dictionary
    letter_count = {}

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the letter to lowercase to ensure case-insensitivity
            char = char.lower()

            # If the letter is already in the dictionary, increment its count
            if char in letter_count:
                letter_count[char] += 1
            # If the letter is not in the dictionary, add it with a count of 1
            else:
                letter_count[char] = 1

    return letter_count


with open(path_to_file) as bookText:
    file_contents=bookText.read()

    # print(file_contents)

    # words = file_contents.split()
    # print(len(words))

    # // create dictionary which will count number of each letter in the provided string

    letter_counts = count_letters(file_contents)
    print(letter_counts)