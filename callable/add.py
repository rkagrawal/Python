class add:

    def __call__( self, a, b ):
        return (a + b )


if __name__ == "__main__":
    mya = add()
    print( mya( 5, 6 ) )
