import colores

colores.setRedForeground()
print(colores.SET_RED_FOREGROUND, end='')
print("rojo")

colores.setGreenForeground()
print("verde")

colores.setBrownForeground()
print("marron")

colores.setBlueForeground()
print("azul")

colores.setMagentaForeground()
print("magenta")

colores.setCyanForeground()
print("cyan")

colores.setWhiteForeground()
print("blanco")

colores.resetAllAttributes()
print("normal")