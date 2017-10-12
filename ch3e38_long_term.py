import re

s = ['It is better in the long-\nterm.', 'How awe-\nsome is that.']
long_words = re.findall('\w+-\n\w+', ' '.join(s))
assert len(long_words) == 2
print(long_words)

subbed = [re.sub('-\n', '-', x) for x in long_words]
print(subbed)
