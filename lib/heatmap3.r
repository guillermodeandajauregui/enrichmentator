# Primero hay que cargar los archivos csv a una tabla de R con su encabezado y todo

args <- commandArgs(trailingOnly = TRUE);

DATA = args[1];

# X=read.table("Archivo.csv", header=TRUE, sep =",")
X=read.table(DATA, header=TRUE, sep ="\t");

# Luego hay que definir la columna de nombres 
#(columna 1 de su csv cargado en el objeto X) 
#en un objeto que llamaré RN (de row names)

RN=X[,1];
END = length(X[0,]) - 2;

# Los datos numéricos de su matríz están en las columnas 2 a la 31, 
#carguenlos en un objeto Y

# Y = X[,2:31]
Y=X[,2:END];

Y = as.matrix(Y);

# Pero en su excel pusieron p-values y nosotros queremos que a 
#mayor significancia más intensidad de color, 
#eso se logra con el -log10(p-value)

Z=-log10(Y);

# Para hacer el heatmap deberán tener cargada la libraría (gplots) en [R]

library(gplots);

# Es buena idea definir una paleta de colores, n es el número de intervalos de color


x = strsplit(DATA, "_")
y <- as.character(x[[1]])
z = strsplit(y[length(y)], ".csv")


if (z[1] == 'CC') {
  my_palette <- colorRampPalette(c("white", "violet", "darkviolet", "midnightblue"))(n = 1000);
} else if (z[1] == 'BP') {
  my_palette <- colorRampPalette(c("white", "greenyellow", "limegreen", "darkgreen"))(n = 1000);
} else if (z[1] == 'MF') {
  my_palette <- colorRampPalette(c("white", "lightsalmon", "orangered", "darkred"))(n = 1000); 
} else if (z[1] == 'kegg') {
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
heatmap.2(Z, trace="none", col=my_palette, labRow=RN, labCol=colnames(Z), margins = c(5, 11.5), cexCol = 0.6, cexRow = 0.3);

dev.off();

