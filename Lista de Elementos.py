# Lista de Elementos

numeros =[2,3,4,5, 6,7, 8,9,10,11, 12, 13,14,15, 16]

num_filter = []

# va a colocar solo los numeros pares que son multiplos de 4
for x in numeros:
    if (x % 4 == 0) and (x % 2==0):
        num_filter.append(x)


print(num_filter)