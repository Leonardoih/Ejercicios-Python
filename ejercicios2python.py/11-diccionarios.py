punto = {"x": 25, "y": 50}
# 3 print(punto)
# *print(punto["x"])
# * print(punto["y"])
punto["nuevo"] = 45
# 3 print(punto)

if "lala" in punto:
    print(punto["lala"])


#! print(punto.get("x"))
print(punto.get("lala", 97))

del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)


for llave, valor in punto.items():
    print(valor, llave)


usuarios = [{"id": 1,  "nombre": "juan", "edad": 25},
            {"id": 2,  "nombre": "leo", "edad": 45},
            {"id": 3,  "nombre": "Clau", "edad": 44},
            {"id": 4,  "nombre": "feliz", "edad": 44},

            ]
for nombre in usuarios:
    print(nombre["nombre"])
for id in usuarios:
    print(id["id"])
    
for edad in usuarios:
    print(edad["edad"])
    

