#usage Analisis_Infomap3.py map_file outdir prefix

import sys
import csv

def leer(results):
  data = []
  ENTRADA = open(results,"r")

  for linea in ENTRADA:
    cadena = linea.split()
    data.append(cadena)
  ENTRADA.close()
  
  return data  ## areglo de lineas
  

data = leer(sys.argv[1])

k = 1
m = int(data[0][2])
ini = 0
fin = 0

for i in data:
  if( i[0]=='*Nodes'):
    ini = k
  elif( i[0]=='*Links'):
    fin = k    
  k = k+1  
 

A = []
B = []
M = []

for i in range(ini,fin-1,1):
  mod = data[i][0].split(":")
  gen = data[i][1].replace('"','')
  
  A.append((mod[0], gen))
  

t = 1
for i in A:
  if (int(i[0]) == t):
    B.append(i[1])
  else:
    t=t+1
    M.append(B)
    B = []
    B.append(i[1])
M.append(B)
 
path = sys.argv[2]
prefix = sys.argv[3]
filename = path+prefix+'_Infomap_TRANSP.csv'
file = open(filename, 'w');
writer = csv.writer(file)
for item in M:
    writer.writerow(item)
file.close()

k=1
for item in M:
  filename = path+prefix+'_C'+str(k).zfill(3)+'.txt'
  file = open(filename, 'w');
   
  for i in range(len(item)):
    #print item[i]
    file.write("%s\n" % item[i])
  
  file.close()    
  k=k+1





