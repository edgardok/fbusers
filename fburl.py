import urllib2

def existe(url):
    return True
    return False


id=0
archivo=open("fbusers.txt","w")
cadena = ""
url = 'https://www.facebook.com/' 
while id<10000000000000:  
    aux = url+str(id)
    print aux
    id+=1
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
