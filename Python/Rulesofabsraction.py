from abc import ABC,abstractmethod
#Rules of Abstraction:
'''In python we can create an object for abstract class if an abstract class does not contain any method.'''
class Student(ABC):
        pass
    
s1=Student()
class Student1(ABC):
    def disp(self):
        print("inside disp method")
s2=Student1()
s2.disp()
class Student2(ABC):
    def disp(self):
        print("inside disp method")
    @abstractmethod
    def disp(self):
        pass
class Detsils(Student2):
        pass
s3=Detsils()
ss.disp()
class Student3(ABC):
    def disp(self):
        print("inside disp method")
    @abstractmethod
    def disp1(self):
        pass
    def disp2(self):
        pass
    
class Detsils1(Student3):
        def disp1(self):
                print("hello")
        def disp2(self):
                print("welcome")
s4=Detsils1()
s4.disp1()
