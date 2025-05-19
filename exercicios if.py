num1= int(input("digite um numero: "))
if num1 % 2 == 0 :
  print ("seu resultado é par")
else:
  print ("seu numero é impar")

#exercicio 2

num= float(input("digite um numero: "))
if num > 0:
    print ("seu numero é positivo")
elif num < 0:
    print ("seu numero é negatico")
else:
   print ("seu numero é zero")

   #exercicio 3

letra= str(input("digite uma letra: "))
if letra == "a" or letra =="e" or letra =="i" or letra == "o" or letra == "u":
    print ("sua letra é uma vogal")
else:
   print ("sua letra é uma consoante")

   
#exercicio 4

angulo1= int(input("escreva um angulo deste tringulo: "))
angulo2= int (input( "escreva o segundo angulo: "))
angulo3=int (input(" escreva o terceiro angulo: "))
if angulo1 == angulo2 == angulo3: 
   print("seu triangulo é equilatero")
elif angulo1 != angulo2 != angulo3:
   print ("seu triangulo escaleno")
else:
  print ("seu triangulo é isosceles")

#exercicio 5

salario= float(input("digite seu salario: "))
anos= int (input("digite a quantos anos recebe este salario:"))
bonus= float(salario * (1.05))
if anos >= 5: 
  print("parabens voce ganhou um bonus! seu salario agora é: ", bonus )
else:
   print("voce nao ganhou um bonus:(")

#exercicio 6
valor1= float(input("digite o valor da sua compra: "))
if valor1 > 100:
  print ("voce recebeu um desconto de: ", valor1* (0.1))
else:
   print(" voce nao recebeu um desconto")

#exericio 7
idade= int(input("digite sua idade:"))
if idade >= 0 and idade <= 12:
   print ("voce é uma criança!")
elif idade > 12 and idade <= 17:
   print(" voce é adolescente!")
elif idade > 17 and idade <= 59:
   print ("voce é adulto!")
else:
   print("voce é um idoso!")


#exercicio 8
nota= float(input("digite sua nota: "))
if nota == 10 and nota >= 9:
   print("voce é nota A")
elif nota >= 7 and nota == 8.9:
   print (" voce é nota B")
elif nota >=5 and nota == 6.9:
   print (" voce é nota C")
elif nota <= 5 and nota == 0:
  print ("voce é nota D")
else:
   print ("nota inexistente")

#exercicio 9
salarioa= float(input("digite seu salario anual:"))
if salarioa == 1 and salario <= 20000:
   print ("seu imposto de renda é igual a 0")
elif salarioa >= 20001 and salarioa <= 50000:
  print ("voce pagara:", salario * (0.15))
else:
   print("seu imposto sera:", salarioa * (0.25))

#exercicio 10
idadea= int (input(" digite sua idade: "))
if idadea >= 18:
  print("voce é maior de idade e pode tirar cnh")
else:
   print(" voce é menor de idade e nao pode ter cnh")

#exercicio 11
temp= float (input("escreva uma temperatura em C para conversão:"))
print ("sua temperatura em fahrenheit:", (temp * 9/ 5) + 32)


#exercicio 12
peso= float(input ("digite seu peso em kg: "))
altura= float (input("digite sua altura em metros: "))
imc= peso/(altura ** 2)
if imc < 18.5 :
   print ("voce é abaixo do peso ideal")
elif imc >= 18.5 and imc < 25:
   print ("voce esta no peso ideal")
elif imc >= 25 and imc < 30:
   print (" voce esta sobrepeso")
else:
   print ("voce esta na condiçao de obesidade")

#exercicio 13
num2= int("digite um numero: ")
print(f"a tabuada do seu numero é {num2}")
for valor in range (1,11):
   print(f"{num2} x {i} = {i * num2}" )