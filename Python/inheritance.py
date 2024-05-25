#single inheritance
class Demo:
    def __init__(self):
        self.x=100
    def disp(self):
        print('single inheritance')
class Demo1(Demo):
    pass
d2=Demo1()
d2.disp()
print(d2.x)
#hireracial inheritance
class A:
    def __init__(self):
        self.x=100
    def disp(self):
        print('hirerical inheritance')
class B(A):
    pass
class C(A):
    def __init__(self):
        self.y=200
    def disp(self):
        print('hirerical inheritance')
c=C()
#print(c.x) #error

#multilevel

class D:
    def __init__(self):
        self.x=100
    def disp(self):
        print('multilevel inheritance')
class D2(D):
    def __init__(self):
        self.y=100
    def disp1(self):
        print('multilevl inheritance')
class D3(D2):
    def __init__(self):
        self.z=100
    def disp2(self):
        print('multilevel inheritance')
d=D3()
print(d.z)
d.disp1()
    
