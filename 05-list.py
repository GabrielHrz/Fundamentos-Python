# Las listas son ordenadas y permiten VALORES repetidos
list_numbers = [1, 2, 3, 4, 5, 6]
# las listas puedesn ser mixtas
list_mixtas = [1, 2, 3, 'a', 'b', 'c', [1, 2, 3]]
# los sets son ordenados y NO permiten valores repetidos
set_numbers = {1, 2, 3, 4, 5, 5}

print(list_mixtas)
print(type(list_mixtas))


# Metodos

# append
# adiciona un valor a la final de la lista
list_numbers.append(7)
print(list_numbers)

# Borra el ultimo valor
list_numbers.pop()
print(list_numbers)

# remove
# remueve el valor indicado, es decir el 4, NO borra el indice 4, borra el numero 4 de
# la lista
list_numbers.remove(4)
print(list_numbers)


# count
# Cuenta cuantas veces aparece cierto valor
print(list_numbers.count(2))

# copy
# copia el valor de una lista

# sort
# ordena la lista

# count
# cuenta cuantas veces aparece algo
