#!/bin/bash
##enrichmentator pipeline

##variables 

sif=$1 
basename=$(echo $sif | cut -d "." -f1)
echo $basename

##take SIF, output ISLANDS

python lib/sif_to_net_islands.py sif

##massage last output to format edible for infoMAP

cd $basename/ISLANDS
#ls
lib/sed_pajek.sh 

###Run infomap on ISLANDS IN sif[0]/ISLANDS
#for i in .net 
#	Infomap
