# wc_tool

# ccwc - Count Bytes, Lines, Words, or Characters in a File

## Description
`ccwc` is a command-line tool that allows you to count the number of bytes, lines, words, or characters in a file. It provides options to specify which count to output, and it supports both file input and reading from standard input.
Solution to [Coding Challenges - wc](https://codingchallenges.fyi/challenges/challenge-wc/)


## Installation
1. Clone this repository
2. Navigate to the directory
3. pipenv install

python ccwc.py [-c] [-l] [-w] [-m] [filename]

markdown
Copy code

### Options
- `-h, --help`: Show the help message and exit.
- `-c`: Output the number of bytes.
- `-l`: Output the number of lines.
- `-w`: Output the number of words.
- `-m`: Output the number of characters.
- `filename`: Input file name. If not provided, reads from standard input.

## Examples

1. Count bytes in a file:
python ccwc.py -c test.txt
output: 342190 test.txt


2. Count lines in a file:
python ccwc.py -l test.txt
output: 7145 test.txt



3. Count words in a file:
python ccwc.py -w test.txt
Output: 58164 test.txt


4. Count characters in a file:
python ccwc.py -m test.txt
Output: 339292 test.txt

5. Without any flag (Gives lines, words and bytes):
python ccwc.py test.txt
7145 58164 342190 test.txt

6. Read from standard input if no file name provided:
cat test.txt | python ccwc.py
7145 58164 342190

7. To run tests
pipenv run test

   


