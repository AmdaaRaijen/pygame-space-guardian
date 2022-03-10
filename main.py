import pygame
import random
from sys import exit

pygame.init()

WIDHT, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDHT, HEIGHT))
PLAYER_ACC = 5

bg = pygame.image.load('Assets/space1.png').convert()
lawan = pygame.transform.rotate((pygame.image.load('Assets/spaceship_red(resized).png').convert_alpha()), -90)
pemain = pygame.transform.rotate((pygame.image.load('Assets/spaceship_yellow(resized).png').convert_alpha()), -90)

FONT = pygame.font.SysFont('Assets/Cyberpunks Italic.ttf', 40)

def Window(bullets, score_counter):
    WIN.blit(bg, (0, 0))
    score = FONT.render('Score : ' + str(score_counter), 1, 'white')
    WIN.blit(score, (370, 20))
    WIN.blit(pemain, player_rect)
    for bullet in bullets:
        pygame.draw.rect(WIN, 'white', bullet)
    

    
    # WIN.blit(lawan, musuh_rect)
    # WIN.blit(text, text_rect)

    # for bullet in bullets:
    #     WIN.draw.rect(WIN, 'white', bullet)

    # pygame.display.update()

def player_move():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_rect.y -= PLAYER_ACC
    
    if keys[pygame.K_s]:
        player_rect.y += PLAYER_ACC

    if keys[pygame.K_a]:
        player_rect.x -= PLAYER_ACC

    if keys[pygame.K_d]:
        player_rect.x += PLAYER_ACC

Musuh_list = []

def Musuh_spawn(musuh_list, bullets):
    if Musuh_list:
        for musuh_rect in musuh_list:
            for bullet in bullets:
                if musuh_rect.colliderect(bullet):
                    print('hit')
                    Player_bullet.remove(bullet)
                    musuh_list.remove(musuh_rect)
                    pygame.event.post(pygame.event.Event(HIT))

            musuh_rect.x -= 5
            WIN.blit(lawan, musuh_rect)

        musuh_list = [musuh for musuh in musuh_list if musuh.x > -100]

        return musuh_list

    else: return []

Player_bullet = []

def Bullet_move(bullets):
    for bullet in bullets:
        # pygame.draw.rect(WIN, 'white', bullet)
        bullet.x += 10
        if musuh_rect.colliderect(bullet):
            print('hit')
            # pygame.event.post(pygame.event.Event(RED_HIT))
            Player_bullet.remove(bullet)
        
        if bullet.x > 900:
            Player_bullet.remove(bullet) 

player_rect = pemain.get_rect(center = (100, 250))
musuh_rect = lawan.get_rect(center = (900, (random.randrange(50, 450))))

musuh_timer = pygame.USEREVENT + 1
pygame.time.set_timer(musuh_timer, 1000)

HIT = pygame.USEREVENT + 2

def main():
    score_counter = 0   

    CLOCK = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == musuh_timer:
                Musuh_list.append(lawan.get_rect(center = (900, (random.randrange(50, 450)))))
                print(Musuh_list)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(Player_bullet) < 4:
                    bullet = pygame.Rect(player_rect.midright[0], player_rect.midright[1], 10, 4)
                    Player_bullet.append(bullet)
                    print(player_rect.midright)
            if event.type == HIT:
                score_counter += 1

        # WIN.blit(bg, (0, 0))
        Bullet_move(Player_bullet)
        Window(Player_bullet, score_counter)
        player_move()
        Musuh_spawn(Musuh_list, Player_bullet)
        pygame.display.update()
        CLOCK.tick(60)

    main()

if __name__ == "__main__":
    main()
