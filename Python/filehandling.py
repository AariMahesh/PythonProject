'''f1=open('text1.txt','r')
print(f1.read())'''
f2=open('text1.txt','w')
f2.write("hello from file handling in python")
f2.close()
f3=open('text1.txt','r')
print(f3.read())
f3.close()
f4=open('text1.txt','a')
f4.write(' python is amazing language')
f4.close()
f5=open('text1.txt','r')
print(f5.read())
'''coping content from file1 to file2'''
r1=open('text1.txt','r')
r2=open('text2.txt','w')
for i in r1:
    r2.write(i)
r2.close()
r3=open('text2.txt','r')
print(r3.read())
