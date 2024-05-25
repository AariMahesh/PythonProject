my=[100,200,300,400,500]
for ind,ele in enumerate(my):
    print(f'Element is{ele} and indes is{ind}')

#linear search
def searchele(myl,tar):
    for ind,ele in enumerate(myl):
        if ele==tar:
            return ind
    return -1
myl=sorted(list(eval(input("enter elements seperated with comma :"))))
tar=int(input())
result=searchele(myl,tar)
if result!=-1:
    print(f'Element {tar} found at index{result}')
else:
    print("element not found")
