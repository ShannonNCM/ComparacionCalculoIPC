#Script con las funciones utilizadas para los calculos del ipc



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
ipc <- function(x,y){
  data.frame(x %>% 
               filter(region !=0) %>% 
               left_join(y, by = "region") %>% 
               group_by(region, grupo_codigo, grupo_nombre) %>% 
               summarize(sum1 = sum(ponderacion_region*participacion), 
                         sum2 = sum(ponderacion_region*participacion*indice_grupo)) %>% 
               mutate(ind = sum2/sum1))
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


