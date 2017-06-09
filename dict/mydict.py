''' there is no method set on dict'''
''' dict is a built in.. where UserDict is from collection package '''

from types import MappingProxyType

class mydict( dict ):
    
    def __missing__ ( self, key ):
        print "calling __missing__ for key ", key
        if isinstance(key, str ):
            print "key is already a string and was not found so return error"
            raise KeyError(key)

        print "Trying with key converted to string"
        return self[str(key)]


if __name__ == "__main__":
    xyz = mydict()
    print( type(xyz) )
    xyz["1"] = 5;
    xyz["2"] = 10;
   
    print "-- trying to find \"1\" --- "
    print ( xyz["1"] )
    print "-- trying to find 2 with int as key --- "
    print ( xyz[2] )
    try: 
        print "-- trying to find \"3\" --- "
        print ( xyz["3"] )
    except:
        print "key \"3\" not found"
    
    try:
        print "-- trying to find 4 with int as key --- "
        print ( xyz[4] )
    except:
        print "key 4 not found"


    mp = MappingProxyType( xyz )
    print ( mp["2"] )
