def conversor(moneda):
    valor_dolar = 0
    tipo_peso = ""
    if moneda == 1:
        valor_dolar = 3933.68
        tipo_peso = "colombianos"
    elif moneda == 2:
        valor_dolar = 3933.68
        tipo_peso = "argentinos"
    elif moneda == 3:
        valor_dolar = 20.6
        tipo_peso = "mexicanos"
    else:
        return "La opción no es valida"
    pesos = input("Cuantos pesos " + tipo_peso + " tienes? ")
    pesos = float(pesos)

    dolares = pesos / valor_dolar
    return "Tienes $" + str(round(dolares, 2)) + " dolares"


print("""
    Bienvenido al conversor de plata

    1 .- Pesos colombianos
    2 .- Pesos argentinos
    3 .- Pesos mexicanos

    Elige una opción...
""")
opcion = int(input("Elige una opción "))
print(conversor(opcion))
