import random as r
import math as m

min = 1
max = 100

maxop = 7

numero = r.randint(1,100)

adivine = "n"
while adivine != "s":
    adivine = input(f"Es {numero}?")
    if adivine!="s":
       mm = input(f"Es menor o mayor? (<,>)?") 
       if mm=="<":
          max=numero-1
       elif mm==">":
          min=numero+1
       numero = m.trunc((min+max)/2)
    elif adivine=="s":
        print("GANE!!!!")         
    maxop -= 1
    if( maxop == 0 ):
        print("Tu ganaste!")
        break   