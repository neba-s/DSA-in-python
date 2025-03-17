#bulilding a min heap(heapfy)
#Time:O(n),Space:O(1)

arr=[9,2,4,4,2,5,4,8,1,4,-2]
print(f"before heapyfing: {arr}")

from heapq import heapify , heappush , heappop,heappushpop

heapify(arr)
print(f"after   heapying: {arr}")

#heappush: Time=O(logn) and space=---
heappush(arr,-20)
print(f"after pushing -20: {arr}")

#heappop: Time=O(logn) and space=----
min=heappop(arr)#cus it is not just removing the min node from the head, but also it return the node that it removed and it take only one arrgument the list
print(f"the removed min node: {min}")
print(f"after poping: {arr}")

#heapsort: Time=O(log n), space=:O(n)

def heapsort1(arrey):
    temp=arrey[:]
    heapify(temp)#first we change it to head then we creat a new arr that store the pop value 
    n=len(arrey)
    new_list=[0]*n
    
    for i in range(n):
        minn=heappop(temp)
        new_list[i]=minn
        
    return new_list
#or you can you see something like this
def heapsort2(arrey):
    temp=arrey[:]
    heapify(temp)#first we change it to head then we creat a new arr that store the pop value 
    n=len(arrey)
    new_list=[]
    
    for i in range(n):
        minn=heappop(temp)
        new_list.append(minn)
        
    print(f"the heapsorting of the new list: {new_list}")
list1=[2,1,3,4,2,4,11,77,-2]
  

print(f"the heapsorting of the new list:{heapsort1(list1)}")
heapsort2(list1)
print("---------------------------------------------")

#heap push pop:#time:O(n) and space:O(log n)

print(f"befor push pop {arr}")
pop=heappushpop(arr, 73)
print(f"the removed node is {pop} and the inserted value is 77")
print(f"after push pop {arr}")
print("------------------------------------------------------")
#make a max heap
b=[1,6,3,-1,-6,3,8,24,2,12]
n=len(b)

print(f"before negaion: {b}")
for i in range(n):#to make max heap , we have to do that ,cuz there is no a buit in fucion to make the max heap
    b[i]=-b[i]

print(f"before heapify:{b}")
heapify(b)
print(f"after heapify: {b}")

#after this time if there is any thing we do, we have to negate it, explae to insert 6 we have to input -6. exaple
largest=-heappop(b)
print(f"after poping{b}")
heappush(b,-16)
print(f"after insering 6:{b}")
print("-----------------building a heapipy------------------------")

#lets build lets build a heapfy from a scracth:timeO(nlogn) but the built in heapify form the library heapq is time:O(n)

c=[-5,4,2,1,-7,0,3]

heap=[]
for x in c:
    heappush(heap,x)
    print(heap)
    
#putting tupel on the hip

print("---------------------------putting tupel on the hip__________________________")# importand for leetcode

from collections import Counter
d=[1,2,3,6,1,7,3,2,3,6,3,6]
counter=Counter(d)#is now a dictionay
print(d)
print(counter)
heap=[]
for k,v in counter.items():
    print(k,v)

#lets print the key value pair using loop
for key,value in counter.items():
    heappush(heap,(key,value))

print(f"now the hip is {heap} . which is assending by heap data sturucture  using the key not by value")
    










