import time
print("""
##############################################
#       Military Alphabetic Translator       #
#     Written by: ScavengerOfHumanSorrow     #
#             Date: 22.11.2019               #
##############################################
""")
military_alphabet = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Ten",
}
text = ''
while True:
    text = input("\nEnter your text here or type qqq to quit program: ").upper()
    splitted_text = text.split(" ")
    if text == 'QQQ':
        print("Bye!")
        time.sleep(2)
        break
    else:
        for word in splitted_text:
            output_text = ""
            temp_text = word
            print(f'\n{temp_text}: ')
            for letter in temp_text:
                output_text += military_alphabet.get(letter, "n/a") + " "
            print(f'{output_text}')