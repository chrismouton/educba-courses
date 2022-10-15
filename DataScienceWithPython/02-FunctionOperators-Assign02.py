# Assignment: GEt a signle string from 2 given strings
# seperated by a space and swap the first 2 char of each string
#John Mishal = Mihn Joshal

def main():
    two_words = input("Please enter two words (your name and surname are good examples): ")

    words = two_words.split()

    temp = words[0][0:2]
    
    formatted_word = words[1][0:2] + words[0][2:] + " " + temp + words[1][2:]

    print(f"The reformated word is now: {formatted_word}")

if __name__ == '__main__':
    main()