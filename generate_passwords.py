# import the random class
import random

# create generate password function
def generatePassword():
    # uppercase alphabet list
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    # lowercase alphabet list
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    # numeric data list
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # list of special characters
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
             '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    # we join the lists
    characters = MAYUS + MINUS + NUMS + CHARS
    # list that will contain the password
    password = []

    # we generate the for that runs through our code n times (n = 20)
    for i in range(20):
        # with the choice function we get a random character from our list of characters
        random_char = random.choice(characters)
        # finally we add the character obtained to our 'password' list
        password.append(random_char)

    """ we return the password list as a string,
        with the help of the join method ''.join
        Joins all the elements of a tuple into a
        string, using a character within      ''
        as a separator """
    return ''.join(password)


def run():
    # call the generatePassword() function
    password = generatePassword()

    print("Nueva contraseña: " + password)


if __name__ == '__main__':
    run()
