import random
import os

# obtém o caminho atual
path = os.path.dirname(os.path.abspath(__file__))
# concatena o caminho atual com o nome do arquivo desejado
arquivo_palavras = os.path.join(path, 'ListaDePalavras.txt')

# Escolhendo a palavra
with open(arquivo_palavras, 'r') as arquivo_de_palavras:
    todas_as_palavras = arquivo_de_palavras.readlines()
palavra = str(random.choice(todas_as_palavras)).lower()

# Máscara da palavra
mascara = []
for letra in range(len(palavra) - 1):
    mascara.append('_')


# Escolher dificuldade
print('Escolha entre as dificuldades: fácil, médio, difícil.')
escolher_dificuldade = input('Qual a dificuldade? ').lower().replace(' ', '')
if escolher_dificuldade == 'facil' or escolher_dificuldade == 'fácil':
    chances = len(palavra) * 2
elif escolher_dificuldade == 'medio' or escolher_dificuldade == 'médio':
    chances = len(palavra) * 1.5
    chances = int(round(chances))
elif escolher_dificuldade == 'dificil' or escolher_dificuldade == 'difícil':
    chances = len(palavra)
else:
    print('Resposta inválida.')
    exit()

# Variaveis padrão iniciais do jogo
letras_tentadas = []
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Informações iniciais
print('\n')
print('digite "chutar" para tentar acertar a palavra, se acertar você vence, mas se errar perde!')
print('digite "letras" para ver as letras que não tentou! \n ')

print(mascara)
print(f'Suas chances: {chances} \n')

while True:
    chute = input('Digite a letra: ').lower().replace(' ', '')

    # Código relacionado ao chute da letra
    if chute not in palavra:
        chances -= 1
        if len(chute) == 1:
            letras_tentadas.append(chute)
    else:
        index = 0
        for letra in palavra:
            if letra == chute:
                mascara[index] = chute
            index += 1

    # Verificando se ganhou
    if mascara.count('_') == 0:
        print('Parabéns! Você ganhou! =D')
        exit()

    # Chute final
    if chute == 'chutar':
        chute_final = input('Qual a palavra? ')
        if chute_final in palavra and len(chute_final) == len(palavra):
            print('Parabéns! Você ganhou! =D')
            exit()
        else:
            print('Perdeu, quem sabe na próxima? =/')
            exit()

    # Letras restantes
    if chute == 'letras':
        chances += 1
        print(f'{alfabeto}\n')

    # Atualizando as letras restantes
    if chute in alfabeto:
        alfabeto.remove(chute)

    # Informações da rodada
    print(mascara)
    print(f'Chances restantes: {chances}')
    print(f'Letras tentadas: {letras_tentadas} \n\n')
