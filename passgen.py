import random
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
from random import choice
def passgen():
    str1=""
    chara = ascii_lowercase+ascii_uppercase+digits+punctuation
    l1 = random.choices(chara,k=8)
    for x in l1:
        str1+=x
    return str1
print(passgen())