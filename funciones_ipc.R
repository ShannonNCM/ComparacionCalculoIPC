#Script con las funciones utilizadas para los calculos del ipc

#funcion para asignar los codigos de subclase, clase, grupo y division
cod_grupos <- function(x){
  data.frame(x %>% 
              mutate(cod_subclase = substr(cod_prod, 1, nchar(cod_prod) - 2), .before = cod_prod) %>% 
              mutate(cod_clase = substr(cod_prod, 1, nchar(cod_prod) - 3), .before = cod_subclase) %>%
              mutate(cod_grupo = substr(cod_prod, 1, nchar(cod_prod) - 4), .before = cod_clase) %>%
              mutate(cod_div = substr(cod_prod, 1, nchar(cod_prod) - 5), .before = cod_grupo))
}


#Funcion para obtener las ponderaciones de las distitas categorias
pondcat <- function(x){
  ponderaciones %>% 
    filter(tipo_grupo == x) %>% 
    select(region_id, grupo_codigo, grupo_nombre, ponderacion_region, indice_anterior) %>% 
    rename(region = region_id) %>% 
    mutate(grupo_codigo = as.character(grupo_codigo))
} 

#funcion para calcular la variacion del precio de un producto
variacion <- function(x){
  data.frame(x %>% 
              mutate(var_prod = (precio_actual/cantidad_actual)*(cantidad_anterior/precio_anterior)))
}
