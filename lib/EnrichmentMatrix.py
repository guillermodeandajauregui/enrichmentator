import sys
import glob

def EnrichmetMatriz(path):
  dik = {};
  files=glob.glob(path)
  l = []

  for file in files:
      a = file.split('_')
      b = a[len(a) - 1]
      c = b.split('.')
      f = open(file, 'r')
      l.append(c[0])
      
      title = True
      cadena =  []
      for linea in f:
          if title:
              title = False
              continue
          cadena = linea.split('\t')
      if cadena and (cadena[0].strip('"')) in dik:
          dik[cadena[0].strip('"')].append((c[0].strip(),cadena[7].strip()))
      elif cadena:
          dik[cadena[0].strip('"')] = [(c[0].strip(),cadena[7].strip())]
      
      f.close()      
#      del(dik['""'])
      l.sort()

  return dik,l


def FileMatrix(filename,diccionario,coms):
  PosComs = {}
  M = [[1 for x in range(len(coms)+1)] for x in range(len(diccionario)+1)]
  k=1

  M[0][0] = ""
  for i in coms:
    M[0][k] = i
    PosComs[i] = k
    k=k+1
    
  k=1  
  for e in diccionario:
    M[k][0] = e
    for i in diccionario[e]:
      for j in PosComs:
          if i[0] == j:
              M[k][PosComs[j]] = i[1]
    k=k+1
    
  file = open(filename, 'w')
  for i in range(len(M)):
    for j in range(len(M[0])):
      file.write("%s\t" % M[i][j])
    file.write("\n")
  file.close()  
  
  
  
dr = sys.argv[1] #shaped as prueba/COMMUNITIES/prueba_I001 
directory = dr
basename = sys.argv[2]
#basename = dr.split(sep = "/")[len(dr.split(sep = "/")) -1]
#filename = sys.argv[2]
#diccionario,coms = EnrichmetMatriz(path)
#FileMatrix(filename,diccionario,coms)

path = directory+'GOBP_*.csv'
diccionario,coms = EnrichmetMatriz(path)
FileMatrix(directory+basename+'_GOBP.csv',diccionario,coms)

path = directory+'GOCC_*.csv'
diccionario,coms = EnrichmetMatriz(path)
FileMatrix(directory+basename+'_GOCC.csv',diccionario,coms)

path = directory+'GOMF_*.csv'
diccionario,coms = EnrichmetMatriz(path)
FileMatrix(directory+basename+'_GOMF.csv',diccionario,coms)

path = directory+'KEGG_*.csv'
diccionario,coms = EnrichmetMatriz(path)
FileMatrix(directory+basename+'_KEGG.csv',diccionario,coms)