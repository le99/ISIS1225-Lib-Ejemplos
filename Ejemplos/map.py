import config as cf
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt


# Creacion
mapa = mp.newMap(maptype='CHAINING')
mapa = mp.newMap(maptype='PROBING')

mp.put(mapa, "k1", 1)               #mapa ={"k1": 1}
mp.put(mapa, "k2", 2)               #mapa ={"k1": 1, "k2": 2}
mp.put(mapa, "k3", 3)               #mapa ={"k1": 1, "k2": 2, "k3": 3}

val = me.getValue(mp.get(mapa, "k1"))   # => 1
val = mp.get(mapa, "k1")["value"]       # => 2

mp.remove(mapa, "k1")               #mapa ={"k2": 2, "k3": 3}

mp.size(mapa)                       # => 2
mp.isEmpty(mapa)                    # => False

mp.contains(mapa, "k2")             # => True

#Imprimir las llaves y valores
for k in lt.iterator(mp.keySet(mapa)):
  print("llave:" + k + ", valor: " + str(mp.get(mapa, k)["value"]))
  
#Imprimir los valores
for v in lt.iterator(mp.valueSet(mapa)):
  print(v)


#----------------------
# Creacion más complicada
#----------------------

def compareKeys(k1, entry):
    k2 = me.getKey(entry)
    if (k1 == k2):
        return 0
    elif (k1 > k2):
        return 1
    else:
        return -1

mapa = mp.newMap(
  numelements=800,                #Numero de elementos que se planean guardar, no hay problema si luego son más
  maptype='CHAINING', #Tipo de Estructura de datos
  loadfactor=2,       #Factor de carga maximo
  comparefunction=compareKeys)
#El tamaño del arreglo "mapa" es numelements/loadfactor = 400 
