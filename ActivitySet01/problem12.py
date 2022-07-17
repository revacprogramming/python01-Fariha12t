# Regular Expressions
# https://www.py4e.com/lessons/regex
# Search for lines that start with From and have an at sign
import re
hand = open('dataset/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)