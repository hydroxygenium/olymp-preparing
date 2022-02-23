from array import array
from collections import Counter

word = array('B', input('word: ').encode())

def count_subpalindroms(s: str) -> int:

    numof_letters = Counter(s)

    counter = len(s)

    while s:
        first_letter = s[0]
        last_letter = s[-1]

    return counter

print(29876543 % count_subpalindroms(word))
