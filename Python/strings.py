s='Mahi'
c='Mahi'

if(s==c):
    print('Equal')
else:
    print('not equal')
s=s.upper()
c=c.upper()
if(id(s)==id(c)):
    print('ids are equal')
else:
    print('ids are not equal')
age=23
print('{} is my friend, and his age is {}'.format(s,age))


          
