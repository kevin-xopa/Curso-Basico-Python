def run():
    # A constant is a type of variable which cannot be changed.
    # In Python, constants are declared in uppercase.
    LIMIT = 1000000
    accountant = 0
    power = 2 ** accountant

    """ The while loop is nothing more than a cycle, which
        repeats everything that is inside it, as long as a condition is met.

        In this case, here we are saying that as long as power is less than
        LIMIT, what is inside the loop will be done.    """
    while power < LIMIT:
        # for this loop, traverse a table of 2 raised LIMIT, and all this
        # will be executed while power is less than LIMIT
        print("2 elevado a " + str(accountant) +
              " es igual a... " + str(power))

        # accountant is our counter, which increases one by one, so that the powers
        # of 2 rise for each turn the loop makes, preventing our loop from being infinite
        # accountant = accountant + 1
        accountant += 1

        # we generate the power
        power = 2**accountant


if __name__ == '__main__':
    run()
