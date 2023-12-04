import os,pygame
from backend import adicionarNoBanco
from pygame.locals import *
import funcionalidades_forca
import time



blue = (0,0,255)
WINDOW_WIDTH  = 1300
WINDOW_HEIGHT = 750
#letra_camuflada_fonte = pygame.font.SysFont("Courier New", 35).render('_', 1, (0,0,0)) # WINDOW.blit(letra_camuflada_fonte , (200, 500))

# funcao definida para exibir mensagem na tela
def show_text( msg, color, x=WINDOW_WIDTH//2, y=WINDOW_WIDTH//2 ):
    global WINDOW
    text = font.render( msg, True, color)
    WINDOW.blit(text, ( x, y ) )

def adicionarMembros():
    imagem = pygame.image.load(os.path.abspath("jogoforca/kp/kelyr/forcak/kely/kforca/pau.png"))
    if chances == 7:
        imagem = pygame.image.load(os.path.abspath("jogoforca/kp/kelyr/forcak/kely/kforca/cabeza.jpg"))
    if chances == 6:
        imagem = pygame.image.load(os.path.abspath("jogoforca/kp/kelyr/forcak/kely/kforca/tronco.jpg"))
    if chances == 5:
        imagem = pygame.image.load(os.path.abspath("jogoforca/kp/kelyr/forcak/kely/kforca/bracodireito.jpg"))
    if chances == 4:
        imagem = pygame.image.load(os.path.abspath("jogoforca/kp/kelyr/forcak/kely/kforca/bracoesquerdo.jpg"))
    if chances == 3:
        imagem = pygame.image.load(os.path.abspath("jogoforca/kp/kelyr/forcak/kely/kforca/pernadireita.jpg"))
    if chances == 2:
        imagem = pygame.image.load(os.path.abspath("jogoforca/kp/kelyr/forcak/kely/kforca/pernaesquerda.jpg"))
    if chances == 1:
        imagem = pygame.image.load(os.path.abspath("jogoforca/kp/kelyr/forcak/kely/kforca/morte.jpg"))
    return imagem


pygame.init()

clock = pygame.time.Clock()

WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Text") # posicao forca:208 620

# criar a fonte (eh feito so uma vez)
font = pygame.font.SysFont(None, 80)
palavra = funcionalidades_forca.escolherPalavraDoDicionario()
chances = 8 #len(palavra)
mascara = funcionalidades_forca.disfarcarPalavra(palavra)
letras_tentadas = funcionalidades_forca.letras_tentadas

print(palavra)
sair = False
while not sair:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            letra = str(pygame.key.name(event.key))
            if letra not in palavra:
                    chances -= 1
                    letras_tentadas.append(letra)
                    print('errou')
                    if chances == 0:
                        pygame.quit()
                        exit()
                         
            else:
                index = 0
                for letraDaPalavra in palavra:
                    if index > len(palavra):
                            index = -1
                    if letraDaPalavra == letra:
                            mascara[index] = letra
                    index +=1
        if mascara.count('_') == 0:
            print('Parabéns! Você ganhou! =D')
            adicionarNoBanco(palavra)
            
            sair = True


    
           
    WINDOW.fill( ( 255, 255, 255 ) )   # fill screen with white background

    # converte a palavra para mostrar
    comoEstaFicando = ''
    for elemento in mascara:
        comoEstaFicando += ' '
        comoEstaFicando += elemento
    show_text(comoEstaFicando, (0,0,0))
    if not sair:
         forca = adicionarMembros()
    else:
         forca = pygame.image.load(os.path.abspath("jogoforca/kp/kelyr/forcak/kely/kforca/parabens.jpg"))
         
    WINDOW.blit(forca, (0, 0))

    

    pygame.display.update()
    clock.tick(60)

    if sair:
         
         time.sleep(2)