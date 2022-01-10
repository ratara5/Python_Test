def verificate_mail(mail):

    """
    This function realize a validation of a mail
    if @ quantity is equal 0 or @ quantity greater than 1 or @ is in last position of mail, then no valid mail:

    >>> verificate_mail('mail@mail.com')
    True
    >>> verificate_mail('mailmail@.com')
    True
    >>> verificate_mail('mailmail.c@om')
    True
    >>> verificate_mail('@mail@mail.com')
    False
    >>> verificate_mail('mailmail.com@')
    False
    >>> verificate_mail('mailmail.com')
    False
    """

    a=mail.count('@')
    if a!=1 or mail.rfind('@')==(len(mail)-1):
        return False
    else:
        return True
    
import doctest
doctest.testmod()


        