num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

opciones=input("Elija la opcion a realizar + - * / : ")

if opciones == "+":
    print(f"El resultado de la suma es: {num1 + num2}")
elif opciones == "-":
    print(f"El resultado de la resta es: {num1 - num2}")
elif opciones == "*":
    print(f"El resultado de la multiplicacion es: {num1 * num2}")
elif opciones == "/":
    print(f"El resultado de la division es: {num1 / num2}")
else:
    print("Error al elegir la opcion, intente de nuevo")