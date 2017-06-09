if __name__ == "__main__":
    s = set()
    # with set it would take it as tuple
    t = set( ['x','a','b','c'] )
    s.add('e')
    s.add('f')
    s.add('d')
    s.add('x')
    print(s)
    print(t)
    print ( "union:", s|t )
    print ( "intersection :", s&t )
    print ( "difference :", s-t )
