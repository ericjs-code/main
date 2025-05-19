meu_dicionario = {}

quantidade = int(input("Quantas pares chave-valor deseja adicionar ao dicionário? "))

for i in range(quantidade):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    meu_dicionario[chave] = valor

print ("dicionario resultante: ", meu_dicionario)   