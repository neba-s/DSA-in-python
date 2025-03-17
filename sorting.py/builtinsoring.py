#what we usually do in practice
#time:O(n log n) , there are two types :in place (O(1)) and new place(O(n))

#1,inplace

arr=[1,8,-1,4,-1,5,3,-3,9,6,2,7]
arr.sort()#is a method of class list that sort the arrey in acending order
print(arr)

#2,new place
H=[1,8,-1,4,-1,5,3,-3,9,6,2,7]
sorted_H=sorted(H)
print(sorted_H)

# the other thing is soring an arrey of tuple like 

tuple_arr=[(1,2),(2,5),(-1,7),(8,9),(-3,5),(9,6),(2,4)]

sorted_tuple_arr_key=sorted(tuple_arr,key=lambda t:t[0]) #is soring the above arrey based on the key. t means any tuple
sorted_tuple_arr_value=sorted(tuple_arr,key=lambda t:t[1])
sorted_tuple_arr_value_reverse=sorted(tuple_arr,key=lambda t:t[1])#is sorting the above arrey baased on the value

print(sorted_tuple_arr_key)
print(sorted_tuple_arr_value)
print(sorted_tuple_arr_value_reverse)