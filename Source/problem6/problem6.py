import random


def get_min_max(ints):
    min = ints[0]
    max = ints[0]
    for i in ints:
        if min > ints[i]:
            min = ints[i]
        if max < ints[i]:
            max = ints[i]
    return min, max


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
