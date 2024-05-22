import sys


def analyze_input(input):
    """This function takes a string as input and prints what it contains."""

    punc_chars = r'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    print("The text contains", len(input), "characters:")
    print(sum(1 for c in input if c.isupper()), "upper letters")
    print(sum(1 for c in input if c.islower()), "lower letters")
    print(sum(1 for c in input if c in punc_chars), "punctuation marks")
    print(sum(1 for c in input if c.isspace()), "spaces")
    print(sum(1 for c in input if c.isdigit()), "digits")


def main():
    """This is the main function of the module."""
    myList = sys.argv
    try:
        assert len(myList) <= 2, "AssertionError: more than one argument are provided"
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
