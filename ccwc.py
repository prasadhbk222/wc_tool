import argparse

def count_bytes(filename):
    try:
        with open(filename, 'rb') as file:
            byte_count = len(file.read())
            return byte_count
    except IOError:
        return "ccwc: {}: No such file or directory".format(filename)

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    except IOError:
        return "ccwc: {}: No such file or directory".format(filename)

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            word_count = sum(len(line.split()) for line in file)
            return word_count
    except IOError:
        return "ccwc: {}: No such file or directory".format(filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ccwc - count bytes, lines, or words in a file')
    parser.add_argument('-c', action='store_true', help='output the number of bytes')
    parser.add_argument('-l', action='store_true', help='output the number of lines')
    parser.add_argument('-w', action='store_true', help='output the number of words')
    parser.add_argument('filename', type=str, help='input file name')

    args = parser.parse_args()

    if args.c:
        byte_count = count_bytes(args.filename)
        if isinstance(byte_count, int):
            print("{} {}".format(byte_count, args.filename))
        else:
            print(byte_count)
    elif args.l:
        line_count = count_lines(args.filename)
        if isinstance(line_count, int):
            print("{} {}".format(line_count, args.filename))
        else:
            print(line_count)
    elif args.w:
        word_count = count_words(args.filename)
        if isinstance(word_count, int):
            print("{} {}".format(word_count, args.filename))
        else:
            print(word_count)
    else:
        print("ccwc: please provide either -c, -l, or -w option to count bytes, lines, or words respectively")