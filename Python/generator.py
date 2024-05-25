def paly():
    yield 100
    print("hello")
    yield 200
score=paly()
print(next(score))
print(next(score))
max=paly()
print(next(max))
def fibpnaci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
    
    
sco=fibpnaci()
print(next(sco))
for i in range(5):
    print(next(sco))

