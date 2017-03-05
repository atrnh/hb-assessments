"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def is_hometown(town):
    """Returns true if town is my hometown.

    Returns false if town is not my hometown.

        >>> is_hometown('Inaba')
        True

        >>> is_hometown('Akihabara')
        False
    """

    my_hometown = 'Inaba'

    return town == my_hometown


#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def get_full_name(first_name, last_name):
    """Returns the full name.

    The return string looks like this:
    'first_name last_name'

        >>> get_full_name('Makoto', 'Yuki')
        'Makoto Yuki'
    """

    return '%s %s' % (first_name, last_name)


#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def greet_by_hometown(hometown, first_name, last_name):
    """Prints a greeting based on the person's hometown.

    Prints 'Hi, first_name last_name, we're from the same place!' if they are
    from the same hometown.

    Prints 'Hi first_name last_name, where are you from?' if they are not from
    the same hometown.

        >>> greet_by_hometown('Inaba', 'Yuu', 'Narukami')
        Hi, Yuu Narukami, we're from the same place!

        >>> greet_by_hometown('Akihabara', 'Rintaro', 'Okabe')
        Hi Rintaro Okabe, where are you from?
    """

    if is_hometown(hometown): # check if from the same hometown
        print "Hi, %s, we're from the same place!" % get_full_name(first_name,
                                                                   last_name)
    else: # not from the same hometown
        print 'Hi %s, where are you from?' % get_full_name(first_name, 
                                                           last_name)


###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."

def is_berry(fruit):
    """Determines if fruit is a berry"""

    berries = ['strawberry', 'cherry', 'blackberry']

    return fruit in berries


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit): return 0 # cost is 0 if fruit is a berry
    else: return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    return lst + [num]



# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(base_price, state, tax=.05):
    """Calculates the total price of an item.

    This functions takes the base price of an item, a two-letter state
    abbreviation, and the tax percentage (as a two-digit decimal).

    It applies the appropriate taxes and fees to calculate the total price of
    an item.

    Tax is 5% by default.
    """

    price_before_fees = base_price + base_price * tax # price before state fees

    fees_by_state = {
        'CA': (price_before_fees * 0.03), # CA's 3% recycling fee
        'PA': 2.0, # PA's $2 fee
        # MA has two fees: the first one is for base price under $100
        # and the second is for gross price over $100
        'MA': (1.0, 3.0)
    }

    if state in fees_by_state:
        # By checking if a value is a tuple (instead of checking if 
        # state == 'MA'), we can add more states to fees_by_state that 
        # apply fees similarly to MA
        if type(fees_by_state[state]) is tuple:
            if base_price < 100:
                # Apply commonwealth fee for base_price below 100
                total_price = price_before_fees + fees_by_state[state][0]
            else:
                # Apply commonwealth fee for base_price above 100
                total_price = price_before_fees + fees_by_state[state][1]
        else:
            # Apply state fees
            total_price = price_before_fees + fees_by_state[state]
    else: # If the state is not in fees_by_state, do not apply any fees
        return price_before_fees

    return total_price


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def append_all(lst, *args):
    """Append all supplied arguments to given list.

        >>> append_all([1, 2], 45, 66, 7)
        [1, 2, 45, 66, 7]
    """

    for arg in args: lst.append(arg)

    return lst


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def get_inner_output(word):
    """Returns the given word and the result of calling the inner function.

        >>> get_inner_output('Three')
        ('Three', 'ThreeThreeThree')
    """

    def mult_by_three(string):
        """Returns given string multiplied 3 times."""
        return string * 3

    inner_output = mult_by_three(word)

    return (word, inner_output)


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
