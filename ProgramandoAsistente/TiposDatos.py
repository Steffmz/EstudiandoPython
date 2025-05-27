# """ Ejercicio 1 """

# nombre = "Wilson"
# edad = 23

# print(f"Hola, {nombre}, tienes {edad} años")
# print("\n")

# """ Ejercicio 2 """

# numero1 = 19
# numero2 = 23

# suma = numero1 + numero2
# print("El resultado es:", suma)
# print("\n")

# """ Ejercicio 3 """

# nombre_producto = "Xbox"
# precio_producto = 100.1
# disponible_online = True

# print("Producto:", nombre_producto)
# print("Precio:", precio_producto)
# print("Disponible:", disponible_online)
# print("\n")

# """ Ejercicio 4 """

# mi_entero = 50
# mi_flotante = 25.0
# mi_texto = "Python es divertido"
# mi_booleano = True
# print(type(mi_entero))
# print(type(mi_flotante))
# print(type(mi_texto))
# print(type(mi_booleano))
# print("\n")

# """ Ejercicio 5 """

# base = 20.0
# altura = 10

# area = base * altura
# perimetro = 2 * (base*altura)
# print(f"Los valores el area y del perimetro son: {area} y {perimetro}")
# print("\n")

# """ Ejercicio 6 """

# edad_usuario = 19

# es_mayor_de_edad = (edad_usuario > 18)
# resultado = es_mayor_de_edad
# print(f"¿La persona es mayor de edad?: {resultado}")
# print("\n")

# """ Ejercicio 7 """

# dividendo = 20
# divisor = 2

# division_entera = dividendo // divisor
# residuo = dividendo % divisor
# print(f"Divion entera: {division_entera} y residuo: {residuo}")
# print("\n")

# """ Ejercicio 8"""

# numero_evaluar = 20
# cumple_condicion = (numero_evaluar %2 == 0 and numero_evaluar > 0)

# print(f"El numero {numero_evaluar} es positivo y par: {cumple_condicion}")
# print("\n")

# """ Ejercicio 9"""
# mi_numero = 1

# if mi_numero > 0:
#     print(f"El numero es positivo")
# elif mi_numero < 0:
#     print(f"El numero es negativo")
# else:
#     print(f"El numero es 0")
# print("\n")

# """ Ejercicio 10"""
# edad_visitante = 18
# tiene_entrada = True

# if edad_visitante >= 18 and tiene_entrada:
#     print("Acceso permitido")
# else:
#     print("Acceso denegado")
# print("\n")

# """ Ejercicio 11"""
# total_compra = 100
# if total_compra > 100:
#     precio_final = total_compra - (total_compra * 0.10)
#     print(f"Tienes un 10% de descuento y el total a pagar es: {precio_final}")    
# elif total_compra > 50:
#     precio_final = total_compra - (total_compra * 0.05)
#     print(f"Tienes un 5% de descuento el total a pagar es: {precio_final}")
# else: 
#     precio_final = total_compra
#     print(f"No obtienes descuento. El total a pagar es: {precio_final}")
# print("\n")

# """ Ejercicio 12"""
# color_semaforo = "Amarillo"
# color_semaforo = color_semaforo.lower()

# if color_semaforo == "rojo":
#     print("Detenerse")
# elif color_semaforo == "amarillo":
#     print("Precaución")
# elif color_semaforo == "verde":
#     print("Avanzar")
# else:
#     print("Color no reconocido")

# """ Ejercicio 13"""

# mi_palabra = "Python"
# for letra in mi_palabra:
#     print(letra)

# """ Ejercicio 14"""

# numero_entero = int(input("Ingresa un numero entero: "))

# for i in range(1, 11): # stop. start y stop. start, stop y step
#     print(f"{numero_entero} x {i} = {i * numero_entero}")

# """ Ejercicio 15"""

# n=10
# suma_total=0

# for recorrido in range(1, n+1):
#     suma_total += recorrido
# print("La suma total es:", suma_total)
# print("\n")

# """ Ejercicio 16 """

# frase = "Aprender Python es emocionante"
# contador_vocales=0

# vocales="aeiou"

# for recorrido in frase:
#     caracter_en_minuscula = recorrido.lower()
#     if caracter_en_minuscula in vocales:
#         contador_vocales += 1
# print("El total de vocales es:", contador_vocales)

# contador = 0
# while contador < 5: # La condición es "contador < 5"
#     print(f"El contador es: {contador}")
#     contador = contador + 1 # ¡Esto es crucial! Modificamos 'contador'
#                             # para que la condición eventualmente sea False.
#                             # También se puede escribir como: contador += 1
# print("Bucle terminado.")

