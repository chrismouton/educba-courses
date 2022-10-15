# Assignment: Get a string froma  given string where all occurances
# of its char have been changed to a '$', except for the first char itself
# "example" where e is repated twice, therefore output shoudl be exampl$

from random import sample


def main():
    sample_word = "example"
    letter_to_replace = sample_word[0]

    print(f"The word before character '{sample_word[0]}' is replaced: {sample_word}")

    replaced_word = sample_word[0] + sample_word[1:].replace(sample_word[0], '$')

    print(f"The word after character '{sample_word[0]}' is replaced: {replaced_word}")

if __name__ == '__main__':
    main()