My memo solution:
I find rotate point to reduce step for search element with binary search
if value point rotate > number && value at last element in array < number
-> find in left rotate point
else
-> find in right rotate point

In some point I can reduce case IF but it make code more complicate to understand

Describle about function:

1 find_rotate_point ( I have referenced udacity teacher's answer in a similar question )
This function use to find rotate point
I have two base cases (easy to understand)

this pivot i choose middle point

-> check if value if pivot point > value in pivot point + 1 -> point rotate
-> if value in pivot point < value in pivot point - 1 => point rotate is pivot -1

2 rotated_array_search
This function use binary search to find point

I can use that code for case list what's not rotate

so i separate case is rotate: -> handle like memo solution
else: -> just binary search normal
