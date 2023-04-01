def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def alreves(texto):
    texto1_al_reves = ""
    for char in texto:
        texto1_al_reves = char + texto1_al_reves
    return texto1_al_reves
   # hola de nuevo


numeros = 1234560


def es_palindromo(texto):
    global numeros
    texto = no_space(texto)
    texto_al_reves = alreves(texto)
    print(texto_al_reves.lower())
    input()

    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("Amo la paloma"))
print(es_palindromo("Leonardo"))
es_palindromo("Amo la paloma")
print("hola mundo")
leo = True
numero = 12346.2
print("hola mundo")
