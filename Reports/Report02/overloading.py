#there is no overloading in python
class Human:
    def eat(self):
        print("Meat")
    def eat(self,str):
        print(str)
class Mammal:
    def eat(self):
        print("Grass")
class Employee(Human,Mammal):
    pass
emp=Employee()
emp.eat()#if run without parameter so it will raise error missing 1 argument, so only useable method will be the last with that name