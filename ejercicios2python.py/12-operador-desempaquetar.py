lista = [1, 2, 3, 4, 5]
print(lista)
print(1, 2, 3, 4, 5)
print(*lista)

lista2 = [1,2,3,4,5]

combinada = ["hola",*lista, *lista2]
print(combinada)

#todo los diciconarios se pueden combinar con el operador **

punto1 = {"x": 1, "y": 2}
punto2 = {"x": 10, "y": 20}

nuevoPunto = {**punto2, "lala":"hola mundo", **punto1, "z": 1}
print(nuevoPunto)