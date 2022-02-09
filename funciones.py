""" They are essential code structures. A function is a group of
    instructions that constitute a logical unit of the program and
    solve a very specific problem.
"""

# we generate a function passAParameter, which needs a string parameter
def passAParameter(option):
    print("Hola")
    print("como estas")
    print("elegiste la opción " + option)
    print("adios")

# we ask for a data input with input, we assign the value obtained to a variable
option = input("Elige una opción (1, 2, 3) ")

# we call the function passAParameter and pass the necessary parameter
passAParameter(option)