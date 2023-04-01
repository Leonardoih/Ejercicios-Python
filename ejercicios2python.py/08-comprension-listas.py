usuarios = [['Juan', 23], ['Maria', 19], ['Pedro', 22], ['Jose', 17], ["alejandro", 21]]

# nombres=[]
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
nombres =sorted([usuario[0].upper() for usuario in usuarios])
print(nombres)


# filtrar
nombre = [ [usuario[0].upper(), usuario[1]] for usuario in usuarios if usuario[1] == 20]
print(nombre)

#map    
nombres = list(map(lambda usuario :usuario[0].upper(), usuarios))
ordenado = (sorted(nombres))
print (ordenado)

menosUsarios = list(filter(lambda usuario: usuario[1] > 18, usuarios))
print(menosUsarios)
menosUsuarios = list(map(lambda usuario: usuario[0].lower(), filter(lambda usuario: usuario[1] > 18, usuarios)))
menosUsuarios.sort()
print(menosUsuarios)


menosUsuarios = [usuario[0].upper() for usuario in usuarios if usuario[1] > 18]
menosUsuarios.sort()
print(menosUsuarios)


menosUsuarios = [usuario[0].capitalize() for usuario in usuarios if usuario[1] > 18]
menosUsuarios.sort()
print(menosUsuarios)

menosUsuarios = [usuario[0].swapcase() for usuario in usuarios if usuario[1] > 18]
menosUsuarios.sort()
print(menosUsuarios)

