import sys
import glob

#TAKE ENRICHMENT DATA, OUTPUT SIZES OF ENRICHED COMMS
def EnrichmedSize(path):
  ematrix = {};
  files=glob.glob(path)
  coms = set()
  procs = set()

  for filename in files:
      splitpath = filename.split("/") #
      filebasename = splitpath[len(splitpath)-1] #make sure to split only actual filenames, regardless of full path
      base_datos, fenotipo, isla, comunidad = filebasename.split('_')
      comunidad = comunidad.split('.')[0]
      komunidad = fenotipo+"_"+isla+"_"+comunidad
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
          #n_genes = n_genes.strip('"')
          n_genes = n_genes.rstrip()

          procs.add(proceso)
          #coms.add(comunidad)
          coms.add(komunidad)
          #coms.add(filebasename)
          if not proceso in ematrix:
               ematrix[proceso] = dict()

          #ematrix[proceso][comunidad] = adj_pvalue
          #ematrix[proceso][komunidad] = adj_pvalue
          ematrix[proceso] = n_genes

      f.close()

  return ematrix, coms, procs


def SaveMatrix(filename, ematrix, procs):

  file = open(filename, 'w')

  #coms = list(coms)
  #coms.sort()
  procs = list(procs)
  procs.sort()

  #write header
  #for c in coms:
  #    file.write("\t{}".format(c))
  #file.write("\n")

  #write content
  for p in procs:
        file.write("{}".format(p))
        file.write("\t{}".format(ematrix[p]))
        file.write("\n")

        #~ for c in coms:
#~ 
            #~ if c in ematrix[p]:
                #~ pvalue = ematrix[p][c]
            #~ else:
                #~ pvalue = 1
#~ 
            #~ file.write("\t{}".format(pvalue))
#~ 
        #~ file.write("\n")

  file.close()



dr = sys.argv[1] #shaped as prueba/COMMUNITIES/prueba_I001/
directory = dr+"/"
basename = sys.argv[2]
#basename = dr.split(sep = "/")[len(dr.split(sep = "/")) -1]
#filename = sys.argv[2]
#ematrix, coms, procs = EnrichmentMatrix(path)
#SaveMatrix(filename,ematrix, coms, procs)

path = directory+'GOBP_*.csv'
ematrix, coms, procs = EnrichmedSize(path)
SaveMatrix(directory+basename+'_GOBP.procsize',ematrix, procs)

path = directory+'GOCC_*.csv'
ematrix, coms, procs = EnrichmedSize(path)
SaveMatrix(directory+basename+'_GOCC.procsize',ematrix, procs)

path = directory+'GOMF_*.csv'
ematrix, coms, procs = EnrichmedSize(path)
SaveMatrix(directory+basename+'_GOMF.procsize',ematrix, procs)

path = directory+'KEGG_*.csv'
ematrix, coms, procs = EnrichmedSize(path)
SaveMatrix(directory+basename+'_KEGG.procsize',ematrix, procs)
