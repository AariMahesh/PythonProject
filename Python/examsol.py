l=[('mah123','2kuhvd71'),('93h0e','0187y3nkp')]
l1=[]
for i in l:
    for j in i:
        for k in j:
            if(k.isdigit()):
                if(int(k)%2==0):
                    l1.append(int(k))


print(l1)
l2=[]
for i in range(2):
    for j in range(2):
        l2.append(tuple(input()))
print(l2)
