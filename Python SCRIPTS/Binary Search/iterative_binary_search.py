from wordsforbinarysearch import words

def iterativebinaysearch(list, target):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first+last) // 2
        
        if list[midpoint] == target:
            return f'Index position is: {midpoint}'
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return 'None'

print(iterativebinaysearch(words, "insidious"))