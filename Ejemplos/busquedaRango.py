# Usando Python

from bisect import bisect_left, bisect_right

lista = [
  {
    "id": 1,
    "loud": 2
  },
  {
    "id": 2,
    "loud": 1
  },
  {
    "id": 3,
    "loud": 3
  },
  {
    "id": 4,
    "loud": 2
  }
]


lista.sort(key=lambda x: x["loud"])
listaLoud = [v["loud"] for v in lista]
print(listaLoud)

left = bisect_left(listaLoud, 2)
right = bisect_right(listaLoud, 2)

print("Elementos entre 2 y 2")
print(lista[left:right])


# https://docs.python.org/3/library/bisect.html
# https://docs.python.org/3/howto/sorting.html
# https://www.geeksforgeeks.org/find-the-number-of-elements-greater-than-k-in-a-sorted-array/?ref=lbp