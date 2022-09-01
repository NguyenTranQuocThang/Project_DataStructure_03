def sort_012(input_list):
    arr_zero = []
    arr_first = []
    arr_second = []

    for i in input_list:
        if i == 0:
            arr_zero.append(0)
        elif i == 1:
            arr_first.append(1)
        else:
            arr_second.append(2)
    return arr_zero + arr_first+arr_second


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
              2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
