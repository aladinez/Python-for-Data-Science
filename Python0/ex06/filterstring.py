import sys
from ft_filter import ft_filter


def main():
    args = sys.argv[1:]
    if len(args) != 2 or not args[1].isdigit():
        print("AssertionError: the arguments are bad")
        return
    min_len = int(args[1])
    words = args[0].split()
    print([word for word in ft_filter(lambda x: len(x) > min_len, words)])


if __name__ == '__main__':
    main()
