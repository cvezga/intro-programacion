
a = float(input("Digite dimencion a: "))
b = float(input("Digite dimencion b: "))
c = float(input("Digite dimencion c: "))

if a ** 2 == b ** 2 + c ** 2:
    print("El triangulo es recto")
elif b ** 2 == a ** 2 + c ** 2:
    print("El triangulo es recto")
elif c ** 2 == a ** 2 + b ** 2:   
    print("El triangulo es recto") 
elif a == b and b == c:
    print("El triangulo es equilatero") 
elif a == b or b == c or a==c:
    print("El triangulo es isoceles")
else:
    print("El triangulo es escaleno")      

axo = 100    
if True:
    es_bisiesto=axo%4 == 0 and(axo%100!=0 or axo%400 == 0 )    
    if True:
        print("x")
