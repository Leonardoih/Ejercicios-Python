

primer = {1,1,2,2,3,4}
#todo set significa grupo o cojunto
print(primer)
primer.add(5)
#primer.remove(2)
print(primer)

segundo = [3,4,6,6,7,7,8,8,9,9,10,10]
print(segundo)
segundo = set(segundo)
print(segundo)
#3 este es el operador de union |
print (primer | segundo)
#* este es el operador de interseccion &
print (primer & segundo)
#3 este es el operador de diferencia -
print (segundo - primer)
#3 este es el operador de diferencia simetrica ^
print (segundo ^  primer)