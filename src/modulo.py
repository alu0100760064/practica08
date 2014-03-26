#! /urs/bin/python
#! encoding: UTF-8

PI350T = 3.14159265358979323846264338327950288
def aprox(n):
  s=0.0
  for i in range(1,n+1):
    xi= (i-0.5)/n
    fxi=4.0/(1+xi**2)  
    s += fxi
  R=1.0/n*s
  return R
  

if __name__=="__main__": 
  import sys
  print "%.35g" % PI350T
  parametro1 = sys.argv[0]
  if(len(sys.argv)==1):
    print "el modo de uso es %s <numero intervalo> <numero veces>" % parametro1
    n= int (raw_input('Introduzca n: '))
    m= int (raw_input('Introduzca m: '))   
  elif (len(sys.argv)==3):
    n= int(sys.argv[1])
    m= int(sys.argv[2])
  else:
    print "el modo de uso es %s <numero intervalo> <numero veces>" % parametro1
    n=0
    m=0
  l= [ ]
  for i in range(1, m+1):
     api = aprox(n*i)
     l=l+[api]
  print l