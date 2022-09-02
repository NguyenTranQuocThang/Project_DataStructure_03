def sort_012(input_list):
    pos_zero = 0
    pos_two = len(input_list) - 1
    position = 0
    while position <= pos_two:
        if input_list[position] == 0:
            input_list[position] = input_list[pos_zero]
            input_list[pos_zero] = 0
            pos_zero += 1
            position += 1
        elif input_list[position] == 2:
            input_list[position] = input_list[pos_two]
            input_list[pos_two] = 2
            pos_two -= 1
        else:
            position += 1
    return input_list


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

test_function([2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1])


test_function([2, 2, 2, 2, 2, 2, 2])
test_function([1, 1, 1, 1, 1, 1, 1])
test_function([0, 0, 0, 0, 0, 0, 0])
test_function([0, 1, 2, 0, 1, 2, 0])
test_function([2, 1, 0, 2, 1, 0, 0])

test_function([])
