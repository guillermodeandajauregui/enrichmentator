idxmatrix <- function(x, i1,i2) {
  return(x[i1,i2])
}

lookupidxmatrix <- function(lookup, x) {
  return(idxmatrix(x, lookup[1], lookup[2]))
}


sif_nxm <- function(x) {
  sif <- expand.grid(rownames(x), colnames(x))
  weight <- apply(sif, 1, lookupidxmatrix, x)
  sif2 <- data.frame(sif, weight)
  return(sif2)
  
}