#!/bin/bash
##enrichmentator pipeline

##variables 

sif=$1 
tamano=$2
basename=$(echo $sif | cut -d "." -f1)
echo $basename

#make output folders

mkdir -p $basename/ISLANDS
mkdir -p $basename/MAPS
mkdir -p $basename/COMMUNITIES

##take SIF, output ISLANDS

python lib/sif_to_net_islands.py $sif $tamano

##massage last output to format edible for infoMAP

cd $basename/ISLANDS
#ls
sh ../../lib/sed_pajek.sh 

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
	   echo $map
       mappathbase=$(echo $map | cut -d "." -f1 )
       mapbase2=$(echo $mappathbase | cut -d "/" -f3) 
       mapfile=$(echo $map | cut -d "/" -f3)
       mkdir -p $basename/COMMUNITIES/$mapbase2 #mapbase2 is ISLAND name (ej pheno_I001)
       dr=$basename/COMMUNITIES/$mapbase2
       python lib/Analisis_Infomap3.py $map $dr/ $mapbase2
#run the enrichment algorithms
##testing
      for j in $(ls $dr/*.txt) 
      do
	  echo $j
	  Rscript lib/Enrichmentator.R  $j
      done       
done
