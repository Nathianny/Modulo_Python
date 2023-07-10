# Neste jogo, o computador vai escolher um número aleatório e o jogador deve tentar adivinhar qual é esse número.
# O computador irá fornecer dicas dizendo se o palpite do jogador está acima ou abaixo do número correto.

# Proposta
# Melhorias na versão inicial do jogo
# - Adicionar limite máximo de tentativas
# - Permitir que o jogador escolha o intervalo de números
# - Incluir uma opção para o jogador jogar novamente ou sair do jogo após acertar ou esgotar todas as tentativas.'''
   
import random

def adivinhacao():
    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação de números!")
    print("Estou pensando em um número entre 1 e 100.")

    while True:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Tente um número maior!")
        elif palpite > numero_secreto:
            print("Tente um número menor!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break

adivinhacao()