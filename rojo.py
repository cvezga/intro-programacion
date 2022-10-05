# char[] SET_RED_FOREGROUND = {ESC, '[', '3', '1', 'm'}; // set red foreground
SET_RED_FOREGROUND = (chr(27),"[","3", "1", "m")
print("".join(SET_RED_FOREGROUND))

print("rojo")