def run():
    """ For loops allow you to execute one or more statements
        iteratively, once for each element in the collection."""

    """ The counter is assigned the value in which this range
        (1, 1001), which starts at 1, and for will go to the
        next number, that's how it works. To demonstrate it,
        we proceed to print the counter value"""

    for contador in range(1, 1001):
        print(contador)

    # in this small cycle we print the results of the table of 11
    # for i in range(10):
    #     print(11 * (i + 1))


if __name__ == '__main__':
    run()
