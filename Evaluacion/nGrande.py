# Escribe un programa que encuentre el número más grande en una
# lista de números. No uses la función max() integrada de Python
# (la idea es que implementes la lógica tú mismo).

lista=[3, 54, 2, 1, 10]

numMayor = lista[0]

for num in lista:
    if num > numMayor:
        numMayor =num
print("El numero mayor es:",numMayor)