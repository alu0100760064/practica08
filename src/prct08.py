#! /urs/bin/python
#! encoding: UTF-8

import modulo

def error(nro_intervalos,nro_test, umbral):
  aprox1= modulo.PI350T
  fallos=0
  for i in range(1, test+1): 
     aprox2=modulo.aprox(nro_intervalos)
     valor=abs(aprox1-aprox2)
     if(valor<=umbral):
       print "no hay eerores"
     else:
       fallos=fallos+1
  porc=(fallos *100) / nro_test
  return porc

  
if __name__=="__main__": 
  import sys
  parametro1 = sys.argv[0]
  if(len(sys.argv)==1):
    m= int (raw_input('Introduzca m: '))
    umbral= float (raw_input('Introduzca el umbral: '))   
    test= int (raw_input('Introduzca test:    '))
  elif (len(sys.argv)==4):
    m= int(sys.argv[1])
    umbral= int(sys.argv[2])
    test= int(sys.argv[3])
  else:
    print "el modo de uso es %s <numero intervalo> <numero veces>" % parametro1
    m=0
    umbral=0.0
    test=0
  print error(m,test,umbral)
 