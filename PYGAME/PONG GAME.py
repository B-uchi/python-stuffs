import random
import pygame
pygame.init()

score_font = pygame.font.SysFont('comicsans', 30)
SCREEN = WIDTH, HEIGHT = 700,500
FPS = 60
BALL_RADIUS = 7
PADDLE_HEIGHT,PADDLE_WIDTH = 100,10

clock = pygame.time.Clock()
WIN = pygame.display.set_mode(SCREEN)
pygame.display.set_caption('Pong')

class paddle(object):
    VEL = 0.6
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (255,255,255), (self.x, self.y, self.width, self.height), 0, 5)
        
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius <= HEIGHT:
        ball.y_vel *= -1
    if ball.y - ball.radius >=4:
        ball.y_vel *= -1
        
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1
                
                middle_y= left_paddle.y + left_paddle.height // 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height/2) / ball.MAX_VEL
                y_vel = difference_in_y/reduction_factor
                ball.y_vel = -1 * y_vel
                
    if ball.x > 0:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
                
                middle_y= right_paddle.y + right_paddle.height // 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height/2) / ball.MAX_VEL
                y_vel = difference_in_y/reduction_factor
                ball.y_vel = -1 * y_vel

class Ball(object):
    MAX_VEL = 0.3
    def __init__(self, x, y, radius):
        self.x = self.original_x= x
        self.y =self.original_y= y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
    
    def draw(self, win):
        pygame.draw.circle(win, (255,255,255), (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        pygame.time.delay(500)
        self.x_vel *= -1
        bb=random.random() - 0.4  
        self.y_vel = bb
        print(bb)

left_paddle = paddle(10, HEIGHT//2-PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = paddle(670, HEIGHT//2-PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

def draw_window(win, paddles, ball, left_score, right_score):
    win.fill((0,0,0))
    left_text = score_font.render(f'{left_score}', 1, (255,255,255))
    right_text = score_font.render(f'{right_score}', 1, (255,255,255))
    win.blit(left_text, (WIDTH//2 - 80, 20-left_text.get_height()//2))
    win.blit(right_text, (WIDTH//2 + 60, 20-right_text.get_height()//2))
    for paddle in paddles:
        paddle.draw(win)
    
    for i in range(10,HEIGHT, HEIGHT//20):
        if i%2==1:
            continue
        pygame.draw.rect(win, (255,255,255), (WIDTH//2 - 5, i, 10, HEIGHT//20))
    
    ball.draw(win)
    ball.move()
    handle_collision(ball, left_paddle, right_paddle)
    pygame.display.update()

def handle_movement(keys_pressed, left_paddle, right_paddle):
    if keys_pressed[pygame.K_w] and left_paddle.y-left_paddle.VEL >0:
        left_paddle.move(True)
    if keys_pressed[pygame.K_s] and left_paddle.y+left_paddle.VEL+left_paddle.height <HEIGHT:
        left_paddle.move(False)
    if keys_pressed[pygame.K_UP] and right_paddle.y-right_paddle.VEL >0:
        right_paddle.move(True)
    if keys_pressed[pygame.K_DOWN] and right_paddle.y+right_paddle.VEL+right_paddle.height <HEIGHT:
        right_paddle.move(False)

def main():
    run = True
    clock.tick(FPS)
    left_score = 0
    right_score = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if ball.x < 0:
            right_score+=1
            ball.reset()
        elif ball.x > WIDTH:
            left_score+=1
            ball.reset()
            
        keys_pressed = pygame.key.get_pressed()
        draw_window(WIN, [left_paddle, right_paddle], ball, left_score, right_score)
        handle_movement(keys_pressed, left_paddle, right_paddle)
    pygame.quit()
    
if __name__ == '__main__':
    main()