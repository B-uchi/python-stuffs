import pygame
import os
pygame.font.init()
pygame.mixer.init()

SIZE = WIDTH, HEIGHT = 900,500
FPS = 60
MAX_BULLETS=30
HEALTH = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'grenade.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'gun_silencer.mp3'))
WIN = pygame.display.set_mode((SIZE))
RED_BULLET = pygame.image.load(os.path.join('Assets', 'bullet.png')) 
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55,40)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (55,40)), -90)
SPACE=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

red_bullets=[]
yellow_bullet=[]


pygame.display.set_caption('First Game')

def drawwindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.fill((255,155,155))
    pygame.draw.rect(WIN, (255,255,255), BORDER)
    
    red_health_text = HEALTH.render(f'Health {red_health}', 1, (255,255,255))
    yellow_health_text = HEALTH.render(f'Health {yellow_health}', 1, (255,255,255))
    WIN.blit(red_health_text, (WIDTH-red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text, (10,10))
    
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255,0,0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255,255,0), bullet)
    
        
    pygame.display.update()

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += 7
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= 7
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def handle_yellow_movement(yellow, keys_pressed):
    if keys_pressed[pygame.K_d] and (yellow.x+yellow.width) - 3 < BORDER.x:
        yellow.x += 3
    if keys_pressed[pygame.K_w] and yellow.y - 3 > 0:
        yellow.y -= 3
    if keys_pressed[pygame.K_s] and yellow.y + 3 < 450:
        yellow.y += 3
    if keys_pressed[pygame.K_a] and yellow.x - 3 > 0:
        yellow.x -= 3
def handle_red_movement(red, keys_pressed):
    if keys_pressed[pygame.K_LEFT] and (red.x+red.width)-3 > BORDER.right+red.width:
        red.x -= 3
    if keys_pressed[pygame.K_UP] and red.y - 3 > 0:
        red.y -= 3
    if keys_pressed[pygame.K_DOWN] and red.y +3 < 450:
        red.y += 3
    if keys_pressed[pygame.K_RIGHT] and red.x+3+red.width < WIDTH:
        red.x += 3
 
def draw_winner(winner_text):
    winner = WINNER_FONT.render(winner_text,1,(25,255,255))
    WIN.blit(winner, (WIDTH/2-winner.get_width()/2, HEIGHT/2-winner.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
    
    
def main():
    red = pygame.Rect(850,250,55,40)
    yellow = pygame.Rect(20,250,55,40)
    red_health = 10
    yellow_health = 10
    
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullet) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x+yellow.width,yellow.height//2+yellow.y,10,5)
                    yellow_bullet.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y+red.height//2,10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_health -=1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -=1
                BULLET_HIT_SOUND.play()
        
        keys_pressed = pygame.key.get_pressed()
        winner_text = ''
        if red_health <=0:
            winner_text = 'Yellow Wins!!'
        if yellow_health <=0:
            winner_text='Red Wins!!'
        if winner_text != '':
            draw_winner(winner_text)
            break
        
        handle_yellow_movement(yellow, keys_pressed)
        handle_red_movement(red, keys_pressed)
        handle_bullets(yellow_bullet, red_bullets, yellow, red)
        drawwindow(red, yellow, red_bullets, yellow_bullet, red_health, yellow_health)
    
    
    main()

if __name__ == '__main__':
    main()
