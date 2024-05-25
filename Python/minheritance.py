#mutiple inheritance
class Demo1:
    def __init__(self):
        self.x=100
        def test(self):
            print("demo1")
class Demo2:
    def __init__(self):
        self.y=300
    def test(self):
        print("demo2")
class Demo3(Demo2,Demo1):
    def __init__(self):
        self.z=600
d3=Demo3()
print(Demo3.mro())
d3.test()
