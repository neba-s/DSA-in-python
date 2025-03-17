#insertion sort:
#time:O(n**2)
#space:0(1)
arr=[1,8,-1,44,-1,5,3,-3,9,6,2,7]

def selection_sort(arr):
    temp=arr[:]
    n=len(arr)
    for x in range(n):
        min_index=x
        for y in range(x+1,n):
            if temp[min_index]>temp[y]:
                min_index=y
        temp[x],temp[min_index]=temp[min_index],temp[x]
    print(temp)

selection_sort(arr)
                

    