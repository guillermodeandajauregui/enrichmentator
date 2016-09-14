#!/bin/bash
##enrichmentator pipeline

##variables 

sif=$1 
basename=$(echo $sif | cut -d "." -f1)
echo $basename

#make output folders

mkdir -p $basename/ISLANDS
mkdir -p $basename/MAPS
mkdir -p $basename/COMMUNITIES

##take SIF, output ISLANDS

python lib/sif_to_net_islands.py $sif

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
####probar analisis infoMAP
for map in $(ls $basename/MAPS/*.map)
  do
	   echo $map
       mappathbase=$(echo $map | cut -d "." -f1 )
       mapbase2=$(echo $mappathbase | cut -d "/" -f3) 
       mapfile=$(echo $map | cut -d "/" -f3)
       #echo $mappathbase
       #echo $mapbase2
       #echo $mapfile
       mkdir -p $basename/COMMUNITIES/$mapbase2
       dr=$basename/COMMUNITIES/$mapbase2
       #cp $map $dir
       python Analisis_Infomap2.py $map $dr/
done
