#!/bin/bash
##enrichmentator pipeline

##variables 

sif=$1 
basename=$(echo $sif | cut -d "." -f1)
echo $basename

#make output folders

mkdir -p $basename/ISLANDS
mkdir -p $basename/MAPS

##take SIF, output ISLANDS

python lib/sif_to_net_islands.py $sif

##massage last output to format edible for infoMAP

cd $basename/ISLANDS
#ls
sh ../../lib/sed_pajek.sh 

###Run infomap on ISLANDS IN sif[0]/ISLANDS
cd ../../
for net in $(ls $basename/ISLANDS/*.net); do
	#echo $net
	./lib/infomap/Infomap $net $basename/MAPS --map --silent
done


#for i in .net 
#	Infomap
