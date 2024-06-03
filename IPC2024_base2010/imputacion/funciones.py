#aca van las funciones y/o diccionarios que se utilicen

#funcion para asignar los codigos de subclase, clase, grupo y division
def pondcat(x, ponderaciones):
    grupo = ponderaciones[ponderaciones['tipo_grupo'] == x]
    newdata = grupo[['region_id', 'grupo_codigo', 'grupo_nombre', 'ponderacion_region', 'indice_anterior']]
    newdata = newdata.rename(columns={'region_id': 'region'})
    newdata['grupo_codigo'] = newdata['grupo_codigo'].astype(str)

    return newdata

#para cambiar el nombre a las decadas
decadas = {
    'Primera década':'1', 'Segunda década':'2', 'Tercera década':'3',
}

#funciones para generar los nombres de los archivos de excel con los indices y 
def excel_mesant(month):
    if month == 1:
        return 12
    elif 2 <= month <= 12:
        return month - 1

def excel_anioant(year, month):
    if year == 2024 and month == 1:
        return 2023
    else:
        return year

#para recodificar los registros con la codificacion del ipc2010
recodificacion = {
    '1111011':'011110101', 
    '1111012':'011110103', #arroz
    '1111021':'011120201', 
    '1111022':'011120202', #maiz
    '1112011':'011120102', 
    '1112021':'011120101', 
    '1112022':'011120101', 
    '1112023':'011120101', #harina
    '1112031':'011120304', #preparacion nutricional
    '1113011':'011130101', #pan frances 
    '1113012':'011130103', #pan rodajado
    '1113021':'011130102', #pan dulce corriente o de manteca
    '1113031':'011130201', #galletas
    '1113041':'011150101', 
    '1113042':'011150101',
    '1113043':'011150101', #tortillas frescas
    '1113051':'011130302', #magdalena
    '1114011':'011120301', #hojuelas de maiz
    '1114021':'011120305', 
    '1114022':'011120305', #mosh
    '1115011':'011140101', #espaguetti 
    '1115021':'011140103',
    '1115022':'011140103',
    '1115023':'011140103',
    '1115024':'011140103',
    '1115025':'011140103', #fideos 
    '1115031':'011140102', #chao mein
    '1122011':'011210101',
    '1122012':'011210102', 
    '1122013':'011210103',
    '1122014':'011210104',
    '1122015':'011210105',
    '1122016':'011210106',
    '1122017':'011210107', #carne de res
    '1122021':'011220101',
    '1122022':'011220102',
    '1122023':'011220104', #carne de cerdo
    '1122031':'011230101', #pollo fresco entero de granja 
    '1124021':'011210108', #higado de res
    '1125011':'011240101', 
    '1125012':'011240101', #salchichas
    '1125021':'011240104', #jamon de pavo
    '1125023':'011240102', #jamon de cerdo
    '1125031':'011240103', 
    '1125032':'011240103', #longaniza de cerdo
    '1125033':'011240105', 
    '1125034':'011240105', #chorizo colorados de cerdo
    '1125061':'011220103', #carne de cerdo adobada
    '1131011':'011310103',
    '1131013':'011310103', #pescado para caldo
    '1131012':'011310101', 
    '1131014':'011310102', #filete de pescado fresco
    '1133011':'011930503', 
    '1133012':'011930503', #sardinas
    '1134011':'011320101', 
    '1134012':'011320101', #camarones
    '1141012':'011410102', #leche liquida
    '1142011':'011410102', #nueva adicion
    '1142012':'011410102', #nueva adicion
    '1143011':'011410101',
    '1143012':'011410101', #leche entera en polvo
    '1143021':'011430103', #crema fresca pasteurizada
    '1145011':'011430101',
    '1145012':'011430101', #queso fresco
    '1145021':'011430104', #queso crema
    '1145041':'011430105',
    '1145042':'011430105', # queso seco
    '1146011':'011410201',
    '1146012':'011410201', #yogur preparado
    '1147012':'011410103', #leche liquida esterilizada
    '1148012':'011440101',
    '1148011':'011440101', #huevos de gallina
    '1151011':'011520101',
    '1151012':'011520101',
    '1151013':'011520101', #aceite corriente
    '1151014':'011520101', #aceite oliva
    '1153011':'011510101',
    '1153012':'011510101',
    '1161011':'011610101', #aguacate
    '1161021':'011610201', #bananos
    '1161031':'011610501', #platanos
    '1161041':'011610606', #mango
    '1161051':'011610601', #papaya
    '1161061':'011610603', #pina
    '1162011':'011610602', 
    '1162012':'011610602', #limon
    '1162021':'011610401',
    '1163011':'011610301', #manzanas
    '1165021':'011610604',
    '1165031':'011610605',
    #'':'011710601', #repollo
    "1171011":"011710601",
    "1171021":"011712001",
    "1171031":"011711701",
    "1171041":"011710701",
    "1171061":"011711801",
    "1171062":"011711901",
    "1171081":"011712002",
    "1172011":"011710301",
    "1172021":"011710401",
    "1172031":"011710101",
    "1172032":"011710102",
    "1172041":"011710201",
    "1172051":"011710501",
    "1173011":"011710901",
    "1174011":"011711301",
    "1174021":"011711401",
    "1174031":"011711101",
    "1174041":"011711001",
    "1175011":"011711201",
    "1176011":"011710801",
    "1176012":"011710801",
    "1176021":"011710802",
    "1176022":"011710802",
    "1179011":"011930501",
    "1179012":"011930501",
    "1181011":"011810101",
    "1185011":"011830101",
    "1186011":"011840101",
    "1186012":"011840102",
    "1189011":"011830102",
    "1189012":"011830104",
    "1189013":"011830104",#goma de mascar nuevo
    "1191011":"011930301",
    "1191012":"011930301",
    "1192012":"011120302",
    "1193011":"011910501",
    "1193021":"011930101",
    "1193031":"011910401",
    "1193041":"011910101",
    "1193051":"011910102",
    "1193052":"011910102",
    "1193053":"011910102",
    "1193061":"011910301",
    "1193062":"011910301",
    "1194012":"011920301",
    "1199011":"011930201",
    "1210011":"012140201",
    "1210012":"012140203",
    "1210013":"012140202",
    "1210021":"012140101",
    "1220011":"012110201",
    "1220012":"012110201",
    "1220021":"012110101",
    "1220022":"012110101",
    "1230013":"012110202",
    "1250011":"012120101",
    "1250012":"012120101",
    "1260011":"012130101",
    "1260012":"012130101",
    "1260013":"012130101",
    "1290011":"012150201",
    "1300011":"011120303",
    "2110011":"021110104",
    "2110012":"021110104",
    "2110021":"021110101", # whisky
    "2130011":"021310101",
    "2130012":"021310101",
    "2130013":"021310101",
    "2301011":"022110101",
    "3110011":"031110102",
    "3110012":"031110101",
    "3121013":"031310201",
    "3121031":"031210201",
    "3121032":"031210201",
    "3121033":"031210201",
    "3121034":"031210201",
    "3121041":"031210202",
    "3121051":"031210401",
    "3121061":"031210102",
    "3121062":"031210102",
    "3121071":"031210101",
    "3121101":"031210301",
    "3121111":"031210501",
    "3121112":"031210501",
    "3121121":"031310101",
    "3121122":"031310101",
    "3122021":"031230302",
    "3122022":"031230302",
    "3122023":"031230302",
    "3122024":"031230302",
    "3122031":"031230301",
    "3122051":"031230101",
    "3122071":"031310106",
    "3122081":"031310102",
    "3123011":"031310202",
    "3123012":"031310202",
    "3123013":"031310202",
    "3123031":"031220201",
    "3123032":"031220201",
    "3123033":"031220201",
    "3123021":"031220201", #agrege las otras blusas
    "3123022":"031220201", #agrege las otras blusas
    "3123041":"031220102",
    "3123042":"031220102",
    "3123051":"031220101",
    "3123061":"031220302",
    "3123062":"031220302", #esto es los vestidos y lo agregue recien
    "3123082":"031220103",
    "3123101":"031220202",
    "3123102":"031220301",
    "3123111":"031220401",
    "3123112":"031220401",
    "3123121":"031220402",
    "3124021":"031230401",
    "3124031":"031230201",
    "3124061":"031230501",
    "3124071":"031310107",
    "3124072":"031310107",
    "3125041":"031240101",
    "3125042":"031240101", #paquetes de mamelucos agregue
    "3126012":"031250102", 
    "3126013":"031250102", #agregue las polo de uniformes a las camisas de uniformes
    "3126014":"031250101",
    "3126015":"031250101", #agregue las faldas
    "3131011":"031310203",
    "3131012":"031310203",
    "3141011":"031410101",
    "3141012":"031410101", #agregue el lavado de ropa
    "3211011":"032110101",
    "3211012":"032110101",
    "3211021":"032110101", 
    "3211022":"032110101",#agregue los zapatos dentro de los que son mocasines
    "3212011":"032120101",
    "3212021":"032120201",
    "3212022":"032120201",
    "3212061":"032120301",
    "3212062":"032120301",
    "3213011":"032130201",
    "3213012":"032130201",
    "3213022":"032130101",
    "4111011":"041110101",
    "4111012":"041110102",
    "4111013":"041110103",
    "4311011":"042110105",
    "4311012":"042110106",
    "4311021":"042110101",
    "4311041":"042110103",
    "4311053":"042110102",
    "4321013":"042210101",
    "4411011":"043110103",
    "4412011":"043110102",
    "4420011":"043210101",
    "4420012":"043210101",
    "4510011":"044110101",
    "4510012":"044110102",
    "4522011":"044210101",
    "4522012":"044210101", # agregue el gas de mas de 25lb
    "4541011":"044310101",
    "4542011":"044310201",
    "5111011":"051110501",
    "5111012":"051110501",
    "5111013":"051110501",
    "5111021":"051110301",
    "5111022":"051110301", # agrege las mesas de comedor a los comedores
    "5111031":"051110401",
    "5111032":"051110401", # agregue lso gabinetes
    "5111041":"051110601",
    "5111042":"051110601", # agregue los otros gabinetes
    "5111043":"051110101",
    "5211011":"052110501",
    "5212011":"052110301",
    "5212012":"052110302",
    "5212013":"052110101",
    "5212014":"052110201",
    "5213011":"052110401",
    "5213012":"052110401", # agregue lo del plastico para mesa y manteles
    "5311011":"052210201",
    "5311021":"052210101",
    "5311022":"052210101",
    "5311031":"052310101",
    "5312011":"052210301",
    "5312012":"052210301",
    "5321011":"052310201",
    "5321012":"052310201",
    "5329011":"052310301",
    "5401011":"053110101",
    "5401012":"053110101",
    "5401013":"053110101",
    "5401014":"053110301",
    "5403041":"053110301",
    "5403042":"053110301", # agregue los vasos de melamina 
    "5403011":"053110201",
    "5403012":"053110202",
    "5403013":"053110202",
    "5403021":"053110402",
    "5403022":"053110402",
    "5403031":"053110401",
    "5510011":"054110101",
    "5521011":"054120201",
    "5522011":"042110301",
    "5522012":"042110301",
    "5611011":"055110201",
    "5611012":"055110201",
    "5611013":"055110201",
    "5611014":"055110201", #agregue el detergente liquido al de polvo
    "5611021":"055110202",
    "5611022":"055110202",
    "5611031":"055120102",
    "5611032":"055120102",
    "5611033":"055120102",
    "5611041":"055120101",
    "5611042":"055120101",
    "5611043":"055120101",
    "5611051":"055110301",
    "5611052":"055110301",
    "5611061":"055110203",
    "5611062":"055110203",
    "5611063":"055110203",
    "5611071":"055120103",
    "5619011":"055110101",
    "5619012":"055110101",
    "5619031":"055120301",
    "5619032":"055120301", # puse los mayordomos en las servilletas de papel
    "5619051":"055120402",
    "5619052":"055120402",
    "5619061":"055120401",
    "5619071":"055120201",
    "5619072":"055120201",
    "5621011":"055210101",
    "5621012":"055210201",
    "6111011":"061110501",
    "6111012":"061110501",
    "6111021":"061110501",
    "6111022":"061110501",
    "6111031":"061110501",
    "6111041":"061110901",
    "6111051":"061110901",
    "6111052":"061110901",
    "6111061":"061110601",
    "6111062":"061110601",
    "6111071":"061110601",
    "6111081":"061110601",
    "6111082":"061110601",
    "6111091":"061110601",
    "6111101":"061110101",
    "6111102":"061110101",
    "6111121":"061210101",
    "6111122":"061210101",
    "6111131":"061110801",
    "6111132":"061110801",
    "6111141":"061111001",
    "6111142":"061111001",
    "6111143":"061111001",
    "6111144":"061111001",
    "6111171":"061110201",
    "6111172":"061110201",
    "6111173":"061110201",
    "6111181":"061110401",
    "6111182":"061110401",
    "6111183":"061110401",
    "6111191":"061110401",
    "6111192":"061110401",
    "6111201":"061110401",
    "6111202":"061110401",
    "6111241":"061210201",
    "6111242":"061210201",
    "6111243":"061210201",
    "6111251":"061110301",
    "6112011":"061111002",
    "6112012":"061111002",
    "6112013":"061111002",
    "6131012":"061310101",
    "6219011":"062110201",
    "6219021":"062110102",
    "6219022":"062110102",
    "6219031":"062110103",
    "6219041":"062110103",
    "6219051":"062110103",
    "6219061":"062110103",
    "6219071":"062110103",
    "6219081":"062110103",
    "6219091":"062110101",
    "6229011":"062210101", # agregue la extraccion en las consultas con odontologos
    "6221011":"062210102",
    "6229021":"062210201",
    "6229031":"062210202",
    "6229032":"062210202", # agregue a ortodoncia el control de brackets
    "6229041":"062210202", # agregue la endodoncia
    "6229051":"062210202", # agregue los implantes dentales
    "6310041":"063110101",
    "6310011":"063110101",
    "6310021":"063110101", # agregue los partos a la intervencion quirurgica con encamamiento
    "6310031":"63110201", #agregue la hosp sin cirugia a los gastos de alojamiento, comida y bebida en hospital
    "6411011":"062310201",
    "6411021":"062310201",
    "6411022":"062310201",
    "6412011":"062310101",
    "6412012":"062310101",
    "6412021":"062310102",
    "6412031":"062310104",
    "6412041":"062310103",
    "6412042":"062310103",
    "6412051":"062310103",
    "7111011":"071110101",
    "7111012":"071110101",
    "7111013":"071110101",
    "7111014":"071110101",
    "7111015":"071110101",
    "7111021":"071110102",
    "7111022":"071110102",
    "7111023":"071110102",
    "7111024":"071110102",
    "7111025":"071110102",
    "7111031":"071110103",
    "7111032":"071110103",
    "7111033":"071110103",
    "7111034":"071110103",
    "7120011":"071210101",
    "7120012":"071210101",
    "7120013":"071210101",
    "7120014":"071210101",
    "7120015":"071210101",
    "7120016":"071210101",
    "7130011":"071310101",
    "7130012":"071310101",
    "7211011":"072110201",
    "7211012":"072110201",
    "7211013":"072110201",
    "7211014":"072110201",
    "7211015":"072110201",
    "7212011":"072110301",
    "7212012":"072110301",
    "7212021":"072110101",
    "7212022":"072110101",
    "7212023":"072110101",
    "7212031":"072110101",
    "7212032":"072110101", # agregue 
    "7221011":"072210301",
    "7222011":"072210201",
    "7222012":"072210101",
    "7224011":"072110302",
    "7224012":"072110302",
    "7224013":"072110302",
    "7224021":"072110302", #agregue el liquido de frenos a los lubricantes
    "7231031":"072310101", 
    "7231032":"072310101", #servicio de tune up
    "7231011":"072310301",
    "7231012":"072310301",
    "7231021":"072420101",
    "7231022":"072420101",
    "7231023":"072420101",
    "7231041":"072310201",
    "7231042":"072310201",
    "7231051":"072310201",
    "7231052":"072310201",
    "7231053":"072310201",
    "7231054":"072310201",
    "7231061":"072310201",#agregados
    "7241011":"072410101",
    "7241012":"072410101",
    "7241013":"072410101",
    "7241014":"072410101",
    "7241021":"072410102",
    "7241022":"072410102",
    "7243011":"072420201",
    "7243021":"072420201",
    "7243022":"072420201", #agregue la renovacion de licencias
    "7321011":"073110301",
    "7321012":"073110301",
    "7321013":"073110301",
    "7321031":"073110301", #agregue el taxi compartido al transporte urbano
    "7321021":"073110401",
    "7321022":"073110401",
    "7321023":"073110401",
    "7321024":"073110401",
    "7322011":"073110101",
    "7322012":"073110101", #agregue los taxis por aplicacion
    "7323011":"073110201",
    "7329012":"073110102",
    "7332011":"073210101",
    "7332012":"073210101",
    "7332013":"073210101",
    "7412011":"081110103",
    "7412012":"081110103", # puse envios de paquetes en encomiendas o paquetes postales
    "8120011":"082110101",
    "8120012":"082110101",
    "8120013":"082110101",
    "8120014":"082110101",
    "8120015":"082110101",
    "8120016":"082110101",
    "8120017":"082110101",
    "8131011":"091310102",
    "8131012":"091310101",
    "8131013":"091310101",
    "8132012":"091310201",
    "8132013":"091310201",
    "8140011":"091110101",
    "8140012":"091110101",
    "8140013":"091110101",
    "8140021":"091110102",
    "8140022":"091110102",
    "8140023":"091110102",
    "8310011":"083110401",
    "8310012":"083110401",
    "8320011":"083110302",
    "8320021":"083110302",
    "8320022":"083110302",
    "8320023":"083110302", #agregeue los planes celulares a telefono celular con linea
    "8330011":"083110101",
    "8340011":"083110201",
    "8340012":"083110202",
    "8340013":"083110202",
    "8340014":"083110202",# agregue los paquetes de telefonia cable, etc
    "9211011":"092110401",
    "9211012":"092110401",
    "9212011":"092110301",
    "9212012":"092110301", # agregue los peluches a los muñecos
    "9212021":"092110101",
    "9212022":"092110101",
    "9221012":"092210101",
    "9312012":"092310101",
    "9312011":"092310101", #agregue las rosas simples a arreglo de flores
    "9321021":"092410101",
    "9321022":"092410101",
    "9321023":"092410101",
    "9321024":"092410101",
    "9321025":"092410101",
    "9450011":"092510101",
    "9450012":"092510101",
    "9450013":"092510101",
    "9462011":"093120101",
    "9462012":"093120101",
    "9462022":"093120201",
    "9610011":"093210101",
    "9610012":"093210101",
    "9610013":"093210101",
    "9711011":"094110103",
    "9711012":"094110101",
    "9719011":"094210201",
    "9719021":"094110105",
    "9719021":"094110105", #agregue los diccionarios en las enciclpedias
    "9721012":"094210101",
    "9721011":"094210101",
    "9740021":"094310102",
    "9740022":"094310101",
    "9740041":"094310104",
    "9740064":"094310201",
    "9740065":"094310201",
    "9740066":"094310201",
    "9740067":"094310201",
    "9740071":"094310103",
    "9740072":"094310103",
    "9740081":"094310202",
    "9740082":"094310202",
    "9740083":"094310203",
    "9800011":"095110201",
    "9800012":"095110201",
    "9800013":"095110201",
    "9800014":"095110201",
    "10101011":"101110102",
    "10101012":"101110102",
    "10101013":"101110101",
    "10102011":"101110202",
    "10102012":"101110202",
    "10102013":"101110201",
    "10200011":"102110102",
    "10200012":"102110102",
    "10200021":"102110102", # inclui la inscripcion diversificado y la por cooperativa en la secundaria
    "10200013":"102110101",
    "10200022":"102110101", # inclui la cuoa mensual diversificado en la secundaria
    "10200014":"102110103",
    "10200023":"102110103",
    "10400011":"103110201",
    "10400012":"103110201",
    "10400013":"103110201",
    "10400014":"103110201",
    "10400015":"103110201",
    "10400016":"103110202",
    "10400017":"103110202",
    "10400018":"103110202",
    "10400019":"103110202",
    "104000110":"103110202",
    "10509011":"104110103",
    "10509021":"104110101",
    "10509022":"104110101",
    "10509031":"104110102",
    "10509032":"104110102",
    "11111011":"111110101", #desayunos
    "11111012":"111110101", #desayunos
    "11111021":"111110101", #desayunos
    "11111031":"111110101", #desayunos
    "11111013":"111110301", #cena
    "11111022":"111110301", #cena
    "11111051":"111110201", #almuerzos
    "11111052":"111110201",
    "11111053":"111110201",
    "11111054":"111110201",
    "11111061":"111110201",
    "11111062":"111110201",
    "11111063":"111110201",
    "11111064":"111110201",
    "11111065":"111110201",
    "11111066":"111110201",
    "11111071":"111110201",
    "11111072":"111110201",
    "11111073":"111110201",
    "11111081":"111110201", #almuerzos
    "11112021":"111120203", #puse el combo de comida rapida familiar de pollo como menu campero
    "11112012":"111120202",
    "11112032":"111110303",
    "11112041":"111120102",
    "11112055":"111110305",
    "11112061":"111110304",
    "11112063":"111110306",
    "11112065":"111110302",
    "11112082":"111120101",
    "11112083":"111120201",
    "11201011":"112110201", #hotel o pension sin comida
    "11201012":"112110201",
    "11201013":"112110201", #hotel o pension sin comida
    "12110011":"123110104",
    "12120011":"123110102",
    "12141011":"123110101",
    "12210011":"124110101",
    "13120011":"121210301",
    "13120012":"121210301",
    "13120021":"121220201",
    "13120022":"121220201",
    "13120031":"121220301",
    "13120032":"121220301",
    "13120041":"121220101",
    "13120042":"121220101",
    "13120043":"121220101",
    "13120051":"121220601",
    "13120053":"121220601",
    "13120052":"121220602",
    "13120061":"121220501",
    "13120062":"121220501",
    "13120071":"121220401",
    "13120072":"121220401",
    "13120073":"121220401",
    "13120101":"121230401", 
    "13120102":"121230401",#cream para manos y cuerpo
    "13120103":"121230601",
    "13120111":"121230501",
    "13120112":"121230501",
    "13120113":"121230501",
    "13120125":"121230201", #esto lo puse dentro del maquillaje
    "13120126":"121230201", #esto lo puse dentro del maquillaje
    "13120121":"121230103",
    "13120122":"121230103",
    "13120123":"121230102",
    "13120124":"121230104",
    "13131011":"121110101",
    "13131012":"121110101",
    "13131021":"121110201",
    "13131022":"121110201",
    "13131031":"121110202",
    "13131032":"121110202",
    "13131033":"121110202",
    "13131034":"121110202",
    "13131035":"121110202",
    "13132011":"121110203",
    "13131041":"121110203",
    "13131042":"121110203",
    "13211011":"122110101",
    "13211012":"122110101",
    "13211013":"122110101",
    "13211041":"122110201",
    "13211042":"122110201",
    "13909011":"125110301",
    "13909021":"125110401",
    "13909022":"125110401",
    "13909041":"125110101",
    "13909042":"125110101",
    "13909043":"125110101",
    "13909044":"125110101",
    "13909051":"093110201",
    "13909052":"093110201",
    "13909053":"093110201",
    "13909054":"093110201",
    "1199031":"111120301", #coloque las frituras de maiz en los tortrix
    "11112072":"011130303", #coloque las porciones de pastel frio de fresas en los pasteles frios
    "1230012":"012110202", #coloque el te de frutas en los te de caja
    '1122032':'011230101', #**agregue el pollo amarillo al pollo fresco entero de granja
    #'1122032':'011230102', #**coloque el pollo amarillo en las pechugas de pollo
    '1113054':'011130102', #coloque los cubiletes, etc en el pan dulce corriente o de manteca
    '1113022':'011130102', #intento de colocar el pan especial en el pan dulce
    '1113032':'011130201', #coloque las galletas saladas en las galletas
    #'1114013':'011120301', #**coloque el cereal de arroz inflado en las hojuelas de maiz
    #'1114014':'011120301', #**coloque el cereal aritos en las hojuelas de maiz
    '1114012':'011120301', #coloque las hojuelas de maiz azucaradas en las hojuelas de maiz
    "1290012":"012150201", #coloqe las bebidas energizantes en las rehidratantes
    "1181012":"011810101", #coloque azucar morena en la azucar blanca
    "6131011":"061310101", #coloque los lentes de lectura en los lentes correctores
    "4321021":"125110501", #cuota de vigilancia residencial
    '11430103':'011430103', #para arreglar una cosa de la crema que sale raro en la base de datos
    "3213031":"032130101", #agregueu los tennis para niños en zapatos amarrados para niño
    "8392021":"083110201", #television por cable
    "9719022":"094110105", #agregue los diccionarios bilingues en las enciclpedias
    "11620101":"011620101", #agregue las frutas en conserva, tienen el codigo de la base anterior
    "11112073":"011130303", #agregue las porciones de pastel de chocolate frio en los pasteles frios
}