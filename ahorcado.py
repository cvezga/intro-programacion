import urllib.request as urllib2
import json
import colores

response = urllib2.urlopen("https://palabras-aleatorias-public-api.herokuapp.com/random")
result = json.load(response)

palabra = result['body']['Word'].upper()

colores.eraseWholeDisplay()


print( '     +------+     ')
print( '     | /    |     ')
print( '     |/    ( )    ')
print( '     |     /|\    ')
print(f'     |      |        {palabra}')
print( '     |     / \    ')
print( '     |            ')
print( '------------------') 