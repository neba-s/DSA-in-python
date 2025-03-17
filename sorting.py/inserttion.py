#insertion sort:
#time:O(n**2)
#space:0(1)
arr=[1,8,-1,44,-1,5,3,-3,9,6,2,7]

def insertion_sort(arr):
    temp=arr[:]
    n=len(temp)
    for x in range(1,n):
        for y in range(x,0,-1):
            if temp[y]<temp[y-1]:
                temp[y-1],temp[y]=temp[y],temp[y-1]
            else:
                break
    
    print(temp)

insertion_sort(arr)
    
    

                