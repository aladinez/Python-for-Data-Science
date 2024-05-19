import sys


def morse_encoder(str):
    '''
    This function takes a string as input and returns the morse code.
    '''
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. "}
    str = str.upper()
    encoded = ""
    for char in str:
        encoded += NESTED_MORSE[char]
    return encoded


def main():
    '''This is the main function of the module.'''
    args = sys.argv[1:]
    if len(args) != 1:
        print("AssertionError: the arguments are bad")
        return
    try:
        print(morse_encoder(args[0]))
    except KeyError:
        print("AssertionError: the arguments are bad")
        return


if __name__ == '__main__':
    main()
