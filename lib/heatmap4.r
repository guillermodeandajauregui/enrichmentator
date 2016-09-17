# Primero hay que cargar los archivos csv a una tabla de R con su encabezado y todo

#args <- commandArgs(trailingOnly = TRUE);
#args<-"pruebas_enrichment_module/intento/gansoz_GOMF.csv"
#args<-"pruebas_enrichment_module/intento/emptyframe.csv"
args<- "pruebas_enrichment_module/prueba_I001/triphop_GOBP.csv"
DATA = args[1];

# X=read.table("Archivo.csv", header=TRUE, sep =",")
X=read.table(DATA, header=TRUE, sep ="\t", row.names = 1);
Y = as.matrix(X)
Z = -log10(Y) #mo color, mo statistical significance

if(ncol(Z)==1){
  Z = cbind(Z,Z)
  colnames(Z)[2] <- paste("FakeColforceheatmap")
  #return(Z)
}

library(gplots);

# color palette
x = strsplit(DATA, "_")
y <- as.character(x[[1]])
z = strsplit(y[length(y)], ".csv")


if (z[1] == 'GOCC') {
  my_palette <- colorRampPalette(c("white", "violet", "darkviolet", "midnightblue"))(n = 1000);
} else if (z[1] == 'GOBP') {
  my_palette <- colorRampPalette(c("white", "greenyellow", "limegreen", "darkgreen"))(n = 1000);
} else if (z[1] == 'GOMF') {
  my_palette <- colorRampPalette(c("white", "lightsalmon", "orangered", "darkred"))(n = 1000); 
} else if (z[1] == 'KEGG') {
  my_palette <- colorRampPalette(c("white", "lightskyblue", "steelblue", "darkblue"))(n = 1000);
} else {
  my_palette <- colorRampPalette(c("white", "lightcoral", "firebrick", "red"))(n = 1000);
}

# El heatmap se hace con el código siguiente:

# heatmap.2(Z, trace="none", col=my_palette, scale="row", labCol=colnames(Z), labRow=RN)

# Si lo quieren guardar en PDF entonces antes de la instrucción anterior "abren la imagen" con PDF("imagen.pdf") y la cierran con dev.off() de manera que el código queda:

# pdf("heatmap1.pdf")
s = strsplit(DATA,".csv");
out = paste(s,".pdf",sep="");
pdf(out, paper="USr");


# heatmap.2(Z, trace="none", col=my_palette, scale="row", labCol=colnames(Z), labRow=RN);
heatmap.2(Z, 
          trace="none", 
          col=my_palette, 
          labRow=rownames(Z), 
          labCol=colnames(Z), 
          margins = c(5, 11.5), 
          cexCol = 0.4, 
          cexRow = 0.3);

dev.off();

