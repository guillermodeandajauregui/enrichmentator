import sys
import glob

def EnrichmentMatrix(path):
  ematrix = {};
  files=glob.glob(path)
  coms = set()
  procs = set()

  for filename in files:
      base_datos, fenotipo, isla, comunidad = filename.split('_')
      comunidad = comunidad.split('.')[0]
      f = open(filename, 'r')

      title = True
      for linea in f:
          # skip title line
          if title:
              title = False
              continue

          (proceso, n_universo,  n_genes, total_hits, expected_hits, observerd_hits, pvalue, adj_pvalue) = linea.split('\t')
          proceso = proceso.strip('"')
          adj_pvalue = adj_pvalue.rstrip()

          procs.add(proceso)
          coms.add(comunidad)
          if not proceso in ematrix:
               ematrix[proceso] = dict()

          ematrix[proceso][comunidad] = adj_pvalue

      f.close()

  return ematrix, coms, procs


def SaveMatrix(filename, ematrix, coms, procs):

  file = open(filename, 'w')

  coms = list(coms)
  coms.sort()
  procs = list(procs)
  procs.sort()

  #write header
  for c in coms:
      file.write("\t{}".format(c))
  file.write("\n")

  #write content
  for p in procs:
        file.write("{}".format(p))

        for c in coms:

            if c in ematrix[p]:
                pvalue = ematrix[p][c]
            else:
                pvalue = 1

            file.write("\t{}".format(pvalue))

        file.write("\n")

  file.close()



dr = sys.argv[1] #shaped as prueba/COMMUNITIES/prueba_I001
directory = dr
basename = sys.argv[2]
#basename = dr.split(sep = "/")[len(dr.split(sep = "/")) -1]
#filename = sys.argv[2]
#ematrix, coms, procs = EnrichmentMatrix(path)
#SaveMatrix(filename,ematrix, coms, procs)

path = directory+'GOBP_*.csv'
ematrix, coms, procs = EnrichmentMatrix(path)
SaveMatrix(directory+basename+'_GOBP.csv',ematrix, coms, procs)

path = directory+'GOCC_*.csv'
ematrix, coms, procs = EnrichmentMatrix(path)
SaveMatrix(directory+basename+'_GOCC.csv',ematrix, coms, procs)

path = directory+'GOMF_*.csv'
ematrix, coms, procs = EnrichmentMatrix(path)
SaveMatrix(directory+basename+'_GOMF.csv',ematrix, coms, procs)

path = directory+'KEGG_*.csv'
ematrix, coms, procs = EnrichmentMatrix(path)
SaveMatrix(directory+basename+'_KEGG.csv',ematrix, coms, procs)