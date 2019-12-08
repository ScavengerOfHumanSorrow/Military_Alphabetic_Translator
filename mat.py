from gtts import gTTS   # Google Text To Speech module
import os
import time
language = "en"
print("""
##############################################
#       Military Alphabetic Translator       #
#     Written by: ScavengerOfHumanSorrow     #
#            Date: 22.11.2019 -              #
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
    "/": "Slash",
    "\\": "Backslash",
    ".": "Period",
    ",": "Comma",
    ";": "Semicolon",
    ":": "Colon",
    "-": "Dash"
}
ttsout = []
while True:
    text = input("\nEnter your text here or type qqq to quit program: ").upper().strip().split()
    if text == ["QQQ"]:
        print("Bye!")
        time.sleep(2)
        break
    else:
        for word in text:
            output_text = ""
            temp_text = word
            print(f'\n{temp_text}: ')
            ttsout.append(f"{temp_text} is ")
            for letter in temp_text:
                output_text += military_alphabet.get(letter, "n/a") + " "
            ttsout.append(output_text)
            print(f'{output_text}')
        output = gTTS(text=str(ttsout), lang=language, slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")
        ttsout = []
