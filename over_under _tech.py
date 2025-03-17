arr=[False,True,True,True,True,True]
def over_under(arr):
    left=0
    right=len(arr)-1
    while left<right:#we need to force the right or left so scape:
        mid=left+(right-left)//2
        if arr[mid]:
            right=mid
        else:
            left=mid+1
            
    return right# or return right
    
print(over_under(arr))