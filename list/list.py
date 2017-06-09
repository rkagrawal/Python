import bisect
import sys

# list does not have method rotate

l = [ "Rod Steward",  "Paula Abdul", "Michael Jackson", "Eric Clapton",
                              "Jay Z", "Michale Bolton", "Bruno Mars", "Paula Abdul", 
                              "Rod Steward", "George Michael", "Elton John",  ]
print( type(l))
print "Unsorted list "
print(l)
print "sorted list "
l.sort()   # in place sorting..
print( l )

print( "Bisect the list around Michael Bolton" )
pos = bisect.bisect_left( l, "Michael Bolton" )
print (pos )
print( "List is bisected around Michael Bolton at position " , pos )

print ("reverse list is " )
l.reverse()
print( l )

t = ( "Eleanor", 1,4,5, "Rajesh" )
print (t)
print( type(t) )
print(sorted(t))
#t.sort()  // tuple has no sort method
