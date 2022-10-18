dia = int(input("dia? "))
mes = int(input("mes? "))
axo = int(input("año? "))


es_valido = True

if axo < 1:
  print("El año no puede ser menor de 1")
  es_valido = False

if mes<1 or mes>12:
  print("El mes debe estar entre 1 y 12")
  es_valido = False

if dia<1 or dia >31:
    print("el dia es invalido")
    es_valido = False

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 and mes == 12:
     if dia<1 or dia>31:
          print("el dia debe estan entre 1 y 31")
          es_valido = False

if  mes == 4 or mes == 6 or mes ==  9 or mes == 11:
     if dia<1 or dia>30:
          print("el dia debe estan entre 1 y 30")
          es_valido = False

if mes == 2:
     es_bisiesto = axo % 4 == 0 and ( axo % 100 != 0 or axo % 400 == 0 )
     print("Es bisiesto",es_bisiesto)
     if es_bisiesto and ( dia <1 or dia>29):
        print("el dia debe estar comprendidi entre 1 y 29")
        es_valido = False
     elif  not es_bisiesto and ( dia <1 or dia>28):
        print("el dia debe estar comprendidi entre 1 y 28")
        es_valido = False

if es_valido:
    print("La fecha aes valida")           
else:
    print("La fecha no es valida")               