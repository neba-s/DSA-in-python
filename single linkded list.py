class singlylinked():
    def __init__(self,value):
        self.value=value
        self.next=None

head=singlylinked(1)
b=singlylinked(2)
c=singlylinked(2.5)
d=singlylinked(3)
tail=singlylinked(4)

head.next=b
b.next=d
d.next=tail
c.next=b.next
b.next=c



def display(head):
    curr=head
    elem=[]
    while curr:
        elem.append(str(curr.value))
        curr=curr.next
        
    print("-->".join(elem))
    
def search(head,target):
    curr=head
    counter=0
    
    while curr:
        counter+=1
        if curr.value==target:
            print(f"it is found on the {counter} of the list.")
            return
        curr=curr.next
              
    print("sorry, sir, we have not found such type of number.")
        

display(head)
search(head,2.5)