def calcularCuota(monto, tasa_interes, meses):
    tasa_mensual = tasa_interes / 100 / 12
    cuota = monto * (tasa_mensual * (1 + tasa_mensual) ** meses) / ((1 + tasa_mensual) ** meses - 1)
    return cuota
