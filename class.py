class animal():
    def __init__(self,type,name,age):
        self.type=type
        self.name=name
        self.age=age
        
animal1=animal("dog","john",12)
animal2=animal("cat","hana",4)
animal3=animal("sheep", "dolly",6)

stk=[animal1,animal2,animal3]
print(stk[1].name)