import pygame 
from pygame.constants import KEYDOWN
from pygame.locals import *
import random
from Snake import Snake
from Vector2 import vector

pygame.init()
clock = pygame.time.Clock()

# Taille de l'écran
ecran_x = 1080
ecran_y = 660
ecran = pygame.display.set_mode((ecran_x, ecran_y))
pygame.display.set_caption("Space Invader 3000")

# Couleurs
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Taille et police du message
font_result = pygame.font.SysFont("comicsansms", 40)
font_score = pygame.font.SysFont(None, 30)

# Résultat du jeu : game over or winner
def result(msg, color):
    msg = font_result.render(msg, True, color)
    ecran.blit(msg, [ecran_x / 8, ecran_y / 3])

# Score de la partie
def score(number):
    msg_score = font_score.render("Score : " + str(number), True, blue)
    ecran.blit(msg_score, [20, 20])

# Jeu snake
def loopGame():
    # Gérer le jeu
    game_over = False
    game_close = False

    # Caractéristique du serpent
    snake_block = 20
    snake_score = 0
    snake_speed = 15
    snake = Snake()

    # Position aléatoire de la pomme
    apple_x = round(random.randrange(0, ecran_x - snake_block) / 20.0) * 20.0
    apple_y = round(random.randrange(0, ecran_y - snake_block) / 20.0) * 20.0

    while not game_over:
        ecran.fill((0,0,0))

        # Si le joueur à perdu
        while game_close == True:
            # On affiche le message et le score
            result("You Lost ! Press P for play again or Q for quit", red)
            score(snake_score)
            pygame.display.update()

            # On ferme la fenetre
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        loopGame()

        # Si le joueur n'a pas perdu on l'autorise à jouer
        for event in pygame.event.get():
            if game_over == False :
                # Lorsqu'on appuie sur un bouton
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        snake.dir = "up"
                    if event.key == pygame.K_q:
                        snake.dir = "left" 
                    if event.key == pygame.K_s:
                        snake.dir = "down"
                    if event.key == pygame.K_d:
                        snake.dir = "right"

            if event.type == pygame.QUIT:
                game_over = True
                game_close = False

        # Si le serpent rentre en collision avec son propre corps
        if len(snake.bodyRect) > 1:
            for x in snake.bodyRect:
                if snake_rect.colliderect(x):
                    game_close = True

        # Si le serpent sors de la zone de jeu
        if snake.x >= ecran_x or snake.y >= ecran_y or snake.x < 0 or snake.y < 0:
            game_close = True

        # Propriété de la pomme et du serpent
        pygame.draw.rect(ecran, red, [apple_x, apple_y, snake_block, snake_block])
        apple_rect = Rect(apple_x, apple_y, snake_block, snake_block)
        snake_rect = Rect(snake.x, snake.y, snake_block, snake_block)

        # Gère le serpent
        snake.Update()
        score(snake_score)
        snake.Draw(ecran, green, snake_block, snake_score)
        pygame.display.flip()

        # Si le serpent rentre en collision avec la pomme
        if snake_rect.colliderect(apple_rect) :
            snake_score += 1
            # Change la position de la pomme
            apple_x = round(random.randrange(0, ecran_x - snake_block) / 20.0) * 20.0
            apple_y = round(random.randrange(0, ecran_y - snake_block) / 20.0) * 20.0    

        #Gestion de la vitesse du serpent
        clock.tick(snake_speed)

    pygame.quit()
    quit()

loopGame()