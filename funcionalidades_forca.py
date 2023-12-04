import random
import os


def escolherPalavraDoDicionario():
# obtém o caminho atual
    path = os.path.dirname(os.path.abspath(__file__))
    # concatena o caminho atual com o nome do arquivo desejado
    arquivo_palavras = os.path.join(path, 'ListaDePalavras.txt')

    # Escolhendo a palavra
    with open(arquivo_palavras, 'r') as arquivo_de_palavras:
        todas_as_palavras = arquivo_de_palavras.readlines()
    palavra = str(random.choice(todas_as_palavras)).lower()
    return palavra

def disfarcarPalavra(palavra):
    # Máscara da palavra
    mascara = []
    for letra in range(len(palavra) - 1):
        mascara.append('_')
    return mascara

# Variaveis padrão iniciais do jogo
letras_tentadas = []
