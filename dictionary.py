def run():
    """ A Dictionary is a data structure and data type in Python
        with special features that allow us to store any type of
        value such as integers, strings, lists, and even other functions.
        These dictionaries also allow us to identify each element by a key.
    """
    dictionary = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
        "llave4": 4,
    }
    # We traverse the dictionary by calling its keys, which are printed respectively
    for item in dictionary.keys():
        print(item)

    # We loop through the dictionary calling its values, which are printed respectively
    for item in dictionary.values():
        print(item)

    # if we need the item with its key and value, we call the items method, and
    # for our for we create two variables to represent the same
    for key, value in dictionary.items():
        print("La llave " + key + " tiene el valor " + str(value))


if __name__ == '__main__':
    run()
