import random

def generar_numero_aleatorio():
    repeticion = True
    while repeticion:
        numeros = []
        try:
            cantidad = int(input("Cuantos números desea agregar a la lista?: "))
            while cantidad > 0:
                try:
                    numeros.append(int(input("Ingrese un número entero: ")))
                    cantidad -= 1
                except ValueError:
                    print("El número aleatorio debe ser un número entero, reintente")
            print(random.choice(numeros))
            otra_vez = input("Desea volver a generar un número aleatorio? [S/N]: ").upper()
            repeticion = True if otra_vez == "S" else False
        except ValueError:
            print("El valor ingresado debe ser un número entero, reintente")
    print("Saliendo...")
    
generar_numero_aleatorio()