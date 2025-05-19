alunos = {}

quantidade= int(input("quantos alunos deseja cadastrar?"))

for a in range (quantidade):
    nome= str(input("nome do aluno: "))
    nota= float(input("nota do aluno: "))
    alunos [nome] = nota

    if nota >= 7:
     print (f"o {nome} foi aprovado com {nota}")
    else:
     print (f"o {nome} foi reprovado com {nota}")

    print("\nResumo dos alunos:")

    for aluno, nota in alunos.items():

     status = "Aprovado" if nota >= 7 else "Reprovado"

    print(f"{aluno}: {nota} - {status}")