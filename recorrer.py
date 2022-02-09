def run():
    """ We can also loop through a string, since a string is a
        string of characters, where each character is at a
        particular index and can be accessed individually.
    """
    sentence = input("Escribe una frase... ")
    for character in sentence:
        print(character.upper())


if __name__ == "__main__":
    run()
