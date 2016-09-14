#!/bin/bash
##enrichmentator pipeline

##variables 

sif=$1 #sif file to be used. Of the shape gene interaction gene, tab or space separated. 
tamano=$2 #size of islands to be considered for the analysis. 

basename=$(echo $sif | cut -d "." -f1) #ideally, the basename of the sif file reflects the phenotype
					#ie, "luminal", "cancer", etc. 
echo $basename

#make output folders

mkdir -p $basename/ISLANDS #where ISLAND files will be kept. 
mkdir -p $basename/MAPS    #where MAP files will be kept
mkdir -p $basename/COMMUNITIES #where COMMUNITIES will be kept.
mkdir -p $basename/ENRICHMENT #where ENRICHMENT data will be kept. 

##take SIF, output ISLANDS
	#$sif is a sif file 
	#tamano is the min. size of island. 
python lib/sif_to_net_islands.py $sif $tamano
	#OUTPUT: .net files, Pajek-like, as formatted by NetworkX. 
		#NX outputs these files with nodes without quotes around them, and "0.0 0.0 ellipse" trailing.
		#InfoMAP doesn't read them like we want them.

##massage last output to a format edible for infoMAP

cd $basename/ISLANDS
#ls
sh ../../lib/sed_pajek.sh #puts quotations around gene names, and removes 0.0 0.0 ellipse from each node.
			  #VERY AD HOC FOR OUR PIPELINE; 

###Community detection phase

###Run infomap on ISLANDS IN sif[0]/ISLANDS
cd ../../
for net in $(ls $basename/ISLANDS/*.net); do
	#echo $net
	./lib/infomap/Infomap $net $basename/MAPS --map --silent
done

### Enrichment phase

#process infomap outputs to individual listfiles
for map in $(ls $basename/MAPS/*.map)
  do
#	   echo $map #ej: prueba/MAPS/prueba_I001.map
       mappathbase=$(echo $map | cut -d "." -f1 ) #ej: prueba/MAPS/prueba_I001
       mapbase2=$(echo $mappathbase | cut -d "/" -f3) #ej: prueba_I001
       mapfile=$(echo $map | cut -d "/" -f3) #ej: prueba_I001.map
#	echo $mappathbase
       mkdir -p $basename/COMMUNITIES/$mapbase2 #mapbase2 is ISLAND name (ej pheno_I001)
       dr=$basename/COMMUNITIES/$mapbase2 # ej: prueba/COMMUNITIES/prueba_I001
	ENRICHMENT_out=$basename/ENRICHMENT/$mapbase2
##usage Analisis_Infomap3.py map_file outdir prefix(island name)
       python lib/Analisis_Infomap3.py $map $dr/ $mapbase2
	#Outputs: genelist files for each community, of the form pheno_I001_C001.txt
	#AND: "InfoMAP_TRANSP.csv", 
		#textfile with genes in communities in each row, separated by tabs. 
		#Each row a comm. 

#run the enrichment algorithms
##testing
      for comm in $(ls $dr/*.txt) 
      do
	  echo $comm
	  echo $mapbase2
	  echo $dr
	  echo $ENRICHMENT_out
	  Rscript lib/Enrichmentator.R  $comm $mapbase2 $ENRICHMENT_out
      done       
done
