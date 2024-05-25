class Demo:
    def __init__(self):
        self.x=10
    def display(self):
        print(self.x)
#d1=Demo()
#d1.display()

class Demo1(Demo):
    def disp2(self):
        print(f'acess parent variable value in child class {self.x}')
d2=Demo1()
d2.disp2()
#d2.display()

#protected

class Demo2:
    def __init__(self):
        self._x=10 #protected
    def display(self):
        print(self._x)
#d1=Demo()
#d1.display()

class Demo3(Demo2):
    def disp2(self):
        print(f'acess parent variable value in child class {self._x}') #can be acessed in child
d3=Demo3()
d3.disp2()

#private
class Demo4:
    def __init__(self):
        self.__x=10
    def display(self):
        print(self.__x)
#d1=Demo()
#d1.display()

class Demo5(Demo4):
    def disp2(self):
        #print(f'acess parent variable value in child class {self.__x}') #error
        print('private variable can not be acessed in child')
d4=Demo5()
d4.disp2()
#name mangaling
class Demo6:
    def __init__(self):
        self.__x=10
    def display(self):
        print(self.__x)
d5=Demo6()
print(d5._Demo6__x)
