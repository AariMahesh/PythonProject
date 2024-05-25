class Demo:
    x=1000 #static/class
    def __init__(self):
        print('inside constructor');
        self.name='mahi' #instance
        print(Demo.x)
    def disp(self):
        print('inside disp')
        a=500  #local
print(Demo.x)
d1=Demo()
print(d1.x)
d2=Demo()
print(d2.x)
