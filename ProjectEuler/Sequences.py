"""
ProjectEuler.Sequences

Collection of classes for various type of sequences.

Author: Daniel Couture
User: MathYourLife
Date: Aug 19, 2012
"""

class Fibonacci:
    """
    A Fibonacci series class.  Provided with a starting condition
    it will propagate to the next value by finding the sum of the
    previous two values.
    
    @param current: The last value of the known sequence
    @type  current: int
    
    @param previous: The previous value of the known sequence
    @type  previous: int
    """
    
    def __init__(self, current = 1, previous = 0):
        self.current = current
        self.previous = previous
    
    def next(self):
        """
        A Fibonacci series class.  Provided with a starting condition
        it will propagate to the next value by finding the sum of the
        previous two values.
        
        @param current: The last value of the known sequence
        @type  current: int
        
        @param previous: The previous value of the known sequence
        @type  previous: int
        
        @return: The next value in the sequence by summing the last two
        @rtype:  int
        """
        next_value = self.current + self.previous
        self.previous = self.current
        self.current = next_value
        return next_value

class Palindrome:
    """
    Palindrome - Efficiently jumps from a palindrome to
    the next/previous.  The internal _seed property tracks
    the left portion of the number and allows us to jump
    from one to the next.
    
    @param   start: Starting palindrome
    @type    start: int
    @default start: 1
    """
    def __init__(self, start = 1):
        # Validate the starting value if not provided
        if start != 1:
            if start < 0:
                print 'Start value must be a non negative integer palindrome.'
                raise
            if not self.is_a_palindrome(start):
                print 'Start value supplied is not a palindrome.'
                raise
        
        # Initialize the seed on the class
        self._odd_length = len(str(start)) % 2 == 1
        start_list = list(str(start))
        seed_len = (len(start_list) + 1) / 2
        self._seed = int(''.join(start_list[:seed_len]))
        
        self.value = start
    
    def is_a_palindrome(self, value):
        """
        is_a_palindrome - Check if the passed value is a palindrome.
        
        @param value: Integer to verify if is a palindrome
        @type  value: Int
        
        @return: If the value is a palindrome
        @rtype:  bool
        """
        str_value = str(value)
        forward_list = list(str_value)
        reverse_list = list(str_value)
        reverse_list.reverse()
        return forward_list == reverse_list
    
    def previous(self):
        """
        Find the next largest palindrome.
        
        @return: The next largest palindrome
        @rtype:  int
        """
        
        if self.value == 0:
            print 'Can not go back past 0'
            raise
        
        # Determine how to modify the seed value
        if len(str(self._seed)) != len(str(self._seed - 1)):
            # Next palindrome has a fewer number of digits
            if self._odd_length == True:
                self._seed = self._seed - 1
                self._odd_length = False
            else:
                self._seed = (self._seed * 10) - 1
                self._odd_length = True
        else:
            # Palindrome is not changing the number of digits
            if self.value == 11:
                # Special case to transfer down to single digits
                self._seed = 9
                self._odd_length = True
            else:
                # Decrement the seed
                self._seed -= 1
        
        # Now that we have the right next seed, create the palindrome
        str_seed = str(self._seed)
        prefix_list = list(str_seed)
        suffix_list = list(str_seed)
        suffix_list.reverse()
        if self._odd_length:
            # Palindrome should be an odd length so no 
            # repeating the center digit
            self.value = int(''.join(prefix_list) + ''.join(suffix_list[1:]))
        else:
            # Just flip and concat the seed
            self.value = int(''.join(prefix_list) + ''.join(suffix_list))
        return self.value
    
    def next(self):
        """
        Find the smallest largest palindrome.
        
        @return: The next smallest palindrome
        @rtype:  int
        """
        
        # Determine how to modify the seed value
        if len(str(self._seed)) != len(str(self._seed + 1)):
            # Next palindrome has increased the number of digits
            if self._odd_length == True:
                self._seed = (self._seed + 1) / 10
                self._odd_length = False
            else:
                self._seed += 1
                self._odd_length = True
        else:
            # Increment the seed
            self._seed += 1
        
        # Now that we have the right next seed, create the palindrome
        str_seed = str(self._seed)
        prefix_list = list(str_seed)
        suffix_list = list(str_seed)
        suffix_list.reverse()
        if self._odd_length:
            # Palindrome should be an odd length so no 
            # repeating the center digit
            self.value = int(''.join(prefix_list) + ''.join(suffix_list[1:]))
        else:
            # Just flip and concat the seed
            self.value = int(''.join(prefix_list) + ''.join(suffix_list))
        return self.value
