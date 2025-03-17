#counting sort:
#time:O(k+n) k=max or arrey so if k is very small then the time will be o(n)
#space:0(k)
arr=[1,8,1,4,1,5,3,3,9,6,2,7]

def counting_sort(arr):
    n=len(arr)
    maxx=max(arr)
    counts=[0]*(maxx + 1)
    
    for x in arr:
        counts[x]+=1
        
    i=0
    for c in range(maxx +1):
        while counts[c]>0:
            arr[i]=c
            i+=1
            counts[c]-=1
    
    

counting_sort(arr)
print(arr)#cuz it automatically pass by pointer or reference 
            
    