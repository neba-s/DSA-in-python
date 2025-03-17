from collections import deque

class binarytree():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
a , b=binarytree(5) , binarytree(1)
c , d=binarytree(8) , binarytree(-1)
e , f=binarytree(3) , binarytree(17)
g = binarytree(9)

a.left , a.right = b , c
b.left , b.right = d , e
c.left , c.right = f , g

def pre_order(node):#inorder binary search tree
    if not node:
        return
    else:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)
        
def in_order(node):#in_order binary search tree
    if not node:
        return
    else:
        in_order(node.left)
        print(node.value)
        in_order(node.right)
        
def post_order(node):#post_order binary search tree
    if not node:
        return
    else:
        post_order(node.left)
        post_order(node.right)
        print(node.value)

def pre_order_interative(node):#pre order binary search tree using iteration or loop
    stk=[node]
    while stk:
        curr=stk.pop()
        print(curr.value)
        
        if curr.right:
            stk.append(curr.right)
        if curr.left:
            stk.append(curr.left)
            
def level_order_itrative(node):#depth first search using interation 
    q=deque()
    q.append(node)
    while q:
        curr=q.popleft()
        print(curr.value)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
            
def search_linearly(node,target): #time:O(1),space:o(n)
    if not node:
        return False
    
    if node.value==target:
        return True
    
    return search_linearly(node.left,target) or search_linearly(node.right, target)

def search_recursivly(node,target):#time:O(logn),space:O(logn) or O(n)
    if not node:
        return False
    
    if node.value==target:
        return False
    
    if node.value<target:
        return search_linearly(node.right,target)
    
    if node.value<target:
        return search_recursivly(node.left,target) 
    
#now lets print all the fuction that we have made
print("pre_order")
pre_order(a)
print("___________________")

print("in_order")
in_order(a)
print("___________________")

print("post_order")
post_order(a)
print("___________________")

print("post_order_in iteration")
pre_order_interative(a)
print("___________________")

print("breadth search using interation")
level_order_itrative(a)
print("___________________")

print("lookup a value using linear search on binary search tree")
print(search_linearly(a,1))
print("____________________")

print("lookup a value using binary search on binary search tree")
print(search_recursivly(a,910))
print("____________________")

