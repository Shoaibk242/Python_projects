from random import randint
def randgen():
    x=randint(100,999)
    if (x % 5) != 0:
        while (x % 5) != 0:
            x=randint(100,999)
    y=randint(100,999)
    if (y % 5) != 0:
        while (y % 5 ) != 0:
            y=randint(100,999)
    z=randint(100,999)
    if (z % 5) != 0:
        while (z % 5) != 0:
            z=randint(100,999)
    return x,y,z
print(randgen())