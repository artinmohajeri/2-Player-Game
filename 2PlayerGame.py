import pygame
import os
pygame.init()
# pygame.font.init()
# pygame.mixer.init()
win = pygame.display.set_mode((1380,800))
pygame.display.set_caption('2 player space war')
pygame.display.set_icon(pygame.image.load('stuff/2picon.png'))
chosi = pygame.font.SysFont('comicsans', 15)
chosit = chosi.render('developed by ARTIN mj', 1, (255,255,255))
war_spaceShip = pygame.image.load('stuff/PicsArt_02-02-02.29.06.png')
war_spaceShip2 = pygame.image.load('stuff/580b585b2edbce24c47b2d2a.png')
war_spaceShip = pygame.transform.scale(war_spaceShip,(100,100))
war_spaceShip2 = pygame.transform.rotate(pygame.transform.scale(war_spaceShip2,(80,100)),320) 
black_hit = pygame.USEREVENT + 1
white_hit = pygame.USEREVENT + 2
border = pygame.Rect(1380/2-9,0,4,800)
bullet_fire_sound = pygame.mixer.Sound('stuff/صدا ۰۰۲ (mp3cut.net).mp3')
# space = pygame.transform.scale(pygame.image.load(os.path.join('stuff/wall.jpg')), (1380,800))
space = pygame.transform.scale(pygame.image.load('stuff/backgroundspace.jpg'),(1380, 800))
health_font = pygame.font.SysFont('comicsans',30)
winner_font = pygame.font.SysFont('comicsans',100)
winvel = 1
i,j = 0,0
def style(black,white,black_bullets, white_bullets,black_health,white_health):
    global i, j, winvel
    win.blit(space,(i,j)); win.blit(space,(i+1380,j)); win.blit(space,(i-1380,j)); win.blit(space,(i,j+800)); win.blit(space,(i,j-800)); win.blit(space,(i+1380,j+800)); win.blit(space,(i-1380,j-800))
    # i += winvel
    # if i >= 60:
    #     j+= winvel
    #     winvel = -1
    # if i <= 0:
    #     winvel = 1
    # j += winvel
    # if j >= 60:
    #     winvel = -1
    # if j <= 0:
    #     winvel = 1

    # win.fill((255,10,10))
    win.blit(war_spaceShip,(black.x,black.y))
    win.blit(war_spaceShip2,(white.x,white.y))
    pygame.draw.rect(win,(10,10,10),border)
    black_health_text = health_font.render('Health: '+ str(black_health),1,(255,255,255))
    white_health_text = health_font.render('Health: '+ str(white_health),1,(255,255,255))
    
    win.blit(black_health_text,(20,10))
    win.blit(white_health_text,(1217,10))
    for bullet in black_bullets:
        pygame.draw.rect(win, (255,255,0),bullet)
    for bullet in white_bullets:
        pygame.draw.rect(win, (0,255,0),bullet)
    win.blit(chosit, (20,51))
    pygame.display.update()
def white_move(keys_pressed,white):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_DOWN] and white.y + 3< 690:  
            white.y += 5
        if keys_pressed[pygame.K_UP] and white.y -3>-14:  
            white.y -= 5
        if keys_pressed[pygame.K_LEFT] and white.x - 3 > border.x-3:  
            white.x -= 5
        if keys_pressed[pygame.K_RIGHT] and white.x + 3<1265:  
            white.x += 5
def black_move(keys_pressed,black):
        if keys_pressed[pygame.K_2]and black.y + 3<690:  
            black.y += 5
        if keys_pressed[pygame.K_F2]and black.y - 3>0:  
            black.y -= 5
        if keys_pressed[pygame.K_1]and black.x - 3>0:  
            black.x -= 5
        if keys_pressed[pygame.K_3]and black.x + 3<border.x-100:  
            black.x += 5
def draw_winner(text):
    draw_text = winner_font.render(text,1,(255,255,255))
    win.blit(draw_text ,(1380//2-270,300))
    pygame.display.update()
    pygame.time.delay(5000)
def handel_bullets(black_bullets, white_bullets, black, white):
    for bullet in  black_bullets:
        bullet.x += 20
        if white.colliderect(bullet): 
            pygame.event.post(pygame.event.Event(white_hit))
            black_bullets.remove(bullet)
        elif bullet.x > 1380:
            black_bullets.remove(bullet)
    for bullet in white_bullets:
        bullet.x -= 20
        if black.colliderect(bullet):
            pygame.event.post(pygame.event.Event(black_hit))
            white_bullets.remove(bullet)
        elif bullet.x<6:
            white_bullets.remove(bullet)
def main():
    black = pygame.Rect(30 ,330,50,100)
    white = pygame.Rect(1260,330,20,100)
    clock = pygame.time.Clock()
    white_bullets = []
    black_bullets = []
    run = True
    black_health = 10
    white_health = 10
    while run:
        clock.tick(70)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL and len(white_bullets) < 3:
                    bullet = pygame.Rect((white.x-30+ white.width, white.y+63, 10, 4))
                    white_bullets.append(bullet)
                    bullet_fire_sound.play()
                if len(white_bullets) > 3:
                    # pygame.time.delay(7000)
                    white_bullets = []

                if event.key == pygame.K_BACKQUOTE and len(black_bullets) < 3:
                    bullet = pygame.Rect((black.x+80, black.y+47, 10, 4))
                    black_bullets.append(bullet)
                    bullet_fire_sound.play()
                if len(black_bullets) > 3:
                    # pygame.time.delay(7000) 
                    black_bullets = []
            if event.type==black_hit:
                black_health -= 1

            if event.type==white_hit:
                white_health -= 1
        
        winnerText = ''
        if black_health==0:
            winnerText = 'White Wins!'
        if white_health==0:
            winnerText = 'Black Wins!'
        if winnerText != '':
            draw_winner(winnerText)
            break

        style(black,white,black_bullets,white_bullets,black_health,white_health)
        keys_pressed = pygame.key.get_pressed()
        white_move(keys_pressed,white)
        black_move(keys_pressed,black)
        handel_bullets(black_bullets, white_bullets, black, white)

    main()

if __name__ == '__main__':
    main()