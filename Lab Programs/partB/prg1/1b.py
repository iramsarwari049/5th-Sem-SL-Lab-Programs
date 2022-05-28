#Write a python program to count the frequency of words in a given file.
import pprint
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :")
pprint.pprint(word_count("prg1/test.txt"))