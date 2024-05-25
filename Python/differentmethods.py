#understanding of inherited ovverriden specialized
class Student:
    def study(self):
        print("student studying")
    def listen(self):
        print("student listening")
class Friend(Student):
    pass
f=Friend()
f.listen()
#overriding, and overriden methods are special methods
class Student1:
    def study(self):
        print("student studying")
    def listen(self):
        print("student listening")
class Friend1(Student1):
    def study(self):
        print("friend studying")
    def listen(self):
        print("frienf listening")
f1=Friend1()
f1.listen()

#method chaining

class GGP:
    def cook(self):
        print("GGP is cooking")
class Gp(GGP):
    def cook(self):
        print("GP is cooking")
        super().cook()
class P(Gp):
    def cook(self):
        print("P is cooking")
        super().cook()
    
class C(P):
    def cook(self):
        print("C is cooking")
        super().cook()
        super.P.self().cook()
c=C()
c.cook()
