path_to_file="books/frankenstein.txt"

def count_letters(s):
    letter_count = {}

    for char in s:
        if char.isalpha():
            char = char.lower()

            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count


with open(path_to_file) as bookText:
    file_contents=bookText.read()

    words = file_contents.split()

    letter_counts = count_letters(file_contents)

    # print(letter_counts.items())

    letter_counts_list_sorted = sorted(letter_counts.items())

print("--- Begin report of books/frankenstein.txt ---")
print(f'{len(words)} words found in the document\n')

for letter in letter_counts_list_sorted:
    print(f'The "{letter[0]}" character was found {letter[1]} times')

print('--- End report ---')
