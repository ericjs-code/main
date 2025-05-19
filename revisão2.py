
cont = 0
while cont < 10:
    print ("digite um numero: ")
    numero = int(input())
    cont += 1
    if  numero % 2 == 0:
     print ("par")   
    else:
     print ("impar")
    break
print ("fim do programa")