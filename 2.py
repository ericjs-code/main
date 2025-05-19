cont = 0 
num1 = int(input("Digite o primeiro número: "))
while num1 > cont:
    cont += 1
    print(cont)
    if cont % 2 == 0:
     print("O número é par")
    else:
     print("O número é ímpar")  
       