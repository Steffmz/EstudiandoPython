
print('Ingrese la cantidad de puntos acumulados en total:')

try:
    puntos = int(input())
except ValueError:
    print("Error: La cantidad de puntos debe ser un número entero válido.")
    exit()

print('Participo en las competencias de natacion? S / N:')
natacion = input().upper() 

print('Participo en las competencias de ciclismo? S / N:')
ciclismo = input().upper() 
if puntos >= 1000:
    if natacion == 'S':
        if ciclismo == 'S':
            print('Cliente Diamante')
        elif ciclismo == 'N':
            print('Cliente Oro')

    elif natacion == 'N':
        if ciclismo == 'S':
            print('Cliente Oro')

            print('Cliente Plata')
elif puntos < 1000:
    if natacion == 'S':
        if ciclismo == 'S':
            print('Cliente Plata')
        elif ciclismo == 'N':
            print('Cliente Bronce')
    elif natacion == 'N':
        if ciclismo == 'S':
            print('Cliente Bronce')  
        elif ciclismo == 'N':
            print('Cliente Platino')
