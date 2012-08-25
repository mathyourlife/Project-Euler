#!/usr/bin/env python
"""
Project Euler - Problem 2
http://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by 
adding the previous two terms. By starting with 1 and 2, 
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, find the sum of the 
even-valued terms.

Author: Daniel Couture
User: MathYourLife
Date: Aug 19, 2012
"""

from sys import path
from os import getcwd

path.append('%s/../ProjectEuler' % getcwd())

import ProjectEuler
from Sequences import Fibonacci

class Problem002(ProjectEuler.Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    Each new term in the Fibonacci sequence is generated by 
    adding the previous two terms. By starting with 1 and 2, 
    the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose 
    values do not exceed four million, find the sum of the 
    even-valued terms.
    """
    def __init__(self):
        super(Problem002, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        fib = Fibonacci()
        value = 1
        total = 0
        while value < 4000000:
            if value % 2 == 0:
                total += value
            value = fib.next()
        return total

def main():
    """
    Run this if called directly versus imported
    """
    prob2 = Problem002()
    
    prob2.solve()
    
    print prob2.problem_statement()
    print prob2.results()

if __name__ == "__main__":
    main()

