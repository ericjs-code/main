cont = 0
maior = 0
while cont < 6:
    num1 = int(input("digite um numero: "))
    cont += 1
    if num1 < 100:
        num2= num1
        print (f" o numero {num2} é menor que 100")
    elif num1 == 100:
        print (f" o numero {num1} é igual a 100")
    else:
        print (f" o numero {num1} é maior que 100")
        maior =+ 1
print (f" temmos {maior} numeros maiores que 100")
