#-------------------------------------------------------------------------------
#   COMP8062 : 2024-2025 : Assignment #1 : Functions
#-------------------------------------------------------------------------------

def box_volume( length, breadth, height ) :

    # The volume of a (cuboid) box of dimensions 'length', 'breadth',
    # and 'height', where each of these is a positive number

    return length * breadth * height

#-------------------------------------------------------------------------------

def perimeter( width, height ) :

    # The length of the perimeter of a rectangle of dimensions 'width'
    # and 'height', where each of these is a positive number

    return 2 * ( width + height )

#-------------------------------------------------------------------------------

def to_seconds( days, hours, minutes, seconds ) :

    # The total number of seconds in 'days' days, 'hours' hours,
    # 'minutes' minutes, and 'seconds' seconds, where each of these
    # is a non-negative integer

    return ( ( days * 24 + hours ) * 60 + minutes ) * 60 + seconds

#-------------------------------------------------------------------------------


def main():
    box = box_volume( 2, 3, 4 )
    print( f"The volume of the box is {box}" )
    
    perimeter_of_rectangle = perimeter( 2, 3 )
    print( f"The perimeter of the rectangle is {perimeter_of_rectangle}" )
    
    seconds = to_seconds( 1, 2, 3, 4 )
    print( f"The total number of seconds is {seconds}" )
    
main()
    