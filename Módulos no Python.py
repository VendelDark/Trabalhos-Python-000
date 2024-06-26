#1-
import math

numero_real = float(input("Digite um número real: "))
parte_inteira = math.floor(numero_real)
print("A parte inteira do número é:", parte_inteira)

#2-

import random

alunos = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos']

escolhido = random.choice(alunos)
print("O aluno escolhido para apagar o quadro é:", escolhido)


#3-

import random

alunos = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos']

ordem_apresentacao = random.sample(alunos, len(alunos))
print("Ordem de apresentação dos alunos:", ordem_apresentacao)

