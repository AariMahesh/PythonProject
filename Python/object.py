class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print('employee is working');
    def paly(self):
        print('employee is playing');
s1=Employee('mahi',12)
s2=Employee('mahesh',23)
print(s1.name,s1.age)
print(s2.name,s2.age)
s1.work()
s2.paly()
