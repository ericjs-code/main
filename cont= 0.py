cont= 1
while cont <= 10:
    print(cont, "x 5=", cont * 5 )
    cont += 1

#usando for

con = 5
for i in range (1,11):
    print (f" {con} x {i}= {i * con}")
  

#soma dos numeros impares 
num1= int(input("digite um numero: "))
soma = 0
conta= 0

while conta <= num1:
    if conta%2 == 1:
        soma += conta
    conta = conta + 1

print (f"sua soma é igual a {soma}") 