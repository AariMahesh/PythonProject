class Calculator:
    def calculate(self,a,b):
        return self.a+self.b
class Add(Calculator):
    def calculate(self,a,b):
        return self.a+self.b
class Sub(Calculator):
    def calculate(self,a,b):
        return self.a-self.b
class Mul(Calculator):
    def calculate(self,a,b):
        print(a*b)
class Div(Calculator):
    def calculate(self,a,b):
        return self.a/self.b
res=Mul()
res.calculate(20,20)
