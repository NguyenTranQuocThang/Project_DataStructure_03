
def rotated_array_search(input_list, number):
    start_point = 0
    end_point = len(input_list) - 1
    point_rotate = find_rotate_point(input_list, start_point, end_point)

    if point_rotate != -1:
        if input_list[point_rotate] == number:
            return point_rotate
        elif input_list[point_rotate] < number:
            return -1
        elif input_list[point_rotate] > number and input_list[end_point] < number:
            end_point = point_rotate - 1
        else:
            start_point = point_rotate + 1

    while(start_point <= end_point):
        middle = (start_point + end_point) // 2
        if(input_list[middle] == number):
            return middle
        elif(input_list[middle] > number):
            end_point = middle - 1
        else:
            start_point = middle + 1
    return -1


def find_rotate_point(input_list, begin_point, end_point):
    if begin_point > end_point:
        return -1
    if end_point == begin_point:
        return begin_point

    pivot = (begin_point + end_point) // 2

    if(pivot < end_point and input_list[pivot] > input_list[pivot + 1]):
        return pivot

    if(pivot > begin_point and input_list[pivot] < input_list[pivot - 1]):
        return pivot - 1

    if input_list[begin_point] < input_list[pivot]:
        return find_rotate_point(input_list, pivot + 1, end_point)
    else:
        return find_rotate_point(input_list, begin_point, pivot - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


test_function([[2, 3, 4, 5, 6, 0, 1], 0])
test_function([[2, 3, 4, 5, 6, 0, 1], 1])
test_function([[2, 3, 4, 5, 6, 0, 1], -1])

test_function([[], -1])
