#def saludar(nombre):
    #return f"¡Hola, {nombre}!"

#saludarwilson = saludar("Wilson")
#saludarxiomara = saludar("Xiomara")

#print(saludarwilson)
#print(saludarxiomara)

#def sumar_dos_numeros(a, b):
    #return a + b

#suma = sumar_dos_numeros(3, 5)
#suma2 = sumar_dos_numeros(9, 10)
#print(suma)
#print(suma2)

def encontrar_mayor(lista_numeros): 
    if not lista_numeros:
        return None

    mayor_hasta_ahora = lista_numeros[0] 

    for recorrido in lista_numeros:
        if recorrido > mayor_hasta_ahora:
            mayor_hasta_ahora = recorrido
    return mayor_hasta_ahora

numeros=[2, 4, 5, 23, 53]
resultado = encontrar_mayor(numeros)
print(f"El numero mas grande de la lista: {numeros} es: {resultado}")



def numeros(lista):
    if not lista:
        return None

    numMayor = lista[0]
    for i in lista:
        if i > numMayor:
            numMayor = i
    return numMayor
listnum = [3, 5, 46, 234, 23, 435, 65, 23, 75, 685]

resultado = numeros(listnum)

print(f"El numero mas grande es: {resultado} en la lista: {listnum}")



