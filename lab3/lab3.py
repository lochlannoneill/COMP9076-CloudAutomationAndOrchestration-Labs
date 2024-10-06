#The Range Function
##
##def alphabet():
##    # Return a string containing all the (lower case) letters
##    # of the English alphabet
##    alphabet = ""
##    for i in range(97, 123): 
##        alphabet += chr(i)
##    return alphabet
##
####Sample sequence: 0 1 1 2 3 5 8 13 21 34
##
##def fibonacci( n ):
##    # Prints the first 'n' members of the fibonacci sequence
##	
##    prev = 0
##    if n >= 1 :
##        print(prev)
##    nxt = 1
##    if n >= 2 :
##        print(nxt)
##    if n < 0 :
##        print("Enter a value >= 0")
##   
##    for i in range(3, n+1):
##        prev, nxt = nxt, nxt+prev  
##        print(nxt)
##
##
##def first_digit( n ):
##    #Find the first digit of the positive integer 'n'
##    for i in range( n ): #[0,1,2,3... n-1] n=10 -> 1 
##        if n < 10 :
##            return n 
##        else:
##            n = n // 10

##for i in range(10,22,3):
##    print(i)

##for i in range(10,2,-1):
##    print(i)
    
##https://docs.python.org/3/tutorial/datastructures.html
##New date type: Lists
##l = [] #empty list
##l = [1,2,3]
##print(l)
##l = [1, "hello", True, 0.9]
##print(l)
##
##l.append(4)
##print(l)
##l += [6,7,8]
##print(l)
##
##l = l + [9]
##print(l)
##
##s = [1,2,3]
##y = s
##y.append(4)
##print(s)

##def append_seq(s):
##    for x in s:
##        s += x #s must be a string
##        print(s)
##    return s

##def append_seq(s): #infinite loop
##    for x in s:
##        s += [x] #must be a list
##        print(s)
##    return s

##def append_seq(s): #infinite loop
##    m = s
##    for x in s:
##        m.append(x) #not a string!
##        print(m)
##    return s

