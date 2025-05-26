lista = [3, 6, 43, 2, 132]

numerogrande = lista[0]

for recorrido in lista:
    if recorrido > numerogrande:
        numerogrande = recorrido
print("El numero mas grande es:", numerogrande)


lista2 = [24, 54, 12, 4324]

print("El numero mas grande es:", max(lista2))