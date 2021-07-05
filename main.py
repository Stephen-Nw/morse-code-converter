MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', 1: '.----', 2: '..---', 3: '...--', 4: '....-', 5: '.....',
              6: '-....', 7: '--...', 8: '---..', 9: '----.'}


def text_to_morse_code_converter():
    """Takes a text and converts it to Morse Code"""
    converted_sentence = ""
    sentence = input("Enter your sentence: \n")
    sentence = sentence.upper()
    for char in sentence:
        if char == ' ':
            converted_sentence += "  "
        else:
            try:
                morse_char = MORSE_CODE[char]
            except KeyError as error_message:
                try:
                    log_file = open("error_log.txt", "a")
                except FileNotFoundError:
                    log_file = open("error_log.txt", "w")
                    log_file.write(f"{char} is not an acceptable character\n")
                    print(f"{error_message} is an invalid character")
                else:
                    log_file.write(f"{char} is not an acceptable character\n")
                    print(f"{error_message} is an invalid character")
                finally:
                    log_file.close()
            else:
                converted_sentence += morse_char
    print(converted_sentence)


text_to_morse_code_converter()
