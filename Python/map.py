from functools import *
li=[1,2,3,4]
sq=list(map((lambda a:a**2),li))
print(sq)
o=reduce((lambda a,b:a*b ),li)
print(o)

