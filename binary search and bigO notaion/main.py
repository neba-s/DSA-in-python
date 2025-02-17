#this is a program in python that show binary search algorithm using
#the fuctioin called binary_search function that takes the sorted list and and an item of of the list as an argument

def binary_search(list,item):
    low=0
    high=len(list)-1 #to find the amount of element the list has. we subtract 1 from it because in arrey the indext start form 0 nor from 1
    
    while low<=high:#the loop that controls the amount of step or operation that it take the algorith.it stop when low is greater than high
        mid=(low+high)//2
        guess=list[mid]
        
        if guess==item:
            return mid # mid is the position of the item if we found our guss is our item ,and if it is found the return breaks and stops the loop
        elif guess<item:
            low=mid+1# update the low value. and we add one because we have already know that mid is not the item, so we remove it and go to up one step from the mid.and that will be our new low  
        else:
            high=mid-1# update the high value if guess is greater than the item . we already know that mid is not the item ,so we remve it then go to down one stop from the mid, and that will be our new high
    return None #if the loop fully complited ,this mean there is no element we want to find on the list,so it will print NONE
        
my_list=[2,3,4,6,8,9]# the list must be sorted in somehow or the binary search algorithm returns NONE even if the item is in the list
item=int(input("enter the item from the list: "))
print(f"{item} is found on the index {binary_search(my_list,item)}")#call the fuction to print the index