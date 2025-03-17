#insertion sort:
#time:O(n**2)
#space:0(1)
arr=[1,8,-1,44,-1,5,3,-3,9,6,2,7]

def bubble_sort(arr):
    temp=arr[:]
    n=len(temp)
    notdone=True
    while notdone:
        notdone=False
        for x in range(1,n):
            if temp[x-1]>temp[x]:
                notdone=True
                temp[x-1],temp[x]=temp[x],temp[x-1]
    print(f"using bubble sort:{temp}")

bubble_sort(arr)
    

                
                
            
        