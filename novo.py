cont= int
n1= int (input("digite o numero para contagem: "))
n2= int (input("digite o numero para contagem: "))

if n1 < n2:
    while n1 <= n2:
        print(n1)
        n1 += 1 
elif n1 > n2:
    while n1 >= n2:
        print(n1)
        n1 -= 1
else:
    print(f"os numeros são iguais {n1}")
    