#Função que retorna menor valor de uma lista
def menor_valor(lista):

    menor = lista[0]
    for i in lista:
        if(i < menor):
            menor = i
    return menor

#Armazena valores na lista
lista = []
print("Digite 3 valores:\n")
for i in range(0,3,1):
    numeros = int(input())
    lista.append(numeros)

# Ordena lista de forma crescente
numeros_ordenados = []
for i in range (0,len(lista), 1):
    menor = menor_valor(lista)
    numeros_ordenados.append(menor)
    lista.remove(menor)
    
#Printa lista ordenada
for i in numeros_ordenados:
        print()
        print(i)