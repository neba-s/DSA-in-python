class linked():
    def __init__(self,value):
        self.value=value
        self.next=None
        
head=linked(1)
b=linked(3)
c=linked(5)
d=linked(7)
tail=linked(77)

head.next=b
b.next=c
c.next=d
d.next=tail
def reverseprint(head):
    if not head:
        return 
    else:
        reverseprint(head.next)
        print(head.value)
        
reverseprint(head)