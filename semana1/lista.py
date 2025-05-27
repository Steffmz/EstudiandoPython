lista_de_numeros = [2, 5, 1, 8]

suma_acumulada = 0                       #va guardando la suma y comienza en 0
                                         #porque todavia no he sumado nada

for numero in lista_de_numeros:          #guardo cada numero en mi lista_de_numeros
    suma_acumulada = suma_acumulada + numero            #se añade y se asigna, es += o suma_acumulada = suma_acumulada + numero
print(f"La suma es: {suma_acumulada}")

#osea lo que hay en numeros (que en este caso ya recorrio la lista y los guardo), 
#se añade y se asigna al contador suma_acumulada










lista = [2, 5, 1, 8]
suma_total = sum(lista)
print(f"La suma es: {suma_total}")