import numpy as np

notas = np.array([
    [85, 92, 78], 
    [62, 75, 80],
    [62, 75, 80]
])
media = np.mean(notas, axis=1)
print("Média das notas por aluno:", media)

media_avaliacoes = np.mean(notas, axis=0)
print("Média das notas por avaliação:", media_avaliacoes)