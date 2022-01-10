from math import sqrt

def sqrt_list(num_list):

    """
    This function returns a list whose elements are the square-root of the element in entry list (sqrt returns double type). In the test, the entry list is created with a cycle:

    >>> num_list=[]
    >>> for elem in [4,9,16,25]:
    ...     num_list.append(elem)
    >>> sqrt_list(num_list)
    [2.0, 3.0, 4.0, 5.0]

    >>> num_list=[]
    >>> for elem in [36,49,64,81,100]:
    ...     num_list.append(elem)
    >>> sqrt_list(num_list)
    [6.0, 7.0, 8.0, 9.0, 10.0]
    
    >>> num_list=[]
    >>> for elem in [36,49,64,81,-100]:
    ...     num_list.append(elem)
    >>> sqrt_list(num_list)
    Traceback (most recent call last):
        ... 
    ValueError: math domain error
    """

    return [sqrt(n) for n in num_list]

#sqrt_list([36,49,64,81,-100]) #to see the error (math domain error) for copy in test (returns a expression, exception or error as failure->It won't be important what or how elements be negatives). square-root of negative number is not defined in Reals

import doctest
doctest.testmod()