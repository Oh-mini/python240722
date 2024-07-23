import pygame
import random

# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 패들 크기
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10

# 공 크기
BALL_SIZE = 10

# 블록 크기
BLOCK_WIDTH = 75
BLOCK_HEIGHT = 20

# FPS 설정
FPS = 60

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 패들 클래스
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
        self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.rect.x = SCREEN_WIDTH - PADDLE_WIDTH

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BALL_SIZE, BALL_SIZE])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.change_x = random.choice([-4, 4])
        self.change_y = -4

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - BALL_SIZE:
            self.change_x *= -1
        if self.rect.y <= 0:
            self.change_y *= -1

# 블록 클래스
class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 스프라이트 그룹
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

# 패들 생성
paddle = Paddle()
all_sprites.add(paddle)

# 공 생성
ball = Ball()
all_sprites.add(ball)

# 블록 생성
for i in range(7):
    for j in range(5):
        block = Block(GREEN, i * (BLOCK_WIDTH + 5) + 35, j * (BLOCK_HEIGHT + 5) + 35)
        all_sprites.add(block)
        blocks.add(block)

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 업데이트
    paddle.update()

    # 공 업데이트
    ball.update()

    # 공과 패들 충돌 검사
    if pygame.sprite.collide_rect(ball, paddle):
        ball.change_y *= -1

    # 공과 블록 충돌 검사
    block_hit_list = pygame.sprite.spritecollide(ball, blocks, True)
    for block in block_hit_list:
        ball.change_y *= -1

    # 공이 바닥에 닿으면 게임 오버
    if ball.rect.y > SCREEN_HEIGHT:
        running = False

    # 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # FPS 설정
    clock.tick(FPS)

pygame.quit()
