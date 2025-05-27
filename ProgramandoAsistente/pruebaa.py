def determinar_tipo_cliente(puntos_acumulados, participacion_natacion, participacion_ciclismo):
    """
    Determina el tipo de cliente basado en los puntos acumulados y la participación
    en actividades deportivas.

    Args:
        puntos_acumulados (int): Los puntos acumulados por el cliente.
        participacion_natacion (bool): True si el cliente participa en natación, False de lo contrario.
        participacion_ciclismo (bool): True si el cliente participa en ciclismo, False de lo contrario.

    Returns:
        str: El tipo de cliente.
    """
    if puntos_acumulados >= 1000:
        if participacion_natacion:
            if participacion_ciclismo:
                return "Cliente Diamante"  # 💎
            else:
                return "Cliente Oro"       # 🥇
        else:  # No participación en natación
            if participacion_ciclismo:
                return "Cliente Oro"       # 🥇
            else:
                return "Cliente Plata"     # 🥈
    else:  # Puntos acumulados < 1000
        if participacion_natacion:
            if participacion_ciclismo:
                return "Cliente Bronce"    # 🥉
            else:
                return "Cliente Plata"     # 🥈
        else:  # No participación en natación
            if participacion_ciclismo:
                return "Cliente Bronce"    # 🥉
            else:
                return "Cliente Platino"   # ✨ (Ojo, el árbol original dice Platino aquí)