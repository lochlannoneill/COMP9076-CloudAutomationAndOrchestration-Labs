#-------------------------------------------------------------------------------
#   COMP8062 : 2024-2025 : 
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#   Assignment #2 : The 'if' Statement
#-------------------------------------------------------------------------------

def letter_grade( percentage ) :

    # The letter grade corresponding to the numerical grade 'percentage'

    if percentage > 100 :
        return "X"
    elif percentage >= 85 :
        return "A"
    elif percentage >= 70 :
        return "B"
    elif percentage >= 55 :
        return "C"
    elif percentage >= 40 :
        return "D"
    elif percentage >= 25 :
        return "E"
    elif percentage >= 0 :
        return "F"
    else :
        return "X"

#-------------------------------------------------------------------------------

def and_function( b1, b2 ) :

    # 'True', if both of the Booleans 'b1' and 'b2' are 'True',
    # and 'False' otherwise

    if b1 :
        return b2
    else :
        return False

#-------------------------------------------------------------------------------

def or_function( b1, b2 ) :

    # 'False', if both of the Booleans 'b1' and 'b2' are 'False',
    # and 'True' otherwise

    if b1 :
        return True
    else :
        return b2

#-------------------------------------------------------------------------------

def all_equal( x1, x2, x3 ) :

    # Are 'x1', 'x2', 'x3' all equal to one another?

    if x1 == x2 :
        if x2 == x3 :
            return True

    return False

#-------------------------------------------------------------------------------

def all_different( x1, x2, x3 ) :

    # Are 'x1', 'x2', 'x3' all different from one another?

    if x1 == x2 :
        return False

    if x1 == x3 :
        return False

    if x2 == x3 :
        return False

    return True

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#   Assignment #3 : The 'for' Statement
#-------------------------------------------------------------------------------

def fraction( c, s ) :

    # The fraction of the sequence 's' formed by the element 'c'

    length = 0
    count  = 0

    for item in s :
        length += 1
        if item == c :
            count += 1

    if length == 0 :
        return 0.0
    else :
        return count / length

#-------------------------------------------------------------------------------

def print_common( s1, s2 ) :

    # Print all elements which appear in both sequences 's1' and 's2',
    # in the order of their appearance in 's1';
    # assume that neither sequence contains repeated elements

    for item1 in s1 :
        if item1 in s2 :
            print( item1 )

#-------------------------------------------------------------------------------

def print_from( c, s ) :

    # Print all elements of sequence 's'
    # from the first instance of element 'c' onwards

    printing = False

    for item in s :
        if item == c :
            printing = True
        if printing :
            print( item )

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#   Assignment #4 : The 'range' Function
#-------------------------------------------------------------------------------

def power( x, n ) :

    # The number 'x' raised to the power of the non-negative integer 'n'

    power = 1

    for count in range( n ) :
        power *= x

    return power

#-------------------------------------------------------------------------------

def smallest_factor( n ) :

    # The smallest positive factor (apart from 1) of the integer 'n' >= 2

    for test in range( 2, n + 1 ) :
        if n % test == 0 :
            return test

#-------------------------------------------------------------------------------

def print_primes_below( limit ) :

    # Print all prime numbers below the integer 'limit'

    for test in range( 2, limit ) :
        if smallest_factor( test ) == test :
            print( test )

#-------------------------------------------------------------------------------

def main():
    
        # Test the functions
    
        print("letter_grade(percentage)")
        print( letter_grade( -1 ) )
        print( letter_grade(  0 ) )
        print( letter_grade( 25 ) )
        print( letter_grade( 40 ) )
        print( letter_grade( 55 ) )
        print( letter_grade( 70 ) )
        print( letter_grade( 85 ) )
        print( letter_grade(100 ) )
        print( letter_grade(101 ) )
        print()
    
        print("and_function(b1, b2)")
        print( and_function( False, False ) )
        print( and_function( False, True  ) )
        print( and_function( True,  False ) )
        print( and_function( True,  True  ) )
        print()
        
        print("or_function(b1, b2)")
        print( or_function( False, False ) )
        print( or_function( False, True  ) )
        print( or_function( True,  False ) )
        print( or_function( True,  True  ) )
        print()
    
        print("all_equal(x1, x2, x3)")
        print( all_equal( 1, 1, 1 ) )
        print( all_equal( 1, 1, 2 ) )
        print( all_equal( 1, 2, 1 ) )
        print( all_equal( 2, 1, 1 ) )
        print()
    
        print("all_different(x1, x2, x3)")
        print( all_different( 1, 1, 1 ) )
        print( all_different( 1, 1, 2 ) )
        print( all_different( 1, 2, 1 ) )
        print( all_different( 2, 1, 1 ) )
        print()
    
        print("fraction(c, s)")
        print( fraction( 1, [ 1, 1, 1, 1, 1 ] ) )
        print( fraction( 1, [ 1, 2, 3, 4, 5 ] ) )
        print( fraction( 1, [ 2, 3, 4, 5, 1 ] ) )
        print()
    #
        print("print_from(c, s)")
        print_common( [ 1, 2, 3, 4, 5 ], [ 1, 2, 3, 4, 5 ] )
        print_common( [ 1, 2, 3, 4, 5 ], [ 5, 4, 3, 2, 1 ] )
        print_common( [ 1, 2, 3, 4, 5 ], [ 6, 7, 8, 9, 0 ] )
        print()

main()