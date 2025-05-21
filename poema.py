#nombre_del_fichero = input("Introduce el nombre del archivo para guardar un poema: ")

#with open(nombre_del_fichero, 'w') as archivo_para_escribir:  
    #print("introduce las lineas del poema. Escribe 'FIN' para terminar.")
    #while True:
        #linea_actual = input("Linea > ")
        #if linea_actual.lower() == 'fin':
            #break
        #else:
            #archivo_para_escribir.write(linea_actual + '\n')
#print(f"Poema guardado en: {nombre_del_fichero}")


nombre_del_poema = input("Ingresa el nombre del poema: ")

with open(nombre_del_poema, 'r') as archivo_para_leer:
    for recorrido in archivo_para_leer:
        print(recorrido, end='')
print("\n\n--- Fin del poema ---")




