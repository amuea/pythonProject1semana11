matriz = [
    [890, 89, 80],
    [678, 9, 70],
    [789, 90,904]
]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def ordenar_fila_con_quicksort(matriz, fila):
    matriz[fila] = quicksort(matriz[fila])


fila_a_ordenar = 1
ordenar_fila_con_quicksort(matriz, fila_a_ordenar)
for fila in matriz:
    print(fila)