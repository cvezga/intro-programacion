__ESC = chr(27)
__RESET_ALL_ATTRIBUTES = "".join((__ESC, "[0m"))
__SET_BOLD = "".join((__ESC, "[1m"))
__SET_HALF_BRIGHT = "".join((__ESC, "[2m"))
__SET_UNDERSCORE = "".join((__ESC, "[4m"))

__SET_RED_FOREGROUND = "".join((__ESC,"[31m"))
__SET_GREEN_FOREGROUND = "".join((__ESC,"[32m"))
__SET_BROWN_FOREGROUND = "".join((__ESC,"[33m"))
__SET_BLUE_FOREGROUND = "".join((__ESC,"[34m"))
__SET_MAGENTA_FOREGROUND = "".join((__ESC,"[35m"))
__SET_CYAN_FOREGROUND = "".join((__ESC,"[36m"))
__SET_WHITE_FOREGROUND = "".join((__ESC,"[37m"))

__ERASE_WHOLE_DISPLAY = "".join((__ESC,"[2J"))

def setRedForeground():
    print(__SET_RED_FOREGROUND, end='')

def setGreenForeground():
    print(__SET_GREEN_FOREGROUND, end='')

def setBrownForeground():
    print(__SET_BROWN_FOREGROUND, end='')

def setBlueForeground():
    print(__SET_BLUE_FOREGROUND, end='')

def setMagentaForeground():
    print(__SET_MAGENTA_FOREGROUND, end='')

def setCyanForeground():
    print(__SET_CYAN_FOREGROUND, end='')

def setWhiteForeground():
    print(__SET_WHITE_FOREGROUND, end='')

def resetAllAttributes():
    print(__RESET_ALL_ATTRIBUTES, end='')

def eraseWholeDisplay():
    print(__ERASE_WHOLE_DISPLAY, end='')