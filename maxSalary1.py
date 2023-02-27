"""
In this solution I interpreted the question as the largest possible number. 
Instead they are looking for the largest number from each of the integers. 
They do not want you to separate the integers and treat them as separate

I would like to split the integers and then append them to a list 
Once that is done then I will sort them in descending order 
and take the list and convert it to a single integer by first converting it
into a string then joining the string and converting back to an int 

"""
from itertools import permutations


def largest_number_naive(numbers):
    maxList=[]
    for i in numbers: 
        string= str(i)
        for i in string:
            maxList.append(int(i))
    maxList.sort(reverse=True)
    stringList = [str(i) for i in maxList]
    finalInt = int("". join(stringList))
    return finalInt


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))



