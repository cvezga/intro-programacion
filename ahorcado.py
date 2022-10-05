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
    for c in letras:
        if( c == caracter ):
            nueva_sinletras.append(c)
        elif sinletras[i] == "_":
            nueva_sinletras.append('_')
        else:
            nueva_sinletras.append(sinletras[i])    
        i+=1
    return nueva_sinletras

response = urllib2.urlopen("https://palabras-aleatorias-public-api.herokuapp.com/random")
result = json.load(response)

palabra = result['body']['Word'].upper()


_letras = letras(palabra)
_sinletras = sin_letras(palabra)

turno = 0

while True:

    turno += 1

    if(turno>8):
        print(f'Perdiste! la palabra era: {palabra}')
        break

    colores.eraseWholeDisplay()

    #print(palabra)
  
    print(f' turno: {turno}')
    print()
    print( '     +------+     ')
    print( '     | /    |     ')
    print( '     |/    ( )    ')
    print( '     |     /|\    ')
    print(f'     |      |        {concatena(_sinletras)}')
    print( '     |     / \    ')
    print( '     |            ')
    print( '------------------') 

    caracter = input('Digite un caracter: ')

    _sinletras = rellena(_letras,_sinletras,caracter)



