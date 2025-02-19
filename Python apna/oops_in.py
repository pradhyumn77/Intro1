# init function is a constructor
# default constructor:
def __init__(self):
    pass
# parameterized constructor ,it consists of constructor
class student:
    def __init__(self,name,marks):
        self.name= name
        self.marks=marks

s1=student("Karan",88)   
s2=student("Piyush",90) 
print(s1.name,s1.marks)  
print(s2.name,s2.marks)

