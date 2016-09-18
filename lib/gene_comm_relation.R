##Writes tables with genes and the comm they belong
##and a single line with comm size 
##useful for Cytoscape visualization and mapping

args <- commandArgs(trailingOnly = TRUE)
comunidad = args[1] # file with genelist of community
outdir = args[2]
#comunidad<- "pruebas_enrichment_module/comms/prueba_I001/prueba_I001_C005.txt"
#outdir <-"pruebas_enrichment_module/comms/outdir/"

nombre <- strsplit(comunidad, "/")
x <- as.character(nombre[[1]])
comname <- strsplit(x[length(x)], ".txt")
filename <- paste0(comname, ".gencom")
outfile<- paste0(outdir, filename)

Com <- read.table(comunidad,stringsAsFactors = FALSE)

for(i in seq_along(Com$V1)){
  Com$V2[i] <- unlist(comname)
}

write.table(Com, 
            file = outfile, 
            row.names=FALSE, 
            col.names = FALSE, 
            quote = FALSE, 
            sep = "\t")

#######
filename2 <- paste0(comname, ".commsize")
outfile2<- paste0(outdir, filename2)
q<-paste(comname, length(Com$V1), sep = " ")
write(q, file = outfile2)