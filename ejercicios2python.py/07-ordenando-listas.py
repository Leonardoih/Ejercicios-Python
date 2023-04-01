nuemrosAlAzar = [1, 2, 80, 4, 5, 10, 67, 38, 9,  45, 21]

nuemrosAlAzar.sort(reverse=True)

#print(nuemrosAlAzar)

numeros2 = sorted(nuemrosAlAzar, reverse=True)
print(numeros2)

usuarios =[['Juan', 23], ['Maria', 19], ['Pedro', 22], ['Jose', 185]]




usuarios.sort(key=lambda elemento:elemento[1], reverse=True)
print(usuarios)
usuarios.sort(key=lambda elemento:elemento[1])
print(usuarios)