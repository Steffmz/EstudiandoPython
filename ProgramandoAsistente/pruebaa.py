
puntos_acumulados = 1500
participacion_natacion = True
participacion_ciclismo = True  


tipo_cliente = ""

if puntos_acumulados >= 1000:
    if participacion_natacion:
        if participacion_ciclismo:
            tipo_cliente = "Cliente Diamante"  # 💎
        else:
            tipo_cliente = "Cliente Oro"       # 🥇
    else: 
        if participacion_ciclismo:
            tipo_cliente = "Cliente Oro"       # 🥇
        else:
            tipo_cliente = "Cliente Plata"     # 🥈
else:
    if participacion_natacion:
        if participacion_ciclismo:
            tipo_cliente = "Cliente Bronce"    # 🥉
        else:
            tipo_cliente = "Cliente Plata"     # 🥈
    else: 
        if participacion_ciclismo:
            tipo_cliente = "Cliente Bronce"    # 🥉
        else:
            tipo_cliente = "Cliente Platino"   # ✨


print(f"El tipo de cliente es: {tipo_cliente}")
