vowels=[i.upper() for i in 'hello' if i in 'aeiou']
print(vowels)
l=[1,2,3,4]
nl=['even' if i%2==0 else 'odd' for i in l]
print(nl)
print('123'.isdigit())
print('mahi'.isdigit())
my=['ab12','cd34','gf56']
dig=[int(j) for i in my for j in i if j.isdigit()]

print(dig)
li=['radar','racecar','python']
pal=[i for i in li if i==''.join(i[::-1])]
print(pal)

pal=[i for i in li if list(i)==list(reversed(list(i)))]
print(pal)

my_l=[1+2j,3+5j,7+9j]
op=[int(x.real)for x in my_l]
print(op)
im_o=[x.imag for x in my_l]
print(im_o)

i1=['apple','banana']
fr=['red','yellow']
cr=[(i,j) for i in i1 for j in fr]
print(cr)

ip=[3+2j,3-8j,8j,-9j]
o=[int(x.imag) for x in ip if x.imag>0]
print(o)



