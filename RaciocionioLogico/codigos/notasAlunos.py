#Objetivo: Elaborar um programa que lê o nome e a nota de um aluno, depois exibe esses dados, mas com a nota formatada para exibir apenas uma casa decimal.
nome = input("Olá, digite seu nome:")
nota = float(input("Digite sua nota:"))

print("Nome do aluno:\n", nome )
print("Nota do aluno:{:,.1f}".format(nota))
