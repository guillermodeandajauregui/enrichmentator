import networkx as nx
import pandas as pd
import os
import sys
# RUN # python sif_to_net_islands.py NETWORK.sif 
########## SYSTEMS ARGUMENTS

NW = sys.argv[1]
tamano= sys.argv[2]

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
    L = sorted(list(nx.connected_components(G)), key = len, reverse=True)
    a = len(L)
    b = len(L[0])
    c = len(L[a-1])
    print("There are",a,"components!")
    print("Largest has",b,"nodes.")
    print("Smallest has",c,"nodes.")
    comp_num = 1
    if not os.path.isdir(NOMBRE[0]+"/"+"ISLANDS/"):    
        os.makedirs(NOMBRE[0]+"/"+"ISLANDS/")
    #lista_graphs =  sorted(list(nx.connected_component_subgraphs(G)))
    for g in L:
        if len(g)>=int(tamano):
            print(len(g), type(g))
            sub = G.subgraph(g)
            print(sorted(nx.nodes(sub))[1], len(sub))
            comp_name = NOMBRE[0]+"/"+"ISLANDS/"+NOMBRE[0]+"_I"+str(comp_num).zfill(3)+".net"
            nx.write_pajek(G.subgraph(g), path=comp_name, encoding = 'UTF-8')
            comp_num = comp_num + 1
