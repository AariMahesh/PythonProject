l=[2,4,2,4,2,3,1]
print(l[::])
print(l[::-1])
res=iter(l)
while True:
    try:
        print(next(res))
    except:
        break
