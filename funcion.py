def saludar():
    print("Hola")

saludar()





def obtener_saludo():
    return "Hola"

mensaje = obtener_saludo()
print(mensaje)  # Esto imprime: Hola





def sumar(a, b):
    resultado = a + b
    return resultado

x = sumar(3, 5)
print(x)  # Imprime 8






def es_par(n):
    return n % 2 == 0

print(es_par(4))  # True
print(es_par(7))  # False
 





def clasificar_edad(edad):
    if edad < 13:
        return "Niño"
    elif edad < 18:
        return "Adolescente"
    else:
        return "Adulto"

print(clasificar_edad(10))  # Niño
print(clasificar_edad(15))  # Adolescente
print(clasificar_edad(25))  # Adulto



def saludar(nombre):
    print(f"Hola {nombre}")

x = saludar("Ana")  # Esto imprime: Hola Ana
print(x)  # Esto imprime: None (porque no hay return)
