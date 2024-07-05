# Quatro times estão disputando as semifinais de um campeonato de futebol. Leia os gols que cada time marcou em suas partidas e informe qual time saiu vencedor. Em caso de empate em uma das partidas, leia o número de pênaltis cobrados corretamente (valores entre 0 e 5) para cada time. Supondo que haverá dois times vencedores das partidas, exiba-os. Exemplo de mensagem final: “Os times A e B estão na grande final!”.
gols = []
for i in range (1,4,1):
    gols.append(int(input("Digite os gols de cada time ")))

maior1 = 0
maior2 = 0

for time, i in gols:
    if(i > gols[maior1]):
        maior2 = maior1
        maior1 = time
    elif(maior2 > gols[maior2]):
        maior2 = time
print(f"Os times {maior1} e {maior2} estão na grande final!")