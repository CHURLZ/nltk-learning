import nltk
import re
from nltk.corpus import brown

print(__file__)
#h4ck3rt3xt

words = brown.words()[:1000]
rules = [
    ('^s', '$'),
    ('\Bs\B', '5'),
    ('[aA]', '4'),
    ('[eE]', '3'),
    ('[iI]', '1'),
    ('[oO]', '0'),
    ('[tT]', '7'),
]

def fold(rules, text):
    if not rules:
        return text
    return fold(rules[1:], re.sub(rules[0][0], rules[0][1], text))


text = ' '.join(words)
text += ' satan'
print(fold(rules, text))
