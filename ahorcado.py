import urllib.request as urllib2
import json
import colores

def letras(palabra):
    letras = []
    for letra in palabra:
        letras.append(letra)
    return letras;    

def sin_letras(palabra):
    letras = []
    for letra in palabra:
        letras.append('_')
    return letras;    

def concatena(arreglo):
    letras = ""
    for letra in arreglo:
        letras += letra + " "
    return letras; 

def rellena(letras,sinletras,caracter):
    i =0;
    nueva_sinletras = []
    contador = 0
    for c in letras:
        if( c == caracter ):
            nueva_sinletras.append(c)
            if(sinletras[i] == "_"):
                contador += 1
        elif sinletras[i] == "_":
            nueva_sinletras.append('_')
        else:
            nueva_sinletras.append(sinletras[i])    
        i+=1
    return nueva_sinletras,contador

response = urllib2.urlopen("https://palabras-aleatorias-public-api.herokuapp.com/random")
result = json.load(response)

palabra = result['body']['Word'].upper()


_letras = letras(palabra)
_sinletras = sin_letras(palabra)

malas = 0

letras_leidas = ""

while True:

    
    if(malas>8):
        print(f'Perdiste! la palabra era: {palabra}')
        break

    colores.eraseWholeDisplay()

    #print(palabra)
  
    print(f' turno: {malas}/8')
    print()
    print( '     +------+     ')
    print( '     | /    |     ')
    print( '     |/    ( )    ')
    print( '     |     /|\    ')
    print(f'     |      |        {concatena(_sinletras)}')
    print( '     |     / \    ')
    print( '     |            ')
    print( '------------------') 
    print(letras_leidas)

    caracter = input('Digite un caracter: ').upper()
    letras_leidas += caracter

    _sinletras,contador = rellena(_letras,_sinletras,caracter)

    if contador == 0:
        malas +=1



