source("lib/sif_from_matrix.R")
args <- commandArgs(trailingOnly = TRUE);
DATA = args[1];
# X=read.table("Archivo.csv", header=TRUE, sep =",")
X=read.table(DATA, header=TRUE, sep ="\t", row.names = 1);
Y = as.matrix(X)

Z = sif_nxm(Y)
s = strsplit(DATA,".csv");
out = paste(s,".procmap",sep="")

write.table(Z, file= out, sep = "\t", quote = FALSE, row.names = FALSE)



