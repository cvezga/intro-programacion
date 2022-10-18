
monto_prestamo = float(input("Monto del prestamo? "))
modena = input("Moneda? (Colones/Dolares) ")
meses = int(input("Plazo en meses? (12,24,38,42,60,120,240,360) "))




if modena == 'Colones':
    interes_anual = 0.15
elif modena == 'Dolares':
    interes_anual = 0.12 
else:
    print("La moneda debe ser Colones o Dolares")
    interes_anual = 0

if meses != 12 and meses != 24 and meses != 38 and meses != 42 and meses != 60 and meses != 120 and meses != 240 and meses != 360:    
    print("Plazo en meses no es valido. Debe ser uno de lis siguientes plazos:  12,24,38,42,60,120,240 o 360")
    meses = 0


if interes_anual > 0 and meses > 0:
    interes_mensual = interes_anual / 12
    cuota_interes_mensual = monto_prestamo * interes_mensual 
    cuota_capital_mensual = monto_prestamo / meses
    total_cuota_mensual = cuota_interes_mensual + cuota_capital_mensual
    print("La cuota mensual es: ", round(total_cuota_mensual,2))

