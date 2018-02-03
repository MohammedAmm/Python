import re
class Person(object):
    moods=("happy","tired","lazy")
    def __init__(self, money,mood,healthRate):
        self.money=money
        self.mood=mood
        self.healthRate
    def sleep(self,hours):
        if hours == 7:
            self.mood= moods[0]
        elif hours < 7 and hours >0:
           self.mood=  moods[1]
        elif hours > 7:
           self.mood=  moods[2]
        else:
            self.mood= "Error"
    def eat(self,meals):
        if meals == 3:
            self.healthRate= "100%"
        elif meals == 2:
           self.healthRate=  "75%"
        elif meals == 1:
           self.healthRate=  "50%"     
    def buy(self,items):
        if item == 1:
            self.money -=10
    @property
    def healthRate(self):
        return self.__healthRate
    @healthRate.setter
    def healthRate(self, healthRate):
        if healthRate < 100 and healthRate > 0:
            self.__healthRate = healthRate
class Employee(Person):
    def __init__(self,email,salary,distanceToWork,car="Fiat 128"):
        self.car=car
        self.email=email
        self.salary=salary
        self.distanceToWork=distanceToWork
        self.c=Car()
    def work(self):
        if hours == 8:
            self.mood= moods[0]
        elif hours < 7 and hours >0:
           self.mood=  moods[2]
        elif hours > 7:
           self.mood=  moods[1]
        else:
            self.mood= "Error"
    def drive(self,distance,time):
            # while  
        self.c.run(distance,time)
    def refuel(self,gasAmount=100):
        fuelRate=gasAmount
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        if salary >= 1000:
            self.__salary = salary
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        myMail=re.match('[^@]+@[^@]+\.[^@]+',email)
        if myMail:
            self.__email = email
# class Office(object):
#     def __init__(self, name,employees):
#         self.name=name
#         self.employees=employees
#     def get_all_employees(self):
#         pass
#     def get_employee(self):
#         pass
#     def hire(self):
#         pass
#     def fire(self):
#         pass
#     def calculate_lateness(self):
#         pass
#     def deduct(self):
#         pass
#     def reward(self):
#         pass
class Car:
    def __init__(self, name="",fuelRate=100):
        self.name=name
        self.fuelRate=fuelRate
        self.distance=0
        self.velocity=0;
    def run(self,distance,time):
        self.velocity=distance/time
        self.distance=distance
        while True:
           self.fuelRate-= 10 
           self.distance-=10 
           if self.fuelRate == 0:
                self.stop()
                break;

    def stop(self):
        print ("remain :"+ str(self.distance))
    @property
    def velocity(self):
        return self.__velocity
    @velocity.setter
    def velocity(self, velocity):
        if velocity >0 and velocity <200:
            self.__velocity = velocity
    @property
    def fuelRate(self):
        return self.__fuelRate
    @fuelRate.setter
    def fuelRate(self, fuelRate):
        if fuelRate >=0 and fuelRate <=200:
            self.__fuelRate = fuelRate
emp=Employee("mohamed@m.com",1000,50)
emp.drive(110,1)
