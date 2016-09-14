import sys
import glob

def EnrichmetMatriz(path):
  dict = {};
  files=glob.glob(path)
  l = []

  for file in files:
      a = file.split('_')
      b = a[len(a) - 1]
      c = b.split('.')
      f = open(file, 'r')
      l.append(c[0])
      
      for linea in f:
	cadena = linea.split('\t')
	if (cadena[0].strip('"')) in dict:
	  dict[cadena[0].strip('"')].append((c[0].strip(),cadena[7].strip()))
	else:
	  dict[cadena[0].strip('"')] = [(c[0].strip(),cadena[7].strip())]
      
      f.close()      
      del dict['']
      l.sort()

  return dict,l


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
  
  
  
directory = sys.argv[1]

#filename = sys.argv[2]
#diccionario,coms = EnrichmetMatriz(path)
#FileMatrix(filename,diccionario,coms)

path = directory+'/comunidad_GS_GO_BP_*.csv'
diccionario,coms = EnrichmetMatriz(path)
FileMatrix(directory+'_GS_GO_BP.csv',diccionario,coms)

path = directory+'/comunidad_GS_GO_CC_*.csv'
diccionario,coms = EnrichmetMatriz(path)
FileMatrix(directory+'_GS_GO_CC.csv',diccionario,coms)

path = directory+'/comunidad_GS_GO_MF_*.csv'
diccionario,coms = EnrichmetMatriz(path)
FileMatrix(directory+'_GS_GO_MF.csv',diccionario,coms)

path = directory+'/comunidad_kegg_*.csv'
diccionario,coms = EnrichmetMatriz(path)
FileMatrix(directory+'_kegg.csv',diccionario,coms)

  











