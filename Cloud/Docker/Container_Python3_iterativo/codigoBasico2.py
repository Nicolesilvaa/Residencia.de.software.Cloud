#Verifica se um valor digitado pelo usuário é par ou ímpar 

flag = 'S'
while(flag == 'S'):

   x = int(input("Olá, usuário! Digite um valor: "))

   if(x % 2 == 0):
     print("Número é par")
   else:
     print("Número ímpar")

   flag = (input("Deseja continuar? Digite S Para sim, ou Y para não\n"))

print("Programa finalizado.")