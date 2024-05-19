import sys

def count_uppercase(input):
    """This function counts the number of uppercase characters in a string."""
    count = 0
    for char in input:
        if char.isupper():
            count += 1
    return count

def count_lowercase(input):
    """This function counts the number of lowercase characters in a string."""
    count = 0
    for char in input:
        if char.islower():
            count += 1
    return count

def count_punctuation(input):
    """This function counts the number of punctuation characters in a string."""
    punc_chars = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    count = 0
    for char in input:
        if char in punc_chars:
            count += 1
    return count

def count_digits(input):
    """This function counts the number of digits in a string."""
    count = 0
    for char in input:
        if char.isdigit():
            count += 1
    return count

def count_spaces(input):
    """This function counts the number of spaces in a string."""
    count = 0
    for char in input:
        if char.isspace():
            count += 1
    return count



def analyze_input(input):
    """This function takes a string as input and prints what it contains."""
    print("The text contains", len(input), "characters:")
    print(count_uppercase(input), "upper letters")
    print(count_lowercase(input), "lower letters")
    print(count_punctuation(input), "punctuation marks")
    print(count_spaces(input), "spaces")
    print(count_digits(input), "digits")


def main():
    """This is the main function of the building module. It is the entry point of the program."""
    myList = sys.argv
    try:
        assert len(myList) <= 2, "AssertionError."
        if len(myList) == 1:
            print("What is the text to count?")
            user_input = input("")
            user_input += " "
        else:
            user_input = myList[1]
        analyze_input(user_input)
    
    except (AssertionError, EOFError) as e:
        if isinstance(e, EOFError):
            analyze_input(user_input)
        else:
            print(e)
        return
        

if __name__ == '__main__':
    main()