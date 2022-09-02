I base in binary search to find sqrt

Firstly I have base condition :number < = 1 -> return it self
I will start from 0 to number in argument
i will get middle position and check value of exponential this location greater than or equal or lower than requirement
-> If equal -> i return
-> If greater than -> i find in left
-> If lower than -> i find in right

Time Complexity is : O(log(n))
Space Complexity is : O(1)

Base(Binary search)
