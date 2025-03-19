class tree:
    def __init__(self,value):
        self.value=value
        self.naghi=[]
        
    def display(self):
        connections=[node.value for node in self.naghi]
        
        print(f"{self.value}---->{connections}")

A=tree("A")
B=tree("b")
C=tree("c")
D=tree("d")

A.naghi.append(B)
A.naghi.append(C)
B.naghi.append(A)
B.naghi.append(C)
B.naghi.append(D)
C.naghi.append(A)
C.naghi.append(B)
D.naghi.append(B)

A.display()
B.display()
C.display()
D.display()


