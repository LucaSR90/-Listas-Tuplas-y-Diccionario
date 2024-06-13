#Filtrar elementos 

num_par =[2, 4, 6, 8, 12, 14, 16]

num_impar =[3, 5, 7, 9, 11, 13, 15]

num = []

for x in num_par:
    if (x % 4) ==0:
        num.append(x)

# va a colocar solo los numeros pares que son multiplos de 4

for y in num_impar:
  if(y % 5) == 0:
    num.append(y)

#colocara demntro solo los numeros que sean impares y multiplos de 5

print(num)