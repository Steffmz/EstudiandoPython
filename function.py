def saludar(nombre):
    return f"¡Hola, {nombre}!"

saludarwilson = saludar("Wilson")
saludarxiomara = saludar("Xiomara")

print(saludarwilson)
print(saludarxiomara)

def sumar_dos_numeros(a, b):
    return a + b

suma = sumar_dos_numeros(3, 5)
suma2 = sumar_dos_numeros(9, 10)
print(suma)
print(suma2)

#def encontrar_mayor():
    #Escribe una función llamada encontrar_mayor que tome una lista de números
    #como argumento y devuelva el número más grande de esa lista.
    #(Recuerda, la idea es que implementes la lógica, 
    #no uses la función max() integrada).