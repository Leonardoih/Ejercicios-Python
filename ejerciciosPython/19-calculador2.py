print("bienvenidos a la calculadora \npara salir escribe salir \nlas operaciones son suma, multi, div, resta")
resultado = ""

while True:
    if not resultado:
        resultado = input("ingrese un numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    op = input("ingrese una operacion: ")
    if op.lower() == "salir":
        break

    n2 = input("ingrese un numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("operacion no valida")
        break
    
    print(f"El resultado es {resultado}")