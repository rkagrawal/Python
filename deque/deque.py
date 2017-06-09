from collections import deque
d=deque( range(1,10 ) )
print(d)
print(type(d))
 
d2=d
print(d2)

# deque assignment is not deep copy.. it is by reference

d2.rotate(5)
print (d2)
print (d)

d[1] = -d[1]
print (d)
print(d2)

l = list([1,2,3,4])
print (l)

