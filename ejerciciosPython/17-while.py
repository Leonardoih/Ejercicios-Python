# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2


comando2 = ""
res = ""

while comando2 != "hola":

    comando2 = input("$")
    res += comando2
    print(res)

comando = ""
while comando.lower() != "salir":
    try:
        comando = input("$ ")
        print(comando)
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario")
        comando = "salir"
