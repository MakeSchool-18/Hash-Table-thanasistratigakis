import sys
import re
import tokenize

with open('shakespear.txt', 'r') as corpus:
    corpus = corpus.read()

clean_corpus = re.findall("\n *[A-Z][A-z]+\. (.+)", corpus)

clean_string = ' '.join(clean_corpus)

print(tokenize.tokenize(clean_string))
