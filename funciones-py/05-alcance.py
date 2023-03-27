saludo = "este es el alcance global"


def saludar():
    global saludo
    saludo = "hola mundo"
    


def saludar_leo():
    saludo = "hola leo"
    
resultado1 = saludo + "este es el global"
print (resultado1)
saludar()
resultado2 = saludo + "este es otro valor"
print(resultado2)
