cont= 0
soma_media= 0

while cont < 50:
    n1= float(input("digite um numero: "))
    n2= float (input("digite outro numero: "))
    n3= float (input("digite mais um numero:"))
    n4= float (input("digite o ultimo numero: "))
    nome= str (input(" digite seu nome: "))

    media= (n1+n2+n3+n4) / 4
    print (nome,",a media das suas notas é: ", media) 

    if media >=7:
        print ("parabens,", nome, ",você foi aprovado") 
    else:
        print ("estude mais na proxima,", nome, ",voce foi reprovado")

    cont= cont + 1
    media_total= soma_media / cont

print ( f"a média total é: {media_total: .2f}")

