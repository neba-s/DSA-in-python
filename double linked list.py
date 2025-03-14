class doublelink():
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
        
head=doublelink(44)
e2=doublelink(66)
tail=doublelink(88)

head.next=e2
e2.prev=head
e2.next=tail
tail.prev=e2

def diplay(head):
    curr=head
    elems=[]
    
    while curr:
        elems.append(str(curr.val))
        curr=curr.next
        
    print("<-->".join(elems))
    
def insert(head,target):
    new_node=doublelink(target)
    new_node.next=head
    head.prev=new_node
    return new_node
head=insert(head,33)
head=insert(head,1)
    
diplay(head)
    


        