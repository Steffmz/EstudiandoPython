import time

while True:
    try:
        num1 = int(input("Introduce un número: "))
        time.sleep(0.5)
        num2 = int(input("Introduce un segundo número: "))
    except ValueError:
        print("❌ Por favor introduce solo números válidos.")
        continue

    print("\nIntroduce la operación:")
    opciones = input("suma, resta, multi, division (o 'salir' para terminar): ").lower()

    if opciones == "suma":
        print(f"✅ El resultado de la suma es: {num1 + num2}")

    elif opciones == "resta":
        print(f"✅ El resultado de la resta es: {num1 - num2}")

    elif opciones == "multi":
        print(f"✅ El resultado de la multiplicación es: {num1 * num2}")

    elif opciones == "division":
        if num2 == 0:
            print("❌ No se puede dividir entre 0")
        else:
            print(f"✅ El resultado de la división es: {num1 / num2}")

    elif opciones == "salir":
        print("👋 Programa terminado.")
        break

    else:
        print("⚠️ Operación no válida. Intenta de nuevo.")
    
    print("\n---\n")  # Separador visual