##def append_seq(s): #NOT infinite loop
##    m = s
##    for x in s:
##        m = m + [x]
##        print(m)
##    return m
##
##def to_list( s ) :
##    # Converts the string ‘s’ to a list
##    # [ Python builtin: list( s ) ]
##    l = []
##    for item in s :
##        l.append(item) #= l + [item], += [item]   
##    return l
##
##def count_odds( numbers ):
##    #Count how many members of the integer list 'numbers' are Odd numbers.
##    odd = 0
##    for num in numbers:
##        if num % 2 == 1:
##            odd += 1
##    return odd
##
##def total( numbers ) :
##    # The sum of the items in the numeric list ’numbers’,
##    # or 0 if this list is empty
##    # [ Python builtin: sum( numbers ) ]
##    tot = 0
##    for number in numbers :
##        tot += number
##    return tot
##
##def average( numbers ) :
##    # The average of the items in the numeric list ’numbers’;
##    # if this list is empty, issue an error message and return ’None’
##    if numbers == [ ] :
##        print( "Average : argument list is empty" )
##        return None
##    return total( numbers ) / len( numbers )
##
##
##def maximum( lst ) :
##    # The largest item in the list ’lst’;
##    # if this list is empty, issue an error message and return ’None’
##    # [ Python builtin: max( lst ) ]
##    if lst == [ ] :
##        print( "Maximum : argument list is empty" )
##    maxi = None
##    for item in lst :
##        if maxi == None or item > maxi :
##            maxi = item
##    return maxi
##
#### Lexicographical ordering
##
##def longest_string( strings ) :
##    # The longest item in the string list ’strings’,
##    # or "" if this list is empty
##    longest = ""
##    for string in strings :
##        if len( string ) > len( longest ) :
##            longest = string
##    return longest
##
##def first_item( s ) :
##    # The first item in sequence ’s’, or ’None’ if this sequence is empty
##    for item in s :
##        return item
##    return None
##
##def all_equal( s ) :
##    # Are all items in sequence ’s’ equal to one another?
##    start_item = first_item( s )
##    for item in s :
##        if item != start_item :
##            return False
##    return True
##
##def is_sorted( s ) :
##    # Is sequence ’s’ sorted in ascending order?
##    prev = None
##    for this in s :
##        if prev != None and this < prev :
##            return False
##        prev = this
##    return True
####
####a = 5
####b = 6 
####c = [a,b]
####print(c)
####
####c=[1,2+3,4*5]
####print(c)
####print(len(c))
##
##def lists_equal( lst1, lst2 ): #[1,2,3,4] [1,2,3,5]
##    #Check if the two given lists, lst1 and lst2, have the same elements
##    #in the same order and return True if so, otherwise return False
##    if( len(lst1) != len(lst2) ):
##        return False
##    position = 0
##    for item1 in lst1:
##        lst2_location = 0
##        for item2 in lst2:
##            if position == lst2_location and item1 != item2:
##                return False
##            lst2_location += 1
##        position += 1
##
##    return True   
#####List Comprehensions
####
#####https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
####
##
##def count_list( n ):
##    #A list containing the integers from 0 to 'n'
##    numbers = []
##    for a in range( n+1 ):
##        numbers.append(a)
##    return numbers
##
##def count_list2( n ):
##    #A list containing the integers from 0 to 'n'
##    return [a for a in range( n+1 ) ]
##
##def double( numbers ):
##    #Return a copy of the integer list 'numbers' with every value doubled
##    doubled = []
##    for n in numbers:
##        doubled.append( n*2 )
##    return doubled
##
##def double2( numbers ):
##    #Return a copy of the integer list 'numbers' with every value doubled
##    return [n*2 for n in numbers]
##
##def squares( limit ) :
##    # The list of squares of positive integers up to that of ’limit’
##    return [ n * n for n in range( 1, limit + 1 ) ]
##
##def positives( numbers ):
##    #Return a copy of the integer list 'numbers' containing only positive values
##    posi = []
##    for n in numbers:
##        if n > 0:
##            posi.append( n )
##    return posi
##
##def positives2( numbers ) :
##    # The list of positive items in the numeric list ’numbers’
##    return [ n for n in numbers if n > 0 ]
##
##def vowels( string ) :
##    # The list of vowels in string ’string’
##    return [ v for v in string if v in "AEIOUaeiou" ]
##
##def factors( n ) :
##    # The list of positive factors of the positive integer ’n’
##    return [ f for f in range( 1, n + 1 ) if n % f == 0 ]
##
##def primes_below( limit ) :
##    # The list of prime numbers below the integer ’limit’
##    return [ p for p in range( 2, limit ) if factors( p ) == [1, p ] ]
##
#########################################
########### Sieve of Eratosthenes ####### 
#########################################
##
##def prime_sieve( limit ):
##    #The list of all prime numbers below the integer 'limit'
##    notPrimes = [j for i in range( 2, int(limit**0.5)+1 ) for j in range(i*i, limit, i)]
##    return [x for x in range(2, limit) if not x in notPrimes]
##
####a = [1,2,3]
####b = [4,5,6]
####c = [a,b]
####print(c)
##
##def word_sizes( strings ):
##    #Return a list of lists, where each list contains
##    #a string from the list of strings 'strings', as well as its length
##    sizes = []
##    for word in strings:
##        sizes.append([word, len(word)])
##    return sizes
##
##def word_sizes2( strings ):
##    #Return a list of lists, where each list contains
##    #a string from the list of strings 'strings', as well as its length
##    return [[word, len(word)] for word in strings ]
##
##def repetitions( n ) :
##    # The list of lists of ’i’ copies of the integer ’i’,
##    # for each value of ’i’ from 0 up to the integer ’n’
##    return [ [ i for _ in range( i ) ] for i in range( n + 1 ) ]
##
##def pairs( s1, s2 ) :
##    # The list of 2-lists of items of sequences ’s1’ and ’s2’,
##    # taken in all possible combinations
##    return [ [ item1, item2 ] for item1 in s1 for item2 in s2 ]

