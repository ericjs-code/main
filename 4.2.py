maior = 0
for i in range(6):
    num1 = int(input("digite um numero: "))
    if num1 > 100:
        maior += 1
print (f" temos {maior} numeros maiores que 100")
