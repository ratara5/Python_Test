def area_triangle(b,h):
    
    """
    This program calculates the area of triangle given base and height:

    >>> area_triangle(2,4)
    'The triangle area is: 4.0'

    >>> area_triangle(5,4)
    'The triangle area is: 10.0'

    >>> area_triangle(6,8)
    'The triangle area is: 24.0'

    >>> area_triangle(7,4)
    'The triangle area is: 14.0'

    >>> area_triangle(9,6)
    'The triangle area is: 27.0'
    """

    return 'The triangle area is: '+str(b*h/2)

import doctest
doctest.testmod()
#If out doesn't show nothing, the test have been completed succesfully