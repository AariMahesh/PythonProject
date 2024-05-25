Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(4,2,-1):
...     for j in range(4,2,-1):
...         if(i==j):
...             print(i,end=" ")
...         else:
...             print(" ",end=" ")
