"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """Print 'Hello World'"""

    print 'Hello World'


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    """Takes a name as a string and prints 'Hi' followed by the name"""

    print 'Hi %s' % name


# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.

def print_product(num1, num2):
    """Prints the product of two integers"""

    print num1 * num2


# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times

def repeat_string(string, num):
    """Takes a string and an integer and prints the string that many times"""

    print string * num


# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".

def print_sign(num):
    """Takes an integer and prints if the integer is higher or lower than zero.

    It prints 'Higher than 0' if the integer is higher than zero, 'Lower
    than 0' if lower than zero. 

    If the integer is zero, it prints 'Zero'.
    """

    if num == 0: print 'Zero'
    elif num > 0: print 'Higher than 0'
    else: print 'Lower than 0' 


# Missing instructions for is_divisible_by_three()

def is_divisible_by_three(num):
    """Returns true if the number is divisible by three.

    Returns false if the number is not divisible by three.
    """

    return num % 3 == 0


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.

def num_spaces(string):
    """Returns the number of spaces in the given string."""

    return string.count(' ')

# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.

def total_meal_price(price, tip=0.15):
    """Returns the total amount paid.

    The function takes the price of the meal and the tip as a percentage.

    The tip defaults to 0.15
    """

    return price + price * tip


# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.

def is_even(num):
    """Returns true if integer is even.

    Returns false if integer is odd.
    """

    return num % 2 == 0


def is_positive(num):
    """Returns true if integer is a positive number.

    Returns false if integer is a negative number.
    """

    if num == 0: return True
    return num > 0


# I think this function should be named parity_and_sign() if the desired outcome
# is [parity, sign] instead of [sign, parity]
def sign_and_parity(num):
    """Returns the sign and parity of the given integer in a list.

    The list is formatted [parity, sign]
    """

    num_info = [] # store the sign and parity in this list

    # check and append the parity
    if is_even(num): num_info.append('Even')
    else: num_info.append('Odd')

    # check and append the sign
    if is_positive(num): num_info.append('Positive')
    else: num_info.append('Negative')

    return num_info


parity, sign = sign_and_parity(-23)
print 'parity: %s \nsign: %s' % (parity, sign)


###############################################################################

# PART TWO

# 1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string

def full_title(name, job_title='Engineer'):
    """Takes a name and a job title and returns a string with the person's job
    title and name.

    job_title defaults to 'Engineer'
    """

    return '%s %s' % (job_title, name)


# 2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(recipient_name, recipient_title, sender_name):
    """Prints a formatted letter.

    The letter looks like this (with no carriage returns):

    Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing! 
    Sincerely, SENDER_NAME.
    """

    print 'Dear %s, I think you are amazing! ' \
          'Sincerely, %s' % (full_title(recipient_name, recipient_title),
                             sender_name)


###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
