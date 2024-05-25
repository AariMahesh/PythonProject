#static variables and methods and class methods
class demo:
    age=20
    def __init__(self):
        self.name="mahesh"
        demo.gender="male"
    @staticmethod
    def static_method():
        demo.color="white"
    @classmethod
    def class_method(cls):
        demo.studyclass=10
        cls.group="general"
print(demo.age)
demo()
print(demo.gender)
demo.static_method()
print(demo.color)
demo.class_method()
print(demo.studyclass)
print(demo.group)
