# Quatro times estão disputando as semifinais de um campeonato de futebol. Leia os gols que cada time marcou em suas partidas e informe qual time saiu vencedor. Em caso de empate em uma das partidas, leia o número de pênaltis cobrados corretamente (valores entre 0 e 5) para cada time. Supondo que haverá dois times vencedores das partidas, exiba-os. Exemplo de mensagem final: “Os times A e B estão na grande final!”.

#Armazena os times e suas pontuações
armazena_gols_times = {} #Dicionário
for i in range (0,4,1):
    time = input("Digite o nome do time:\n")
    gols = int(input("Digite quantos gols o time fez Bahia na partida time:\n"))
    armazena_gols_times[gols] = time

#Ordena, de forma crescente os times de acordo com suas pontuações
gols_ordenados = sorted(armazena_gols_times.keys())

#Revertelista ordenada e armazena os valores em nova lista. Assim obtemos uma lista em ordem decrescente 
index = len(gols_ordenados) -1
resultado = []
while index >= 0:
    resultado.append(gols_ordenados[index])
    index = index-1

#Armazena os dois primeiros valores da lista ordenanda em forma decrescente. Assim obtemos as duas maiores pontuações
timeA = armazena_gols_times.get(resultado[0])
timeB = armazena_gols_times.get(resultado[1])

#Printa resultado final
print("Os times ", timeA, " e ", timeB, " estão na grande final!")
