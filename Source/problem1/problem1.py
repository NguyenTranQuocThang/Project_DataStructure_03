from re import I


def sqrt(number):
    if number <= 1:
        return number
    begin = 0
    end = number
    while begin <= end:
        middle = (begin + end) // 2
        middle_expo = middle**2
        if middle_expo == number:
            return middle
        elif middle_expo < number:
            begin = middle + 1
        else:
            end = middle - 1
    return -1


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

print("Pass" if (9 == sqrt(81)) else "Fail")
print("Pass" if (10 == sqrt(100)) else "Fail")
print("Pass" if (-1 == 0) else "Fail")
