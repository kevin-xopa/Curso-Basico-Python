""" We will create a function in charge of verifying that
    a word is a palindrome, requesting a string as a parameter
    that will return a true or false.
"""
def palindromo(palabra):
    """ replace(), receives two parameters, the first one
        indicates which characters it is going to look for
        to replace, the second one indicates how it will
        change those characters.

        lower() converts all text to lowercase.
    """
    # by performing this slice [::-1], we are making our string wrap backwards
    palabra = palabra.replace(' ', '').lower()
    palabra_invertida = palabra[::-1]
    # we verify that they are equal
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Dame una palabra... ")
    if(palindromo(palabra)):
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()
