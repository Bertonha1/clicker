import pygame
import time

pygame.init()

screen_width = 800
screen_height = 600
# desenha a tela
screen = pygame.display.set_mode((screen_width, screen_height))
# cria um objeto retangulo
player = pygame.Rect(100, 250, 150, 150)
# cria o primeiro item
item1 = pygame.Rect((450, 150), (350, 50))
# cria o segundo item
item2 = pygame.Rect((450, 300), (350, 50))
# buffa clicques
buffa_cliques = pygame.Rect((450, 450), (350, 50))
run = True

cliques = 0

text_font = pygame.font.SysFont("Calibri", 30)

cliques_para_reaparecer = None

cliques_buffados = 0

cliques_passivos = 0

# Armazena o tempo da última atualização dos cliques passivos
last_update_time = time.time()

gasto = 0

nivel_item1 = 0

nivel_item2 = 0

nivel_upgrade = 0

preço_item1 = 15 * 1.15 ** nivel_item1

preço_item2 = 100 * 1.15 ** nivel_item2

preço_upgrade = 200 * 1.15 ** nivel_upgrade


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


while run:
    # atualiza a tela
    screen.fill((0, 0, 0))
    # cria o retangulo com a cor vermelha
    pygame.draw.rect(screen, (255, 0, 0), player)
    # Desenha o texto do total de cliques
    draw_text(f'Cliques no retângulo: {cliques:.1f}',
              text_font, (255, 255, 255), 250, 10)

    # Desenha o texto do total de cliques por segundo
    draw_text(f'Cliques passivos: {cliques_passivos:.1f}',
              text_font, (255, 255, 255), 250, 50)

    # desenha o item 1
    pygame.draw.rect(screen, (0, 0, 255), item1)
    # texto item 1
    draw_text(f'Upgrade 1: {preço_item1:.2f} cliques',
              text_font, (255, 255, 255), 455, 150)

    # desenha o item 2
    pygame.draw.rect(screen, (141, 100, 202), item2)
    # texto item 2
    draw_text(f'Upgrade 2: {preço_item2:.2f} cliques',
              text_font, (255, 255, 255), 455, 300)

    # desenha o buff de cliques
    pygame.draw.rect(screen, (185, 101, 202), buffa_cliques)
    # texto item 2
    draw_text(f'Aumenta os cliques: {preço_upgrade:.2f} cliques',
              text_font, (255, 255, 255), 455, 450)
    # Atualiza os cookies passivos
    current_time = time.time()
    if current_time - last_update_time >= 1:  # Verifica se passou 1 segundo
        cliques += cliques_passivos
        last_update_time = current_time
    # captura os eventos
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player.collidepoint(event.pos):
                cliques += 1 + cliques_buffados
            if item1.collidepoint(event.pos) and cliques >= preço_item1:
                cliques_passivos += 0.2 * nivel_item1
                cliques = cliques - preço_item1
                nivel_item1 += 1
                preço_item1 = 15 * 1.15 ** nivel_item1
                # Calcula a nova quantidade de cliques necessária para reaparecer o retângulo azul
            if item2.collidepoint(event.pos) and cliques >= preço_item2:
                cliques_passivos += 2 * nivel_item2
                cliques = cliques - preço_item2
                nivel_item2 += 1
                preço_item2 = 100 * 1.15 ** nivel_item2
            if buffa_cliques.collidepoint(event.pos) and cliques >= preço_upgrade:
                cliques_passivos += 3
                cliques_buffados += 5
                cliques = cliques - preço_upgrade
                nivel_upgrade += 1
                preço_upgrade = 200 * 1.15 ** nivel_upgrade

        if event.type == pygame.QUIT:
            run = False
    # atualiza o display
    pygame.display.update()

pygame.quit()
