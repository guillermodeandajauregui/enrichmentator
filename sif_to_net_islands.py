import networkx as nx
import pandas as pd
import os
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
    L = sorted(nx.connected_components(G), key = len, reverse=True)
    a = len(L)
    b = len(L[0])
    c = len(L[a-1])
    print("Se tienen",a,"componentes!")
    print("El mayor es de",b,"nodos.")
    print("El menor es de",c,"nodos.")
    #tamano = int(raw_input("Ingresa el tamaño minimo de los componentes a considerar  "))
    comp_num = 1
    if not os.path.isdir(NOMBRE[0]+"/"+"ISLANDS/"):    
        os.makedirs(NOMBRE[0]+"/"+"ISLANDS/")
    #lista_graphs =  sorted(list(nx.connected_component_subgraphs(G)))
    for g in L:
        comp_name = NOMBRE[0]+"/"+"ISLANDS/"+NOMBRE[0]+"_I"+str(comp_num).zfill(2)+".net"
        nx.write_pajek(G.subgraph(g), path=comp_name)
        comp_num = comp_num + 1
