def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr)/2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        #index of the lefthalf 
        i = 0
        
        #index of the righthalf
        j = 0

        #index of the whole array
        k = 0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]

                i += 1

            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

arr = [2,1,6,3,2,7,5,1,9,4]
merge_sort(arr)

print arr         
            

