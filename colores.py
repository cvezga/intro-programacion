ESC = chr(27)
RESET_ALL_ATTRIBUTES = "".join((ESC, "[0m"))
SET_BOLD = "".join((ESC, "[1m"))
SET_HALF_BRIGHT = "".join((ESC, "[2m"))
SET_UNDERSCORE = "".join((ESC, "[4m"))

SET_RED_FOREGROUND = "".join((ESC,"[31m"))
SET_GREEN_FOREGROUND = "".join((ESC,"[32m"))
SET_BROWN_FOREGROUND = "".join((ESC,"[33m"))
SET_BLUE_FOREGROUND = "".join((ESC,"[34m"))
SET_MAGENTA_FOREGROUND = "".join((ESC,"[35m"))
SET_CYAN_FOREGROUND = "".join((ESC,"[36m"))
SET_WHITE_FOREGROUND = "".join((ESC,"[37m"))

def setRedForeground():
    print(SET_RED_FOREGROUND, end='')

def setGreenForeground():
    print(SET_GREEN_FOREGROUND, end='')

def setBrownForeground():
    print(SET_BROWN_FOREGROUND, end='')

def setBlueForeground():
    print(SET_BLUE_FOREGROUND, end='')

def setMagentaForeground():
    print(SET_MAGENTA_FOREGROUND, end='')

def setCyanForeground():
    print(SET_CYAN_FOREGROUND, end='')

def setWhiteForeground():
    print(SET_WHITE_FOREGROUND, end='')

def resetAllAttributes():
    print(RESET_ALL_ATTRIBUTES, end='')
