import urllib2

def existe(url):
    return True
    return False

limite=1000000000000000

id=0
archivo=open("fbusers.txt","w")
cadena = ""
url = 'https://www.facebook.com/' 
for id in range(limite):  
    aux = url+str(id)
    print aux
    try:
        usock = urllib2.urlopen(aux)
        DATA = usock.read() 
        usock.close()
    except :
        continue
        if (existe(DATA)):
            cadena=cadena+aux+"\n"
    archivo.write(cadena)
    archivo.close
