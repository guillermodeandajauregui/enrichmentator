
source("lib/Enrichment.R")
#source("lib/matriz_nombres_genes.csv")

args <- commandArgs(trailingOnly = TRUE)
comunidad = args[1]

Com <- read.table(comunidad,stringsAsFactors = FALSE)
Com <- Com$V1

nombre <- strsplit(comunidad, "/")
x <- as.character(nombre[[1]])
y <- strsplit(x[2], ".txt")
#name <- paste(y, ".csv", sep="")
name <- paste0(y, ".csv")

#path <- x[1]
path <- paste0(x[1], "/")


#print(file)
enrichmentator(Com,name,path)
#enrichmentator(Com,file)
