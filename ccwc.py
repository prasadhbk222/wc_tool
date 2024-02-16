import argparse
import sys


def count_bytes(byte_object: bytes):
    return len(byte_object)


def count_lines(byteObject: bytes):
    return sum(1 for ch in byteObject.decode() if ch == '\n')


def count_words(byteObject: bytes):
    return len(byteObject.decode().split())


def count_characters(byteObject):

    return len(byteObject.decode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='ccwc - count bytes, lines, or words in a file')
    parser.add_argument('-c',
                        action='store_true',
                        help='output the number of bytes')
    parser.add_argument('-l',
                        action='store_true',
                        help='output the number of lines')
    parser.add_argument('-w',
                        action='store_true',
                        help='output the number of words')
    parser.add_argument('-m',
                        action='store_true',
                        help='output the number of characters')

    parser.add_argument('filename',
                        nargs='?',
                        type=str,
                        help='input file name')

    args = parser.parse_args()
    print(args)

    if args.filename:

        with open(args.filename, 'rb') as file:
            data = file.read()

    else:

        data = sys.stdin.buffer.read()

    if args.c:
        byte_count = count_bytes(data)
        print("{} {}".format(byte_count, args.filename))

    elif args.l:
        line_count = count_lines(data)
        print("{} {}".format(line_count, args.filename))

    elif args.w:
        word_count = count_words(data)
        print("{} {}".format(word_count, args.filename))

    elif args.m:
        char_count = count_characters(data)
        print("{} {}".format(char_count, args.filename))

    elif not args.c and not args.l and not args.w and not args.m:
        line_count = count_lines(data)
        word_count = count_words(data)
        byte_count = count_bytes(data)
        print("{} {} {} {}".format(line_count, word_count, byte_count,
                                   args.filename if args.filename else ''))

    else:
        print(
            "ccwc: please provide either -c, -l, or -w option to count bytes, lines, or words respectively"
        )
