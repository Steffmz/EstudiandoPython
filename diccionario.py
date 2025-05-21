def agenda():
    agenda = [
        {
            "nombre": "Wilson",
            "celular": "1122334455",
            "correo": "w@m.com"
        },
        {
            "nombre": "xiomara",
            "celular": "3223341321",
            "correo": "x@r.com"

        },
    ]
    for contacto_actual in agenda:
        print(f"\nNombre: {contacto_actual['nombre']}") # Imprime el nombre del contacto actual
        print(f"Teléfono: {contacto_actual['celular']}") # Indentado para claridad
        print(f"Email: {contacto_actual['correo']}")
agenda()

def buscar_contacto(agenda, nombre_buscado):
    if not agenda:
        return None

    for nombre_buscado in agenda:














def diccionario():
    #Diccionario = Array
    persona1={
        "nombre" : "wil",
        "telefono" : "3332456334",
        "email" : "w@m.com"
    }

    #Imprimimos lo que querramos ver en el diccionario
    print(f"{persona1['nombre']}")

    print(f"{persona1['telefono']}")

    #Aqui agregamos un nuevo dato al diccionario que es la ciudad
    persona1["ciudad"] = "Bogotá"
    print(f"{persona1["ciudad"]}")

    #Modificamos un dato existente con una nueva informacion
    persona1["email"] = "Xio@r.com"
    print(f"{persona1['email']}")


    print("\nInformación de contacto actualizada:")
    print(persona1)
    print("\n")
    for llave, valor in persona1.items():
        print(f"La llave es: {llave.capitalize()} y el valor es: {valor}")

