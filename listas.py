numeros:list[int] = [1, 2, 4, 5, 10, 7, 99]
#[1][2][4][5][10]
# 0  1  2  3  4
print(numeros[0])
print(numeros[1])
print(numeros[-1])
print(numeros[1:4])
numeros[4] = 77
print(numeros[4]) 

#Agregar un elemento al final de la lista
numeros.append(100)
print(numeros[-1])

#Insertar un elemento en un índice específico
numeros.insert(3, 88)
print(numeros[3])

otra_lista = [55, 33, 230]
print(numeros)

#Extender la lista con otra lista
numeros.extend(otra_lista)
print(numeros)

#Eliminar un elemento específico por valor
numeros.remove(77)
print(numeros)

#Eliminar el último elemento de la lista
numeros.pop()
print(numeros)

#Eliminar un elemento por índice
numeros.pop(4)
print(numeros)

#Eliminar todos los elementos de la lista
#numeros.clear()
#print(numeros)

#Revertir el orden de la lista
numeros.reverse()
print(numeros)

#Ordenar la lista en orden ascendente
numeros.sort()
print(numeros)

#Ordenar la lista en orden descendente
numeros.sort(reverse=True)
print(numeros)

#Obtener la longitud de la lista
print("longitud:", len(numeros)) # logintud:int = len(numeros)

#Obtener el menor elemento
print("minimo:", min(numeros)) # minimo:int = min(numeros)

#Obtener el mayor elemento
print("maximo:", max(numeros)) # maximo:int = min(numeros)

#Calcular la suma de todos los elementos
print("sumatoria:", sum(numeros)) #sumatoria:int = sum(numeros)

frutas = ['manzana', 'naranja', 'banana', 'manzana', 'uva', 'manzana']

#Contar cuántas veces aparece 'manzana'
print("aparece:", frutas.count('manzana'))

print(frutas)
for fruta in frutas:
    print("fruta",fruta.upper())
