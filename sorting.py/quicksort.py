#quicksort sort:
#time:O(n log n)
#space:0(logn)
arr=[1,8,-1,44,-1,5,3,-3,9,6,2,7]

def quicksort(arr):
    n=len(arr)
    
    if n<=1:
        return arr
    
    pivot=arr[-1]
    
    left_arr=[x for x in arr[:-1] if x<=pivot]
    right_arr=[y for y in arr[:-1] if y>pivot]
    
    left_arr=quicksort(left_arr)
    right_arr=quicksort(right_arr)
    return left_arr + [pivot] + right_arr
    
print(quicksort(arr))