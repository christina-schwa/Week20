#!/usr/bin/env python 3

'''1.	Write a python program (not a Jupyter notebook, but a py file you run from the command line) 
that accepts the cats_txt.txt file as input and counts the frequency of all words and punctuation 
in that text file, ordered by frequency. Make sure to handle capital and lowercase versions of words 
and count them together.'''

from nltk.tokenize import wordpunct_tokenize
from collections import Counter

cats_txt = open('cats_txt.txt', 'r')
with open('cats_txt.txt', 'r') as cats_txt:
     cats = cats_txt.read()
cats.replace("\n", " ")
lc_cats = cats.lower()
tokens = wordpunct_tokenize(lc_cats)
counter = Counter(tokens)
print(counter)

# I cannot get this to run in Terminal, even with the "chmod 755" command.
# It only runs in VS Code when I run the debugger, but it doesn't tell me what's wrong or how to fix it.
# I tested this code inJupyter Notebook, and it ran perfectly.