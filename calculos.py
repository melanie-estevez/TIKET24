def calcular_cuota(prestamo, tasa_interes_anual, plazo_meses):
    tasa_mensual = tasa_interes_anual / 100 / 12
    cuota_mensual = (prestamo * tasa_mensual) / (1 - (1 + tasa_mensual) ** -plazo_meses)
    return cuota_mensual

from datetime import datetime

def calcularEdad(anioNacimiento):
    anioActual = datetime.now().year
    
    if anioNacimiento < 0 or anioNacimiento > anioActual:
        return -1
    
    edad = anioActual - anioNacimiento
    return edad

def encontrarMayor(a, b, c):
    return max(a, b, c)

def encontrarMenor(a, b, c, d):
    return min(a, b, c, d)
