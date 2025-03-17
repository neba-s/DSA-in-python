#merg sort:
#time:O(n log n)
#space:0(n)
arr=[1,8,-1,44,-1,5,3,-3,9,6,2,7]

def mergesort(arr):
    n=len(arr)  
    if n==1:
        return arr
    m = len(arr)//2
    left_arr=arr[:m]
    right_arr=arr[m:]
    
    left_arr=mergesort(left_arr)
    right_arr=mergesort(right_arr)
    l,r=0,0
    
    left_len=len(left_arr)
    right_len=len(right_arr)

    sorted_arr = [0] * n
    i=0
    
    while l<left_len and r<right_len:
        if left_arr[l]<right_arr[r]:
            sorted_arr[i]=left_arr[l]
            l+=1
        else:
            sorted_arr[i]=right_arr[r]
            r+=1
        i+=1

    if l<left_len:
        sorted_arr[i]=left_arr[l]
        l+=1
        i+=1
        
    if r<right_len:
        sorted_arr[i]=right_arr[r]
        r+=1
        i+=1    
    return sorted_arr

print(mergesort(arr))
        
        
        
        
        
        
            
        
    
    
    
    
    
    