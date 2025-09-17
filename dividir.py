def dividir(a, b):
    """
    Función para dividir dos números.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
    
    Returns:
        float: El cociente de los dos números
        
    Raises:
        ZeroDivisionError: Si el divisor es cero
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b