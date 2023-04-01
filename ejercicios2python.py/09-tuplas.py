numero = (1, 2, 3, 4, 5)+( 6, 7, 8, 9, 10)

print(numero)

punto = tuple([1,2])
print(punto)

menosNumeros = numero[:2]
print(menosNumeros)

primero, segundo,tercero ,*resto = numero
print(primero, segundo,tercero, resto)
for n in numero:
    print(n)
    

listaNuemros = list(numero)
listaNuemros[5-1+3-1] = "hola"

print(listaNuemros)