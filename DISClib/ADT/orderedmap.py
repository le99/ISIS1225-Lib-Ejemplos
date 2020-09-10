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
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """


import config
from DISClib.DataStructures import orderedmapstructure as om
assert config


def newMap(omaptype='RBT', comparefunction=None):
    """
    Crea una tabla de simbolos ordenada.
    """
    return om.newMap(omaptype, comparefunction)


def put(map, key, value):
    """
    Ingresa una pareja llave,valor a la tabla.  Si la llave ya existe,
    se reemplaza el valor.
    """
    return om.put(map, key, value)


def get(map, key):
    """
    Retorna la pareja llave, valor, cuya llave sea igual a key.
    """
    return om.get(map, key)


def remove(map, key):
    """
    Elimina la pareja llave,valor, donde llave == key.
    """
    om.remove(map, key)


def contains(map, key, comparefunction):
    """
    Retorna True si la llave key se encuentra en la tabla
    o False en caso contrario.
    """
    return om.contains(map, key, comparefunction)


def size(map):
    """
    Retornar el número de entradas en la tabla
    """
    return om.size(map)


def isEmpty(map):
    """
    Informa si la tabla  se encuentra vacia
    """
    return om.isEmpty(map)


def keySet(map):
    """
    Retorna una lista con todas las llaves de la tabla
    """
    return om.keySet(map)


def valueSet(map):
    """
    Retorna una lista con todos los valores de la tabla
    """
    return om.valueSet(map)


def min(map):
    """
    Retorna la menor llave de la tabla de simbolos
    """
    return om.min(map)


def max(map):
    """
    Retorna la mayor llave de la tabla de simbolos
    """
    return om.max(map)


def deleteMin(map):
    """
    Encuentra y remueve la menor  llave de la tabla de simbolos
    y su valor asociado
    """
    return om.deleteMin(map)


def deleteMax(map):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado
    """
    return om.deleteMax(map)


def floor(map, key):
    """
    Retorna la llave mas grande en la tabla de simbolos,
    menor o igual a la llave key
    """
    return om.floor(map, key)


def ceiling(map, key):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key
    """
    return om.ceiling(map, key)


def select(map, k):
    """
    Retorna la k-esima llave mas pequeña de la tabla
    """
    return om.select(map, k)


def rank(map, key):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    """
    return om.rank(map, key)


def height(map):
    """
    Retorna la altura del arbol de busqueda
    """
    return om.height(map)


def keys(map, keylo, keyhi):
    """
    Retorna todas las llaves encontradas en el rango dado por keylo y keyhi
    """
    return om.keys(map, keylo, keyhi)


def values(map, keylo, keyhi):
    """
    Retorna todas los valores del arbol que se encuentren entre
    [keylo, keyhi]
    """
    return om.keys(map, keylo, keyhi)
