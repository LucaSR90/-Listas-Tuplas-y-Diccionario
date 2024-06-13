# Acceder y modificar elementos:
datos_personales = {
    "nombre": "luca",
    "edad": 19,
    "ocupacion": "Estudiante",
    "hobbies": ["leer", "correr", "cocinar"]
}

nombre = datos_personales["nombre"]
print(f"Nombre: {nombre}")

edad = datos_personales["edad"]
print(f"Edad: {edad}")

ocupacion = datos_personales["ocupacion"]
print(f"Ocupación: {ocupacion}")

primer_hobbie = datos_personales["hobbies"][0]
print(f"Primer hobbie: {primer_hobbie}")

datos_personales["edad"] = 20
datos_personales["ocupacion"] = "Gerente"
datos_personales["hobbies"][1] = "nadar"

print("Diccionario modificado:")
print(datos_personales)
