import sys

def is_even(n):
    return n % 2 == 0

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

myList = sys.argv

if len(myList) == 1:
    pass
elif len(myList) == 2:
    if is_digit(myList[1]):
        if is_even(int(myList[1])):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")
else:
    print("AssertionError: more than one argument is provided")