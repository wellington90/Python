import pygame
import sys

pygame.init()

# Configuração da janela
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Definir as constantes
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60
BALL_RADIUS = 10
PADDLE_SPEED = 5
BALL_SPEED = 5

# Definir as variáveis
player_score = 0
ai_score = 0

# Classe para a bola
class Ball:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = [1, 1]

    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def bounce(self):
        if self.y > height - BALL_RADIUS or self.y < BALL_RADIUS:
            self.direction[1] = -self.direction[1]

    def reset(self):
        self.x = width/2
        self.y = height/2
        self.direction = [1, 1]

# Classe para o jogador
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y -= PADDLE_SPEED

    def move_down(self):
        self.y += PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Desenhar os objetos na tela
def draw():
    # Desenhar a tela
    screen.fill((0, 0, 0))

    # Desenhar a bola
    pygame.draw.circle(screen, (255, 255, 255), (ball.x, ball.y), BALL_RADIUS)

    # Desenhar os jogadores
    player_paddle.draw()
    ai_paddle.draw()

    # Desenhar a pontuação
    font = pygame.font.Font(None, 36)
    player_text = font.render("Player: " + str(player_score), 1, (255, 255, 255))
    ai_text = font.render("AI: " + str(ai_score), 1, (255, 255, 255))
    screen.blit(player_text, (10, 10))
    screen.blit(ai_text, (width - ai_text.get_width() - 10, 10))

    # Atualizar a tela
    pygame.display.update()

# Lógica do jogo
def game_loop():
    global player_score, ai_score

    ball.reset()

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimentação do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_paddle.move_up()
        if keys[pygame.K_DOWN]:
            player_paddle.move_down()

        # Movimentação da bola
        ball.move()
        ball.bounce()

        # Verificar colisão com as raquetes
        if ball.x <= player_paddle.x + PADDLE_WIDTH and ball.y >= player_paddle.y and ball.y <= player_paddle.y + PADDLE_HEIGHT:
            ball.direction[0] = 1
        elif ball.x >= ai_paddle.x - BALL_RADIUS and ball.y >= ai_paddle.y and ball.y <= ai_paddle.y + PADDLE_HEIGHT:
            ball.direction[0] = -1
        elif ball.x < 0:
            ai_score += 1
            ball.reset()
        elif ball.x > width:
            player_score += 1
            ball.reset()

        # Movimentação do adversário
        if ball.direction[0] == 1:
            if ai_paddle.y + PADDLE_HEIGHT/2 < ball.y:
                ai_paddle.move_down()
            elif ai_paddle.y + PADDLE_HEIGHT/2 > ball.y:
                ai_paddle.move_up()

        # Desenhar os objetos na tela
        draw()

        # Delay para controlar a velocidade do jogo
        pygame.time.delay(10)

# Inicialização do jogo
player_paddle = Paddle(50, height/2 - PADDLE_HEIGHT/2)
ai_paddle = Paddle(width - 50 - PADDLE_WIDTH, height/2 - PADDLE_HEIGHT/2)
ball = Ball(width/2, height/2, BALL_SPEED)

game_loop()
