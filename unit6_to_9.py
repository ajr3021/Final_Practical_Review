def find_primes(limit):
    """
    Write am iterative function that
    returns a list of all primes numbers given a limit.
    A prime number is a number that is not divisible
    by anything other than itself and 1.
    Assume limit is always at least 2 
    """
    pass


def letter_count(filename):
    """
    Write a function that given a filename will return a list
    that contains the number of times each letter is used.
    You can only use lists, not dicts.
    In order to do this you are going to need to use ord() and
    some math to calculate the index. (I don't know we knew ord at
    this point, but go ahead and use it)
    Convert all letters to lower case and ignore all puncuation.
    For reference a letter with have an ord value between 97 and 122.
    Make sure to use try except.
    Use list comprehension to create the initial list
    """
    pass



def reverse_string_recursive(string):
    """
    Create a recursive function that returns
    the reversed version of a string.
    """
    pass


def gcd(num1, num2):
    """
    Create a recursive function that given two numbers 
    will return the gcd.
    For example if you passed in 4 and 12 the function should
    return 4.
    If you want a hint, view the recursive definition of
    gcd in the gcd.png file. 
    """
    pass


def add():
    """
    Given this function, write a test for it using
    capsys and monkeypatch.
    """
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    return int(num1) + int(num2)