from turtle import right


def rearrange_digits(input_list):

    input_list = merge_sort(input_list)

    num1 = ''
    num2 = ''

    first = True

    for i in range(len(input_list)-1, -1, -1):
        if first:
            num1 += str(input_list[i])
            first = False
        else:
            num2 += str(input_list[i])
            first = True
    return int(num1), int(num2)


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    merge = []
    point_left = 0
    point_right = 0
    while point_left < len(left) and point_right < len(right):
        if left[point_left] < right[point_right]:
            merge.append(left[point_left])
            point_left += 1
        else:
            merge.append(right[point_right])
            point_right += 1
    merge += left[point_left:]
    merge += right[point_right:]
    return merge


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
