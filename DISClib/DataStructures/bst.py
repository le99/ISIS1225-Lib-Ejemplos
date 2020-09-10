"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config
from DISClib.DataStructures import bstnode
from DISClib.ADT import list as lt
assert config


#  ------------------------------------------------------------
#                       API TAD_BST
#  ------------------------------------------------------------

def newMap(compfunction):
    """
    Crea una tabla de simbolos ordenada.
    Args:
        node: El nodo a revisar

    Returns:
        True si el nodo es rojo, False de lo contrario
    Raises:
        Excep
    """
    bst = {'root': None,
           'cmpfunction': compfunction}
    return bst


def put(bst, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe,
    se reemplaza el valor.
    Args:
        bst: El BST
        key: La llave asociada a la pareja
        value: El valor asociado a la pareja
    Returns:
        El arbol con la nueva pareja
    Raises:
        Excep
    """
    bst['root'] = insertNode(bst['root'], key, value, bst['cmpfunction'])
    return bst


def get(bst, key):
    """
    Retorna la pareja lleve-valor con llave igual  a key
    Args:
        bst: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        El arbol con la nueva pareja
    Raises:
        Excep
    """
    node = getNode(bst['root'], key, bst['cmpfunction'])
    return node


def remove(bst, key):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Args:
        bst: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        El arbol sin la pareja key-value
    Raises:
        Excep
    """
    bst['root'] = removeNode(bst['root'], key, bst['cmpfunction'])
    return bst


def contains(bst, key):
    """
    Informa si la llave key se encuentra en la tabla de hash
    Args:
        bst: El arbol de búsqueda
        key: La llave a buscar
    Returns:
        True si la llave está presente False en caso contrario
    Raises:
        Excep
    """
    return (get(bst, key) is not None)


def size(bst):
    """
    Retorna el número de entradas en la tabla de simbolos
    Args:
        bst: El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Raises:
        Excep
    """
    return sizeTree(bst['root'])


def isEmpty(bst):
    """
    Informa si la tabla de hash se encuentra vacia
    Args:
        bst: El arbol de búsqueda
    Returns:
        True si la tabla es vacía, False en caso contrario
    Raises:
        Excep
    """
    return (bst['root'] is None)


def keySet(bst):
    """
    Retorna una lista con todas las llaves de la tabla de hash
    Args:
        bst: La tabla con los elementos
    Returns:
        Una lista con todas las llaves
    Raises:
        Excep
    """
    klist = lt.newList()
    klist = keySetTree(bst, klist)
    return klist


def valueSet(bst):
    """
    Construye una lista con los valorers de la tabla
    Args:
        bst: La tabla con los elementos
    Returns:
        Una lista con todos los valores
    Raises:
        Excep
    """
    vlist = lt.newList()
    vlist = valueSetTree(bst, vlist)
    return vlist


def minKey(bst):
    """
    Retorna la menor llave de la tabla de simbolos
    Args:
        bst: La tabla con los elementos
    Returns:
        La menor llave de la tabla
    Raises:
        Excep
    """
    node = minKeyNode(bst['root'])
    if (node is not None):
        return node['key']
    return node


def maxKey(bst):
    """
    Retorna la mayor llave de la tabla de simbolos
    Args:
        bst: La tabla de simbolos
    Returns:
        La mayor llave de la tabla
    Raises:
        Excep
    """
    node = maxKeyNode(bst['root'])
    if (node is not None):
        return node['key']
    return node


def deleteMin(bst):
    """
    Encuentra y remueve la menor llave de la tabla de simbolos
    y su valor asociado
    Args:
        bst: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Excep
    """
    return deleteMinTree(bst['root'])


def deleteMax(bst):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado
    Args:
        bst: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la mayor llave
    Raises:
        Excep
    """
    return deleteMaxTree(bst['root'])


def floor(bst, key):
    """
    Retorna la llave mas grande en la tabla de simbolos,
    menor o igual a la llave key
    Args:
        bst: La tabla de simbolos
        key: La llave de búsqueda
    Returns:
        La llave más grande menor o igual a key
    Raises:
        Excep
    """
    node = floorKey(bst['root'], key, bst['cmpfunction'])
    if (node is not None):
        return node['key']
    return node


def ceiling(bst, key):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key
    Args:
        bst: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Excep
    """
    node = ceilingKey(bst['root'], key, bst['cmpfunction'])
    if (node is not None):
        return node['key']
    return node


def select(bst, pos):
    """
    Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
    Args:
        bst: La tabla de simbolos
        pos: la pos-esima llave mas pequeña
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Excep
    """
    node = selectKey(bst['root'], pos)
    if (node is not None):
        return node['key']
    return node


def rank(bst, key):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        bst: La tabla de simbolos
        pos: la pos-esima llave mas pequeña
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Excep
    """
    return rankKeys(bst['root'], key, bst['cmpfunction'])


def height(bst):
    """
    Retorna la altura del arbol de busqueda
    Args:
        bst: La tabla de simbolos
    Returns:
        La altura del arbol
    Raises:
        Excep
    """
    return heightTree(bst['root'])


def keys(bst, keylo, keyhi):
    """
    Retorna todas las llaves del arbol que se encuentren entre
    [keylo, keyhi]

    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Excep
    """
    lstkeys = lt.newList('SINGLELINKED', bst['cmpfunction'])
    lstkeys = keysRange(bst['root'], keylo, keyhi, lstkeys, bst['cmpfunction'])
    return lstkeys


def values(bst, keylo, keyhi):
    """
    Retorna todas los valores del arbol que se encuentren entre
    [keylo, keyhi]

    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Excep
    """
    lstvalues = lt.newList('SINGLELINKED', bst['cmpfunction'])
    lstvalues = valuesRange(bst['root'], keylo, keyhi, lstvalues,
                            bst['cmpfunction'])
    return lstvalues


# _____________________________________________________________________
#            Funciones Helper
# _____________________________________________________________________


def insertNode(root, key, value, cmpfunction):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe,
    se reemplaza el valor.
    Args:
        root: La raiz del arbol
        key: La llave asociada a la pareja
        value: El valor asociado a la pareja
        cmpfunction : Función de comparación
    Returns:
        El arbol con la nueva pareja
    Raises:
        Excep
    """
    if (root is None):
        root = bstnode.newNode(key, value, 1)
    else:
        cmp = cmpfunction(key, root['key'])
        if (cmp < 0):           # La llave a insertar es menor que la raiz
            root['left'] = insertNode(root['left'], key, value, cmpfunction)

        elif (cmp > 0):        # La llave a insertar es mayor que la raiz
            root['right'] = insertNode(root['right'], key, value, cmpfunction)

        else:                  # La llave a insertar es igual que la raiz
            root['value'] = value
    leftsize = sizeTree(root['left'])
    rightsize = sizeTree(root['right'])
    root['size'] = 1 + leftsize + rightsize
    return root


def getNode(root, key, cmpfunction):
    """
    Retorna la pareja lleve-valor con llave igual  a key
    Args:
        root: El arbol de búsqueda
        key: La llave asociada a la pareja
        cmpfunction: Función de comparación
    Returns:
        El arbol con la nueva pareja
    Raises:
        Excep
    """
    node = None
    if (root is not None):
        cmp = cmpfunction(key, root['key'])
        if (cmp == 0):
            node = root
        elif (cmp < 0):
            node = getNode(root['left'], key, cmpfunction)
        else:
            node = getNode(root['right'], key, cmpfunction)
    return node


def removeNode(root, key, cmpfunction):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Args:
        bst: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        El arbol sin la pareja key-value
    Raises:
        Excep
    """
    if (root is not None):
        cmp = cmpfunction(key, root['key'])
        if (cmp == 0):  # La llave es la que se busca
            if (root['right'] is None):   # No tiene hijo derecho
                return root['left']
            elif (root['left'] is None):  # No tiene hijo izquierdo
                return root['right']
            else:      # se cambia por el menor de los mayores
                elem = root
                root = minKeyNode(elem['right'])
                root['right'] = deleteMinTree(elem['right'])
                root['left'] = elem['left']
        elif (cmp < 0):
            root['left'] = removeNode(root['left'], key, cmpfunction)
        else:
            root['right'] = removeNode(root['right'], key, cmpfunction)
        root['size'] = 1 + sizeTree(root['left']) + sizeTree(root['right'])
    return root


def sizeTree(root):
    """
    Retornar el número de entradas en la a partir un punto dado
    Args:
        bst: El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Raises:
        Excep
    """
    if (root is None):
        return 0
    else:
        return root['size']


def valueSetTree(root, klist):
    """
    Construye una lista con los valorers de la tabla
    Args:
        root: El arbol con los elementos
        klist: La lista de respuesta
    Returns:
        Una lista con todos los valores
    Raises:
        Excep
    """
    if (root is not None):
        valueSetTree(root['left'], klist)
        lt.addLast(klist, root['value'])
        valueSetTree(root['right'], klist)
    return klist


def keySetTree(root, klist):
    """
    Construye una lista con las llaves de la tabla
    Args:
        root: El arbol con los elementos
        klist: La lista de respuesta
    Returns:
        Una lista con todos las llaves
    Raises:
        Excep
    """
    if (root is not None):
        keySetTree(root['left'], klist)
        lt.addLast(klist, root['key'])
        keySetTree(root['right'], klist)
    return klist


def minKeyNode(root):
    """
    Retorna la menor llave de la tabla de simbolos
    Args:
        root: La raiz del arbol de busqueda
    Returns:
        El elemento mas izquierdo del arbol
    Raises:
        Excep
    """
    min = None
    if (root is not None):
        if (root['left'] is None):
            min = root
        else:
            min = minKeyNode(root['left'])
    return min


def maxKeyNode(root):
    """
    Retorna la mayor llave de la tabla de simbolos
    Args:
        bst: La tabla de simbolos
    Returns:
        El elemento mas derecho del árbol
    Raises:
        Excep
    """
    max = None
    if (root is not None):
        if (root['right'] is None):
            max = root
        else:
            max = maxKeyNode(root['right'])
    return max


def deleteMinTree(root):
    """
    Encuentra y remueve la menor llave de la tabla de simbolos
    y su valor asociado
    Args:
        root: La raiz del arbol de busqueda
    Returns:
        El arbol de busqueda
    Raises:
        Excep
    """
    if (root is not None):
        if (root['left'] is None):
            return root['right']
        else:
            root['left'] = deleteMinTree(root['left'])
        root['size'] = sizeTree(root['left']) + sizeTree(root['right']) + 1
    return root


def deleteMaxTree(root):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado
    Args:
        root: el arbol de busqueda
    Returns:
        El árbol de búsqueda sin la mayor llave
    Raises:
        Excep
    """
    if (root is not None):
        if (root['right'] is None):
            return root['left']
        else:
            root['right'] = deleteMaxTree(root['right'])
        root['size'] = sizeTree(root['left']) + sizeTree(root['right']) + 1
    return root


def floorKey(root, key, cmpfunction):
    """
    Retorna la llave mas grande en la tabla de simbolos,
    menor o igual a la llave key
    Args:
        bst: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la mayor llave
    Raises:
        Excep
    """
    if (root is not None):
        cmp = cmpfunction(key, root['key'])
        if (cmp == 0):
            return root
        if (cmp < 0):
            return floorKey(root['left'], key, cmpfunction)
        t = floorKey(root['right'], key, cmpfunction)
        if (t is not None):
            return t
        else:
            return root
    return root


def ceilingKey(root, key, cmpfunction):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key
    Args:
        bst: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Excep
    """
    if (root is not None):
        cmp = cmpfunction(key, root['key'])
        if (cmp == 0):
            return root
        if (cmp < 0):
            t = ceilingKey(root['left'], key, cmpfunction)
            if (t is not None):
                return t
            else:
                return root
        return ceilingKey(root['right'], key, cmpfunction)
    return None


def selectKey(root, key):
    """
    Retorna la k-esima llave mas pequeña de la tabla
    Args:
        bst: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Excep
    """
    if (root is not None):
        cont = sizeTree(root['left'])
        if (cont > key):
            return selectKey(root['left'], key)
        elif (cont < key):
            return selectKey(root['right'], key-cont-1)
        else:
            return root
    return root


def rankKeys(root, key, cmpfunction):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        bst: La tabla de simbolos
        pos: la pos-esima llave mas pequeña
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Excep
    """
    if (root is not None):
        cmp = cmpfunction(key, root['key'])
        if (cmp < 0):
            return rankKeys(root['left'], key, cmpfunction)
        elif (cmp > 0):
            leftsize = sizeTree(root['left'])
            rank = rankKeys(root['right'], key, cmpfunction)
            total = 1 + leftsize + rank
            return total
        else:
            return sizeTree(root['left'])
    return 0


def heightTree(root):
    """
    Retorna la altura del arbol de busqueda
    Args:
        root: La tabla de simbolos
    Returns:
        La altura del arbol
    Raises:
        Excep
    """
    if (root is None):
        return -1
    else:
        return 1 + max(heightTree(root['left']),  heightTree(root['right']))


def keysRange(root, keylo, keyhi, lstkeys, cmpfunction):
    """
    Retorna todas las llaves del arbol en un rango dado
    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Excep
    """
    if (root is not None):
        complo = cmpfunction(keylo, root['key'])
        comphi = cmpfunction(keyhi, root['key'])

        if (complo < 0):
            keysRange(root['left'], keylo, keyhi, lstkeys, cmpfunction)
        if ((complo <= 0) and (comphi >= 0)):
            lt.addLast(lstkeys, root['key'])
        if (comphi > 0):
            keysRange(root['right'], keylo, keyhi, lstkeys, cmpfunction)
    return lstkeys


def valuesRange(root, keylo, keyhi, lstvalues, cmpfunction):
    """
    Retorna todas los valores del arbol en un rango dado por
    [keylo, keyhi]
    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superior
    Returns:
        Las llaves en el rago especificado
    Raises:
        Excep
    """
    if (root is not None):
        complo = cmpfunction(keylo, root['key'])
        comphi = cmpfunction(keyhi, root['key'])

        if (complo < 0):
            keysRange(root['left'], keylo, keyhi, lstvalues, cmpfunction)
        if ((complo <= 0) and (comphi >= 0)):
            lt.addLast(lstvalues, root['value'])
        if (comphi > 0):
            keysRange(root['right'], keylo, keyhi, lstvalues, cmpfunction)
    return lstvalues
