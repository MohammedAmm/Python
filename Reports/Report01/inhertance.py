#1.multiple inhertance, child class call parent classes from right to left  
class A():
    def __init__(self):
        super(A, self).__init__()
        print ("init A")
        
class B:
    def __init__(self):
        super(B, self).__init__()
        print ("init B")
        
class C:
    def __init__(self):
        super(C, self).__init__()
        print ("init C")
        
class D(C, B,A):
    def __init__(self):
        super(D, self).__init__()
        print ("init D")
#You can Class constructor from specific class by its name like : A.__init(self)
if __name__ == '__main__':
    D()
#Diamond problem
class A:
    x=5
    def __init__(self):
        print("I'm A")
        super().__init__()
    def name(self):
        print ("My name is A")
class B(A):
    x=6
class C(A):
    x=7
class D(B,C):
    pass
obj=D()
print(obj.x)#output : 6 so it call x from C first then shadow it by x from B
#2.
class Human:
    def eat(self):
        print("Meat")
class Mammal:
    def eat(self):
        print("Grass")
class Employee(Human,Mammal):
    pass
emp=Employee()
emp.eat()#output : Meat , get eat function of Mammal then shadow it with the one from Human