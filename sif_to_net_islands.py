import networkx as nx
import pandas as pd
#import pickle
import sys
# RUN # python sif_to_net_islands.py NETWORK.sif 
########## SYSTEMS ARGUMENTS

NW = sys.argv[1]

### GRAPH LOADING FUNCTION
def graphfromsif(sif):
    s = pd.read_table(sif,
                      header =None,
                      delim_whitespace=True)
    s = s[[0,2,1]]
    s = s.values.tolist()
    def formatfunction(lista):
        return "{} {} {}".format(lista[0], lista[1], lista[2])
    reformat = []
    for elem in s:
        reformat.append(formatfunction(elem))
    g = nx.parse_edgelist(reformat, 
                           nodetype = str, 
                           data=(('weight',float),)
                           )
    return(g)
#########
#LOAD GRAPH
#########

G = graphfromsif(NW)

NOMBRE = NW.split(".")
#########
#BREAK INTO ISLANDS
#########
if not nx.is_connected(G):
    L = sorted(nx.connected_components(G))
    a = len(L)
    b = len(L[0])
    c = len(L[a-1])
    print("Se tienen",a,"componentes!")
    print("El mayor es de",b,"nodos.")
    print("El menor es de",c,"nodos.")
    #tamano = int(raw_input("Ingresa el tamaño minimo de los componentes a considerar  "))
    comp_num = 1
    #lista_graphs =  sorted(list(nx.connected_component_subgraphs(G)))
    lista_graphs = L
    for g in lista_graphs:
        comp_name = NOMBRE[0]+"C"+str(comp_num)+".net"
        nx.write_pajek(G.subgraph(g), path=comp_name)
        comp_num = comp_num + 1
##
#    H = G.subgraph(G)
#    for g in nx.connected_components(G):
#      #if len(g) >= int(sys.argv[4]):
#      #if len(g) >= int(sys.argv[5]):
#      if len(g) >= int(1):      
#    H = G.subgraph(g)
#    dictEdges = {}
#    #comp_name = "Componente"+str(comp_num)
#    comp_name = NOMBRE[0]+"C"+str(comp_num)
#    OUT = open(comp_name+'.net',"w")
#    OUT.write("%s %s \n" % ("*Vertices", H.number_of_nodes()))
#    k = 1
#
#    for i in H.nodes():
#      OUT.write('%s "%s" \n' % (k,diccionarioB[i]))
#      dictEdges[i] = k
#      k = k+1
#      
#    OUT.write("%s %s \n" % ("*Edges", H.number_of_edges()))
#    for e in H.edges():
#        ed = H.get_edge_data(*e)
#        OUT.write("%s %s %s \n" % (dictEdges[e[0]],dictEdges[e[1]],ed['w']))
#        
#    pick = comp_name+'.pickle'
#    pickle.dump(H, open(pick, 'w'))
#
#    comp_num = comp_num + 1
## 
################################################################################################################ 
  
#################################### puntoNET ##################################################  
#SALIDA.write("%s %s \n" % ("*Edges", G.number_of_edges()))
#for e in G.edges():
#    ed = G.get_edge_data(*e)
#    SALIDA.write("%s %s %s \n" % (e[0],e[1],ed['w']))
    
#picklename = name[0]+'.pickle'
#pickle.dump(G, open(picklename, 'w'))
