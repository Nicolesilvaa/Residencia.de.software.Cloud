#Verifica se um valor é par ou ímpar

x = int(input("Olá, usuário! Digite um valor: "))

flag = 'S'
while(flag == 'S'):

    if(x % 2 == 0):
        print("Número é par")
    else:
        print("Número ímpar")
    
    flag = (input("Deseja continuar? Digite S Para sim, ou Y para não\n"))

print("Programa finalizado.")
