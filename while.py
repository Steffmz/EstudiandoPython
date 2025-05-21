def cuenta_atras():
    numero_cuenta_atras = int(input("ingresa un numero para la cuenta regresiva: "))

    while numero_cuenta_atras > 0:
        print(numero_cuenta_atras)
        numero_cuenta_atras -=1
    print("¡Despegue!")

#Objetivo: Escribe un programa que pida al usuario que ingrese un número positivo.
#El programa debe seguir pidiendo el número hasta que el usuario ingrese un número
#que sea efectivamente mayor que cero. Una vez que se ingrese un número positivo 
#el programa debe imprimir un mensaje confirmándolo.




numero = int(input("Introduce un numero positivo: "))

while numero <= 0:
        print("Sigue intentandolo")
        numero = int(input("Introduce un numero positivo: "))
print(f"¡Excelente! {numero} es un numero positivo")


