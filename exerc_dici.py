alunos = {}

while True:
    nome = input("Nome do aluno (ou 'fim' para encerrar): ")
    if nome == 'fim':
        break
    notas = [float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: "))]
    alunos[nome] = notas

for nome, notas in alunos.items():
    media = sum(notas) / 3
    if media >= 7:
        print(nome)

while True:
    busca = input("Buscar aluno (ou 'fim' para encerrar): ")
    if busca == 'fim':
        break
    if busca in alunos:
        media = sum(alunos[busca]) / 3
        print(f"Média de {busca}: {media:.2f}")


#Estoque

estoque = {}

while True:
    produto = input("Produto (ou 'fim' para encerrar): ")
    if produto == 'fim':
        break
    quantidade = int(input("Quantidade: "))
    estoque[produto] = quantidade

while True:
    consulta = input("Consultar produto (ou 'fim' para encerrar): ")
    if consulta == 'fim':
        break
    print(estoque.get(consulta, "Produto não encontrado."))

while True:
    compra = input("Comprar produto (ou 'fim' para encerrar): ")
    if compra == 'fim':
        break
    qtd = int(input("Quantidade: "))
    if compra in estoque and estoque[compra] >= qtd:
        estoque[compra] -= qtd
        print(f"Estoque atualizado: {estoque[compra]}")

#Contagem letras

frase = input("Digite uma frase: ").lower()
contagem = {}

for letra in frase:
    if letra.isalpha():
        contagem[letra] = contagem.get(letra, 0) + 1

print(contagem)

#Votos

votos = {}

while True:
    candidato = input("Candidato (ou 'fim' para encerrar): ")
    if candidato == 'fim':
        break
    votos[candidato] = votos.get(candidato, 0) + 1

vencedor = max(votos, key=votos.get)
print(f"Vencedor: {vencedor} com {votos[vencedor]} votos")

#Agenda

contatos = {}

while True:
    acao = input("C - Cadastrar, B - Buscar, E - Excluir, Fim - Sair: ").lower()
    if acao == 'fim':
        break
    if acao == 'c':
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        contatos[nome] = telefone
    elif acao == 'b':
        nome = input("Nome para buscar: ")
        print(contatos.get(nome, "Contato não encontrado."))
    elif acao == 'e':
        nome = input("Nome para excluir: ")
        if nome in contatos:
            del contatos[nome]
            print("Contato excluído.")
