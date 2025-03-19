#the program that find all the sbset of a given arrey using recurssive backtraking


sol=[]
curr=[]
i=0
def subset(curr,arr,i):
    
    if i==len(arr):
        sol.append(curr)
        return
    subset(curr,arr,i+1)
    subset(curr+[arr[i]],arr,i+1)

    return sol
          
arr=[1,2,3] #all subset are [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
print(subset(curr,arr,i))

