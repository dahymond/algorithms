'''
def finder(arr1, arr2):
  
    #Sort the arrays
    arr1.sort()
    arr1.sort()

    for num1, num2 in zip(arr1 , arr2):
        if num1 != num2:
            return num1
    
    return arr1[-1]    
            '''

#linear approach 


import collections

def finder(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] ==0:
            return num

        else:
            d[num] -= 1   
