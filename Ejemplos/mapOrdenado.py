import config as cf
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt


# Creacion
mapa = om.newMap(omaptype='RBT')
mapa = om.newMap(omaptype='BST')

om.put(mapa, "k1", 1)               #mapa ={"k1": 1}
om.put(mapa, "k2", 2)               #mapa ={"k1": 1, "k2": 2}
om.put(mapa, "k3", 3)               #mapa ={"k1": 1, "k2": 2, "k3": 3}

val = me.getValue(om.get(mapa, "k1"))   # => 1
val = om.get(mapa, "k1")["value"]       # => 2

om.remove(mapa, "k1")               #mapa ={"k2": 2, "k3": 3}

om.size(mapa)                       # => 2
om.isEmpty(mapa)                    # => False

om.contains(mapa, "k2")             # => True

#Imprimir las llaves y valores en orden
for k in lt.iterator(om.keySet(mapa)):
  print("llave:" + k + ", valor: " + str(om.get(mapa, k)["value"]))
  
#Imprimir los valores
for v in lt.iterator(om.valueSet(mapa)):
  print(v)

#----------------------
# operaciones ordenadas
#----------------------
mapa = om.newMap(omaptype='RBT')
om.put(mapa, "k1", 1)              
om.put(mapa, "k2", 2)              
om.put(mapa, "k3", 3) 
om.put(mapa, "k6", 6) 
#mapa ={"k1": 1, "k2": 2, "k3": 3, , "k6": 3}

om.minKey(mapa)           # => k1
om.maxKey(mapa)           # => k6

om.floor(mapa, "k3")   # => k3
om.floor(mapa, "k4")   # => k3

om.ceiling(mapa, "k4")   # => k6
om.ceiling(mapa, "k6")   # => k6

om.rank(mapa, "k1")      # => 0
om.rank(mapa, "k2")      # => 1
om.rank(mapa, "k3")      # => 2
om.rank(mapa, "k4")      # => 3

om.select(mapa, 0)      # => k1
om.select(mapa, 1)      # => k2
om.select(mapa, 2)      # => k3
om.select(mapa, 3)      # => k6

# Llaves en un rango inclusivo
for k in lt.iterator(om.keys(mapa, "k1", "k4")):
  print(k)  #k1, k2, k3

#----------------------
# Creacion más complicada
#----------------------

# def compareKeys(k1, entry):
#     k2 = me.getKey(entry)
#     if (k1 == k2):
#         return 0
#     elif (k1 > k2):
#         return 1
#     else:
#         return -1

# mapa = mp.newMap(
#   numelements=5,                #Numero de elementos que se planean guardar, no hay problema si luego son más
#   prime=109345121,		            #Un primo, para el hash con MAD
#   maptype='CHAINING',             #Tipo de Estructura de datos
#   loadfactor=2,                   #Factor de carga maximo. Distinto al factor de carga
#   comparefunction=compareKeys     #Funcion para comparar las llaves
#   )
# #El tamaño del arreglo en "mapa" es un primo > (numelements//loadfactor), en este caso primo > 2, primo == 3

# print('size: ', len(mapa["table"]["elements"])) #SOLO para propositos ilustrativos, NO USAR este codigo!!!

# mp.put(mapa, "k1", 1)
# mp.put(mapa, "k2", 1)
# mp.put(mapa, "k3", 1)
# mp.put(mapa, "k4", 1)
# mp.put(mapa, "k5", 1)
# print('size: ', len(mapa["table"]["elements"])) #SOLO para propositos ilustrativos, NO USAR este codigo!!!

# mp.put(mapa, "k6", 1) #Causa rehash a una tabla de tamaño primo > 2*size = 7, porque se supera el factor de carga maximo
# print('size: ', len(mapa["table"]["elements"])) #SOLO para propositos ilustrativos, NO USAR este codigo!!!





