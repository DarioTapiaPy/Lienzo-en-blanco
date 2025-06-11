from random_utils import generar_numero_aleatorio
# from sort_utils import ordenar_numeros
# from average_utils import calcular_promedio

print("Bienvenido al software de menú")
while True:
	opcion = input("""
1. Generar un número aleatorio
2. Ordenar 5 números
3. Calcular promedio de 5 números
4. Salir del programa

Opción:""")
	match opcion:
		case "1":
			generar_numero_aleatorio()
		case "2":
			ordenar_numeros()
		case "3":
			calcular_promedio()
		case "4":
			print("Saliendo del progama...")
			break
		case _:
			print("Opción ingresada no es válida, reintente")
