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
  ponderacionesmesant %>% 
    filter(tipo_grupo == x) %>% 
    select(region_id, grupo_codigo, grupo_nombre, ponderacion_region, indice_grupo) %>% 
    rename(region = region_id) %>% 
    mutate(grupo_codigo = as.character(grupo_codigo))
} 

#funcion para calcular la variacion del precio de un producto
variacion <- function(x){
  data.frame(x %>% 
              mutate(var_prod = (precio_actual/cantidad_actual)*(cantidad_anterior/precio_anterior)))
}




#funcion para calcular el ipc en las categorias superiores por region
#x es la columna del dataframe que tiene el codigo del grupo para el que se va a calcular el ipc
ipc <- function(x, y){
  data.frame(x %>% 
               #select(region, y, grupo_nombre, ponderacion_region, ind_prod) %>% 
               rename(grupo_codigo = y) %>% 
               group_by(region, grupo_codigo) %>% 
               summarize(sum1 = sum(ind_prod*ponderacion_region),
                         sum2 = sum(ponderacion_region)) %>% 
               mutate(ind = sum1/sum2))
}





#funcion para calcular el ipc en las categorias superiores a nivel nacional
ipc_nac <- function(x,y){
  data.frame(x %>% 
               filter(region != 0) %>% 
               left_join(y, by ="region") %>%
               group_by(grupo_codigo, grupo_nombre) %>% 
               summarize(sum1 = sum(ponderacion_region*participacion), 
                         sum2 = sum(ponderacion_region*participacion*indice_grupo)) %>% 
               mutate(ind = sum2/sum1))
}





#funcion para calcular el ipc general


