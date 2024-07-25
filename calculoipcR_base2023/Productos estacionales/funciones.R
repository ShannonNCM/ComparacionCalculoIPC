# En este script se encuentran las funciones utilizadas para realizar el calculo 
# de los factores estacionales

## Funcion que calcula los promedios moviles

prom_movil <- function(x, k){
  n <- length(x) #se determina el tamaño de la columna del dataframe a usar
  resultado <- rep(NA, n)
  for (i in seq_along(x)) {
    if (i == 1) {
      resultado[i] <- mean(x[i:(i + 1)])
    } else if (i == n) {
      resultado[i] <- mean(x[(i - 1):i])
    } else {
      resultado[i] <- mean(x[(i - (k-1)/2):(i + (k-1)/2)])
    }
  }
  return(resultado)
}


## Funcion que calcula el factor estacional
factor_est <- function(x, y){
  x %>% 
    filter(Descripción == y) %>% 
    select(Año, Mes, Descripción, Rep.) %>% 
    mutate(prom_mov = prom_movil(Rep.,3)) %>% #calcula el promedio movil
    mutate(aggeom = Rep./prom_mov) %>%
    group_by(Mes) %>% 
    summarize(factest = geometric.mean(aggeom, na.rm = TRUE)) %>% 
    mutate(producto = y)
}



#factor_est <- function(df, producto){
#  df %>% 
#    filter(Descripción == producto) %>% 
#    select(Año, Mes, Descripción, Rep.) %>% 
#    mutate(prom_mov = prom_movil(Rep.,3)) %>% #calcula el promedio movil
#    mutate(aggeom = Rep./prom_mov) %>%
#    group_by(Mes) %>% 
#    summarize(geom_mean = geometric.mean(aggeom, na.rm = TRUE)) %>% 
#    mutate(Prod = producto)
#}
