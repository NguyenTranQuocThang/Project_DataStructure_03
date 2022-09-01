from re import I


def sqrt(number):
    i = 0
    while True:
        if i * i == number:
            return i
        elif i * i > number:
            return -1
        else:
            i += 1


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
