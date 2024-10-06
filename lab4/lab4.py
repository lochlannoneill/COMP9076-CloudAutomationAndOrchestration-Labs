#-------------------------------------------------------------------------------
#   COMP8062 : 2024-2025 : 
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#   Assignment #9 : The 'while' Statement
#-------------------------------------------------------------------------------

def first_cube_above( n ) :

    # The smallest cube which exceeds the non-negative integer 'n'

    r = 1

    while r * r * r <= n :
        r += 1

    return r * r * r

#-------------------------------------------------------------------------------

def is_palindrome( s ) :

    # Does sequence 's' read the same forwards and backwards?

    lo = 0
    hi = len( s ) - 1

    while lo < hi and s[ lo ] == s[ hi ] :
        lo += 1
        hi -= 1

    return lo >= hi

#-------------------------------------------------------------------------------

def is_palindrome_words( s ):
    # Does the string 's' read the same forwards and backwards, when all
    # non-letters and capitalisations are ignored?

    only_letters = []
    position = 0
    while position < len(s): #a 'for' statement makes more sense here, if the assignment didn't prohibit it
        asciiCode = ord( s[position] )
        if 65 <= asciiCode <= 90:
            asciiCode += 32
        if 97 <= asciiCode <= 122:
            onlyLetters.append( asciiCode )
        position += 1
    return IsPalindrome( onlyLetters )


#-------------------------------------------------------------------------------

def binary( n ) :

    # The list of binary digits of the non-negative integer 'n'

    if n == 0 :
        return [ 0 ]

    else :
        binary_list = [ ]

        while n != 0 :
            binary_list   = [ n % 2 ] + binary_list
            n      //= 2

        return binary_list

#-------------------------------------------------------------------------------

def gcd( a, b ):
    
    #Find the greatest common divisor (GCD) of positive integers 'a' and 'b',
    #using the Euclidean Algorithm.
    
    while b != 0:
        remainder = a%b;
        a = b;
        b = remainder;
    return a

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#   Assignment #10 : Simulating Dice Rolls
#-------------------------------------------------------------------------------

def total_score( dice ) :

    # The sum of the scores obtained by rolling 'dice' dice

    from random import choice

    return sum( [ choice( range( 1, 7 ) ) for _ in range( dice ) ] )

#-------------------------------------------------------------------------------

def percent( part, whole ) :

    # The percentage that 'part' forms of 'whole', rounded to an integer

    return round( 100 * part / whole )

#-------------------------------------------------------------------------------

def dice_rolls( ) :

    # - repeatedly input a number of dice and a number of rolls
    # - simulate rolling the given number of dice for the given number of rolls
    # - each time the dice are rolled, calculate the total score obtained
    # - output a chart of the percentage of times each total score is obtained
    # - stop when a value of zero is supplied for the number of dice

    while True :
        dice  = int( input( "Number of Dice  = " ) )
        if dice == 0 :
            break
        rolls = int( input( "Number of Rolls = " ) )

        min_score = dice
        max_score = 6 * dice

        count = [0]*(max_score+1)

        for roll in range( rolls ) :
            count[ total_score( dice ) ] += 1

        print( )
        for tot_score in range( min_score, max_score + 1 ) :
            percent = percent( count[ tot_score ], rolls )
            print( "%2i : %2i%% : %s" % ( tot_score, percent, percent * "*" ) )
        print( )

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#   Assignment #11 : Reading Files
#-------------------------------------------------------------------------------

def print_long_lines( file_name, limit ) :

    # Output, to the screen, each line in file 'file_name' whose length exceeds
    # the integer 'limit', preceded by its line number in the input file;
    # newline characters are not counted when calculating line lengths

    file_handle = open( file_name, "r" )

    line_number = 0

    for line in file_handle :
        line_number += 1
        if len( line ) - 1 > limit :
            print( "%3i - %s" % ( line_number, line ), end = "" )

    file_handle.close()

#-------------------------------------------------------------------------------

def stats( file_names ) :

    # For each file in the list 'file_names', output, to the screen, the name
    # of the file along with both the number of lines and and the number of
    # characters in that file; finally, if there is more than one file in
    # 'file_names', output the total number of lines and characters for all files

    formatting = "%15s %6s %8s"  # using '%s' for both strings and integers

    print( formatting % ( "FILE", "LINES", "CHARS" ) )

    total_lines = 0
    total_chars = 0

    for file_name in file_names :
        file_handle = open( file_name, "r" )
        this_lines  = 0
        this_chars  = 0

        for line in fileHandle :
            this_lines += 1
            this_chars += len( line )

        print( formatting % ( file_name, this_lines, this_chars ) )

        total_lines += this_lines
        total_chars += this_chars

        file_handle.close()

    if len( file_names ) > 1 :
        print( formatting % ( "TOTAL", total_lines, total_chars ) )

#-------------------------------------------------------------------------------

def equal_files( file_name1, file_name2 ) :

    # Are the contents of 'filename1' and 'filename2' identical?

    file_handle1 = open( file_name1, "r" )
    file_handle2 = open( file_name2, "r" )

    while True :
        line1 = file_handle1.readline( )
        line2 = file_handle2.readline( )
        if line1 != line2 :
            file_handle1.close()
            file_handle2.close()
            return False
        if line1 == "":
            file_handle1.close()
            file_handle2.close()
            return True
#-------------------------------------------------------------------------------

def common_lines( file_name1, file_name2 ):

    #Output, to the screen, each line which is present
    #in both files 'file_name1' and 'file_name2'

    lines = []
    file_handle = open( file_name1, "r" )
    for line in file_handle:
        lines.append( line )

    file_handle = open( file_name2, "r" )
    for line in file_handle:
        if line in lines:
            print( line, end="" )
    file_handle.close()
    
#-------------------------------------------------------------------------------

def caesar( file_name ):
    
    #Output, to the screen, the contents of file 'file_name'
    #encoded using the Caesar cipher.

    shift = -3
    file_handle = open( file_name, "r" )
    
    for line in file_handle:
        for char in line:
            if char.isalpha(): #if it's a letter
                order = ord(char)
                if order <= 90: #A-Z
                    order = (((order - 65) + shift ) % 26 ) + 65
                else: #a-z
                    order = (((order - 97) + shift ) % 26 ) + 97
                print( chr(order), end="" )
            else:
                print( char, end="" )
            
    file_handle.close()

