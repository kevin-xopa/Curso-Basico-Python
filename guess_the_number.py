# We import the random class https://docs.python.org/es/3.10/library/random.html
import random


def run():
    # The randint method returns a random integer in the range [a, b], including both endpoints.
    random_number = random.randint(1, 100)

    # we request a number, which we will transform to int
    chosen_number = int(input("Elige un numero del 1 al 100... "))

    # we generate a loop, which will be fulfilled whenever the chosen_number is different from random_number
    while chosen_number != random_number:
        if(chosen_number < random_number):
            print("El numero es mayor, intentalo de nuevo... ")
        else:
            print("El numero es menor, intentalo de nuevo... ")

        # we will request a number again, so as not to generate an infinite loop
        chosen_number = int(
            input("Elige un numero del 1 al 100... "))

    # breaking the loop sends a message
    print("Ganaste chulo, el numero es... " + str(random_number))


if __name__ == '__main__':
    run()
