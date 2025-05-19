alunos = []
while True:
    nome = str (input("digite o nome do aluno: "))
    alunos.append(nome)
    continuar= str(input( "quer continuar? sim ou não "))
    if continuar == 'não':
     break
alunos.sort()
print (alunos)

#2 
notas= []
for a in range (5):
   alunos= float(input("digite a nota do aluno: "))
   notas.append(alunos)

media= sum(notas) / len(notas)
print (f"A média das notas é: {media:.2f}")