lsts = [['a', 'd'], ['a', 'e'], ['b', 'd'], ['b', 'e'], ['c', 'd'], ['c', 'e']]
##for lst in lsts:
##    print(lst)

##for lst in lsts:
##    for item in lst:
##        print(item)

##a = [1,2]
##b = [3,4]
##c = [5,6]
##d = [a,b,c]
##print(d)
##
##for i in a:
##    print(i)

##a = [1,2]
##b = [[4,5],a,[6,7],a]
##print(b)
##a.append(3)
##print(a)
##print(b)

#rev = rev + [item] [1,2]+[3] -> [1,2,3], rev = [item] + rev [3]+[1,2] -> [3,1,2]

##def reverse_func( lst ) :
##    # A copy of the list ’lst’ with items in reverse order
##    #Related to Python Built-In: lst.reverse()
##    rev = [ ]
##    for item in lst :
##        rev = [ item ] + rev 
##    return rev
##
##a = [1,2,3,4]
##a.pop(2)
##print(a)

###"Indexing" into Lists and Strings
##lst = "David"
##+---+---+---+---+---+
##| D | a | v | i | d |
##+---+---+---+---+---+
##  0   1   2   3   4
## s-5 s-4 s-3 s-2 s-1  #s = len(lst)

## -5  -4  -3  -2  -1
##
##a = [1,2,3]
##print(a[1])
##b = a
##a[-2] = 6
##print(b)
##
##c = "hello"
##print(c[2])
####c[2] = "B"

def print_func( s ) :
    # Print the items of the sequence ’s’, one per line
    for i in range( len( s ) ) :
        print( s[ i ] )

def print_reversed( s ) :
    # Print the items of the sequence ’s’, one per line, in reverse order
    lastIndex = len( s ) - 1
    for i in range( len( s ) ) :
        print( s[ lastIndex - i ] )

def reverse( lst ) :
    # A copy of the list ‘lst’ with the items in
    # reverse order
    copy = [ ]
    last_index = len( lst ) - 1
    for i in range( len( lst ) ) :
        copy.append( lst[ last_index - i ] )
    return copy

def reverse_in_place( lst ) :
    # The contents of the list ‘lst’ with the items
    # reversed in place
    last_index = len( lst ) - 1
    for i in range( len( lst ) // 2 ) :
        lst[i], lst[last_index-i] = lst[last_index-i], lst[i]

def is_sorted( s ) :
    # Is sequence ’s’ sorted in ascending order? 
    for i in range( len( s ) - 1 ) :
        if s[ i + 1 ] < s[ i ] :
            return False
    return True

def double( lst ) :
    # Double the values of the items in the integer
    # list ‘lst’, in place
    for i in range( len( lst ) ) :
        #lst[ i ] = lst[ i ]*2
        lst[ i ] *= 2

def add_lists( numbers1, numbers2 ) :
    # The list formed by adding corresponding items
    # in numeric lists ’numbers1’ and ’numbers2’;
    # assume that both lists have the same number of items
    return [ numbers1[ i ] + numbers2[ i ] for i in range( len( numbers1 ) ) ]

def alternate_items( s1, s2 ):
    #Create a list which alternates between the elements of the sequences
    #'s1' and 's2'. Assume that both lists are of the same length
    alt_lst = []
    for i in range( len( s1 ) ):
        alt_lst.append(s1[i])
        alt_lst.append(s2[i])
    return alt_lst

#[1,2,3,4,5],2 -> [3,4,5,1,2]

def rotate( lst, n ) :
    # A copy of list ’lst’ rotated leftwards by ’n’ items;
    # assume that 0 <= n <= len( lst ) - 1
    rot = [ ]
    for i in range( n, len( lst ) ) :
        rot += [ lst[ i ] ] #[3,4,5]
    for i in range( 0, n ) :
        rot += [ lst[ i ] ] #[3,4,5,1,2]
    return rot


