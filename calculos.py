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

def determinarResultadosIMC(imc):
    if 0 <= imc <=16:
        return "Delgadez severa"
    elif 16 <imc <=17:
        return "Delgadez moderada"
    elif 17 < imc <=18.5:
        return "Delgadez leve"
    elif 18.5 < imc <=25:
        return "Peso normal"
    elif 25 < imc <= 30:
        return "Sobrepeso"
    elif 30 < imc <=35:
        return "Obesidad grado 1"
    elif 35 < imc <= 40:
        return "Obesidad grado 2"
    elif imc >40:
        return "Obesidad grado 3"
    else:
        return "IMC fuera de rango"


def encontrarMayor(a, b, c):
    return max(a, b, c)

def encontrarMenor(a, b, c, d):
    return min(a, b, c, d)
