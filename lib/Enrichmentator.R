
source("lib/Enrichment.R")
#source("lib/matriz_nombres_genes.csv")

args <- commandArgs(trailingOnly = TRUE)
comunidad = args[1] # file with genelist of community

Com <- read.table(comunidad,stringsAsFactors = FALSE) #read community
Com <- Com$V1 #community as chr vector, each element a gene  

name <- args[2]
nombre <- strsplit(comunidad, "/")
x <- as.character(nombre[[1]])
y <- strsplit(x[length(x)], ".txt")
#name <- paste(y, ".csv", sep="")
name <- paste0(y, ".csv") # prueba_I001_C001.csv

#path <- x[1]
#path <- paste0(x[1], "/")
path <- args[3]

#print(file)
enrichmentator(Com,name,path)
#enrichmentator(Com,file)
