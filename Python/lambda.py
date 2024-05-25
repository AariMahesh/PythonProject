s=lambda a,b:a//b
print(s(2,1))
ev=lambda a:"even" if a%2==0 else "odd"
print(ev(5))
li=[1,2,3,4,5]
even=[]
def check(li):
    for i in li:
        if i%2==0:
            even.append(i)
check(li)
print(even)
ev_l=list(filter((lambda i:i%2==0),li))
print(ev_l)

