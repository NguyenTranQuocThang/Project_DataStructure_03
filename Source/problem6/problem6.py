import random


def get_min_max(ints):
    min = ints[0]
    max = ints[0]
    for i in ints:
        if min > i:
            min = i
        if max < i:
            max = i
    return min, max


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 100)]  # a list containing 0 - 99
random.shuffle(l)
print("Pass" if ((0, 99) == get_min_max(l)) else "Fail")

l = [i for i in range(1, 9)]  # a list containing 1 - 8
random.shuffle(l)
print("Pass" if ((1, 8) == get_min_max(l)) else "Fail")
