# Solicita o número de alunos
alunos = int(input("Digite o número de alunos: "))

# Variáveis para armazenar o nome e a maior nota
maior_nota = 0
aluno_com_maior_nota = ""

# Loop para registrar as notas dos alunos
while alunos > 0:
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    
    # Verifica se a nota atual é a maior
    if nota > maior_nota:
        maior_nota = nota
        aluno_com_maior_nota = nome
    
    alunos -= 1  # Decrementa o contador de alunos

# Exibe o aluno com a maior nota
print(f"O aluno com a maior nota é {aluno_com_maior_nota} com {maior_nota}.")