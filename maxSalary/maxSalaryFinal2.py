from itertools import permutations
"""
Solving the question using their interpretation of the question
"""
#numbers= [21, 2]
#def largest_number_naive(numbers):
#numbers.sort(reverse=True)
#stringList = [str(i) for i in numbers]
#finalInt = int("". join(stringList))
#return finalInt

#is better(number, maxNumber):
#you want to check each digit on each other
#check if number is single digit

def isBetter(number, maxNumber):
    number = str(number)
    lengthNum= len(number)
    maxNumber = str(maxNumber)
    lengthMaxNum= len(maxNumber)
    listToCheck = []
    for i in number: 
        listToCheck.append(int(i))
    for i in maxNumber: 
        listToCheck.append(int(i))
        numberCount = 0
        maxNumCount = lengthNum
    isTrue= None
    while isTrue == None:
        if listToCheck[numberCount]> listToCheck[maxNumCount]:
            isTrue= True 
            return isTrue
        elif listToCheck[numberCount]< listToCheck[maxNumCount]:
            isTrue= False
            return isTrue
        else:
            if numberCount+1 == lengthNum and maxNumCount+1== lengthNum +lengthMaxNum:
                isTrue= True 
                return isTrue 
            elif numberCount+1 == lengthNum:
                if listToCheck[0]> listToCheck[maxNumCount+1]:
                    isTrue= True
                    return isTrue 
                else: 
                    isTrue= False 
                    return isTrue
            elif maxNumCount+1== lengthNum +lengthMaxNum: 
                if listToCheck[numberCount+1]> listToCheck[lengthNum]:
                    isTrue= True
                    return isTrue
                else: 
                    isTrue=False
                    return isTrue
            else: 
                maxNumCount +=1 
                numberCount +=1

#number = 46
#maxNumber = 465

#print(isBetter(number, maxNumber))


def largest_number_naive(numbers):
    mySalary = []
    while numbers: 
        maxNumber= 0
        for i in numbers:
            if isBetter(i, maxNumber)==True: 
                maxNumber= i
        mySalary.append(maxNumber)
        numbers.remove(maxNumber)
    stringList = [str(i) for i in mySalary]
    finalInt = int("". join(stringList))
    return finalInt

numbers = [54, 546, 548, 60]

print(largest_number_naive(numbers))

"""
if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
"""
