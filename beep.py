# Control character 
# 07 BEL 
print(chr(7))

# public static final char[] SET_RED_FOREGROUND = {ESC, '[', '3', '1', 'm'}; // 31        set red foreground
SET_RED_FOREGROUND = (chr(27),"[","3", "1", "m")
print("".join(SET_RED_FOREGROUND))
print("rojo")