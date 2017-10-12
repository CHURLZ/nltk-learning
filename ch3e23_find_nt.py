import nltk
import re
from nltk.corpus import brown

print(__file__)
#grab all the n'ts!

words = brown.words()
unique_words = set(brown.words())
print('words:', len(words))
print('unique_words:', len(unique_words))
print('diversity(lower is better):{:.3f}'.format(len(unique_words) / len(words)))

pattern = r'(\w+)(n\'t)'
all_the_nts = re.findall(pattern, ' '.join(words).lower())
print(set(all_the_nts))
print(len(set(all_the_nts)), ' n\'ts found in brown corpus!')
