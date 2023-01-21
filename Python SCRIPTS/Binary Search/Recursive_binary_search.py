from operator import indexOf
from wordsforbinarysearch import words


def textnaivesearch(list, target):
     
    for i in list:
        if i == target:
            b = indexOf(list, i)
            return f'The index is {b}'
    return -1
    


def binarysearch(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
        
    if low > high:
        return -1    
   
    midpoint = (low+high) // 2
    if list[midpoint]==target:
        return f'\nThe bs index is: {midpoint}'
        
    elif target < list[midpoint]:
        return binarysearch(list, target, low, midpoint-1) 
    else:
        return binarysearch(list, target, midpoint+1, high)



print(binarysearch(words, "bb"))
