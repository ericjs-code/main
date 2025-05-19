cont = 0 
maior_num= 0
while cont < 5:
    numero= int(input("digite um numero: "))
    cont += 1
    
    if numero > maior_num:
        maior_num = numero
    else:   
        maior_num = maior_num
print("O maior numero é: ", maior_num)