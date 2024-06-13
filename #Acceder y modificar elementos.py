#Acceder y modificar elementos

hombres = ["alan","pablo","oscar"]

mujeres = ["juana", "sara","olivia"]

personas = []

personas.append(hombres)
personas.append(mujeres)

print(personas)

print(len(personas))

#indice para que solo se imprima el primer nombre de la segunda lista
print(personas[1][0])