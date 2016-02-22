from urllib2 import *
import datetime
 
 
 
print("Fb py v0.1")
##nombre=input("ingrese nombre para archivo de salida")
print("---")
archivo= open("test.txt","w")
info=""
cadena = ""
 
error404=0
suma=0
guardados=0

def existe(DATA):
   if "no se pudo encontrar" in str(DATA).lower():
      return false
   else:
      return true
 
url = "http://facebook.com/"
print("web seleccionada: "+url)

 
 
Minimo=int(input("ingrese un valor minimo de ID"))
Maximo=int(input("ingrese un valor maximo de ID"))
 
contador=0
print("hora de inicio "+str(datetime.datetime.now()))
print("id minimo:"+str(Minimo)+" id maximo:"+str(Maximo))
for id in range(Minimo,Maximo):
   aux = url+str(id)
   print aux
   try:
      usock = urllib2.urlopen(aux)
      print "estamos en try"
      DATA = usock.read()
      if (existe(DATA)):
            info=info+str(DATA)+"\n"
      usock.close()               
      print(aux)
      print(info)
 
 
      if contador == 5: # <---- Aca pone cada cuantos id queres guardar, yo le puse un numero bajo para probar
         contador=0
         guardados+=1
         salida=str(guardados)+".txt"
         print(salida+" salida")
         archivo=open(salida,"w")
         archivo.write(info)
         archivo.close()
         info=""
      else:
         contador+=1
   except :
      error404+=1
      continue
 
   cadena=cadena+aux+"\n"