# entrada_usuario = ""
# while entrada_usuario != "salir": # La condición es que la entrada no sea "salir"
#     entrada_usuario = input("Escribe 'salir' para terminar: ")
#     print(f"Escribiste: {entrada_usuario}")
# print("¡Adiós!")

# """ Ejercicio 17 """

# numero_inicio = 5
# while numero_inicio >= 1:
#     print(f"{numero_inicio}")
#     numero_inicio-=1
# print("¡Despegue!")

# """ Ejercicio 18 """

# contrasena_correcta = "python123"
# entrada_usuario=""
# while entrada_usuario != contrasena_correcta:
#     entrada_usuario = input("Ingresa la contraseña: ")
#     if entrada_usuario != contrasena_correcta:
#         print("Contraseña incorrecta. Intenta de nuevo.")
# print("¡Contraseña aceptada!")

# """ Ejercicio 19 """

# suma_acumulada = 0

# while True:
#     numero_ingresado = int(input("Ingresa un número (ingresa 0 o un negativo para terminar): "))
#     if numero_ingresado > 0:
#         suma_acumulada+=numero_ingresado
#     elif numero_ingresado <= 0:
#         break
# print(f"La suma de los números positivos ingresados es: {suma_acumulada}")

# """ Ejercicio 20 """

# while True:
#     opcion = input("Elige una opcion (1, 2, 3): ")
#     if opcion == "1":
#         print("¡Hola! ¿Cómo estás?")
#     elif opcion == "2":
#         print("¡Hasta luego!")
#     elif opcion == "3":
#         print("Saliendo del programa...")
#         break
#     else:
#         print("Opcion no valida. intenta de nuevo")

# """ Ejercicio 21 """

# peliculas_favoritas = ["28 weeks later", "Interstellar", "Pacific Rim"]

# print(peliculas_favoritas)
# print(peliculas_favoritas[0])
# print(peliculas_favoritas[-1])

# """ Ejercicio 22 """

# lista_compras = []
# lista_compras.append("Ropa")
# lista_compras.append("Zapatillas")
# lista_compras.append("Celular")

# lista_compras.insert(0, "Dinero")

# print(lista_compras)
# print(len(lista_compras))

# """ Ejercicio 23 """

# invitados = ["Wilson", "Xiomara", "Tom", "Simba", "Raa"]
# invitados.remove("Wilson")
# invitados.append("Steven")
# print(invitados)
# print(len(invitados))

# """ Ejercicio 24 """

# numeros_prueba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = []
# impares = []

# for numeros in numeros_prueba:
#     if numeros %2 == 0:
#         pares.append(numeros)
#     else:
#         impares.append(numeros)
# print(pares)
# print(impares)

# """ Ejercicio 25 """

# numero_diez = list(range(11))#Genera una lista del 0 al 10
# print(numero_diez[0:5])      #Imprime los 5 primeros numeros osea 0,1,2,3,4

# print(numero_diez[3:8])      #imprime del 3 al 7

# print(numero_diez[-3:])      #Imprime los ultimos 3

# print(numero_diez[0:11:2]) #Imprime del 0 al 10 pero de dos en dos

# numeros_invertidos = numero_diez[::-1]
# print(numeros_invertidos)

""" Ejercicio 26 """

ranking = [("Ana", 85), ("Luis", 92), ("Eva", 78), ("Juan", 92), ("Leo", 88)]
ranking.sort(key=lambda x: x[1], reverse=True)
print(ranking)

jugadores=["Ana", "Luis", "Eva", "Juan", "Leo"]
puntuaciones=[85, 92, 78, 92, 88]
puntuaciones.sort(reverse=True)
print(puntuaciones)

# """ Ejercicio 27 """

# inventario=["manzana", "banana", "naranja", "manzana", "uva", "banana", "manzana"]

# cuantas_manzanas_hay=inventario.count("manzana")
# posicion_naranja=inventario.index("naranja")

# print("Manzana(s):", cuantas_manzanas_hay)
# print("Naranja(s):", posicion_naranja)

# if "pera" in inventario:
#     print(inventario.index('pera'))
# else:
#     print("Lo siento, no tenemos pera(s).")

# """ Ejercicio 28 """

# temperatura=[22.5, 23.1, 22.8, 21.9, 23.5, 24.0, 21.5, 22.8, 23.1]

# temperatura.sort()

# print("La temperatura mas baja registrada fue:", temperatura[0])
# print("La temperatura mas alta registrada fue:", temperatura[-1])

# temperatura.reverse()
# print("Temperaturas ordenadas de mayor a menor:", temperatura)