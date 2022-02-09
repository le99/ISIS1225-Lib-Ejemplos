import config as cf
from DISClib.ADT import list as lt


a = lt.newList('SINGLE_LINKED')   #Creacion de una lista vacia con listas sencillamente anlazadas
a = lt.newList('ARRAY_LIST')      #Creacion de una lista vacia con arreglos

#Agregar Elementos
lt.addFirst(a, 'a')               # ["a"]
lt.addFirst(a, 'b')               # ["b", "a"]
lt.addLast(a, 'c')                # ["b", "a", "c"]
lt.insertElement(a, "z", 2)       # ["b", "z", "a", "c"]
lt.insertElement(a, "x", 3)       # ["b", "z", "x", "a", "c"]
lt.size(a)                        # => 5

#Consultar
lt.firstElement(a)                # => "b"
lt.lastElement(a)                 # => "c"
lt.getElement(a, 3)               # => "x"
lt.isEmpty(a)                     # => False                    

#Cambiar un elemento
lt.changeInfo(a, 1, "w")          #["w", "z", "x", "a", "c"]

#Eliminar un elemento
lt.removeFirst(a)                 #["z", "x", "a", "c"]
lt.removeLast(a)                  #["z", "x", "a"]
lt.deleteElement(a, 2)            #["z", "a"]


# Recorrer una lista
for n in lt.iterator(a):
  pass
  
  
#=================================
# Ejemplos Avanzados
#=================================

def compararElementos(e1, e2):
    if (e1 == e2):
        return 0
    elif (e1 > e2):
        return 1
    return -1


a = lt.newList('ARRAY_LIST', 
    cmpfunction=compararElementos) #Creacion de una lista vacia, los elementos se pueden comparar con cmpfunction (para poder usar lt.isPresent)

lt.addLast(a, 'a')                # ["a"]
lt.addLast(a, 'b')                # ["a", "b"]
lt.addLast(a, 'c')                # ["a", "b", "c"]
lt.addLast(a, 'd')                # ["a", "b", "c", "d"]

#Intercambiar dos elementos
lt.exchange(a, 2, 4)              # ["a", "d", "c", "b"]
sublista = lt.subList(a, 2, 3)    # => ["d", "c", "b"]


lt.isPresent(a, "z")              # => 0, no esta 
lt.isPresent(a, "a")              # => 1, esta en la posicion 1 
lt.isPresent(a, "d")              # => 2, esta en la posicion 2






