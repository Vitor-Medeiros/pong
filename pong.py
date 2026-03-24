import pygame
import sys

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.SysFont(None, 60)
        self.font_text = pygame.font.SysFont(None, 30)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return

            self.screen.fill(BLACK)

            title = self.font_title.render("PONG", True, WHITE)
            self.screen.blit(title, (WIDTH // 2 - 80, HEIGHT // 3))
 
            if pygame.time.get_ticks() % 1000 < 500:
                text = self.font_text.render(
                    "Pressione ESPAÇO para jogar", True, WHITE
                )
                self.screen.blit(text, (WIDTH // 2 - 140, HEIGHT // 2))

            pygame.display.flip()

class raquete:

    def __init__(self, x, y, width=10, height=60, speed=5):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, direction):
    
        self.rect.y += direction * self.speed
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)


class Bola:

    def __init__(self, size=7, speed=5):
        self.size = size
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, size, size)
        self.speed_x = speed
        self.speed_y = speed

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce_y(self):
        self.speed_y *= -1

    def bounce_x(self):
        self.speed_x *= -1

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.bounce_x()

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.rect.center, self.size)

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong Refatorado")
        self.clock = pygame.time.Clock()

        self.player = raquete(15, HEIGHT // 2 - 30)
        self.enemy = raquete(WIDTH - 25, HEIGHT // 2 - 30)
        self.ball = Bola()

        self.score_player = 0
        self.score_enemy = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move(-1)
        if keys[pygame.K_DOWN]:
            self.player.move(1)

    def player_2(self):
       
        if self.enemy.rect.centery < self.ball.rect.centery:
            self.enemy.move(1)
        else:
            self.enemy.move(-1)

    def colisao(self):
        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= HEIGHT:
            self.ball.bounce_y()

        if self.ball.rect.colliderect(self.player.rect) or \
           self.ball.rect.colliderect(self.enemy.rect):
            self.ball.bounce_x()

    def pontuacao(self):
        if self.ball.rect.left <= 0:
            self.score_enemy += 1
            self.ball.reset()

        if self.ball.rect.right >= WIDTH:
            self.score_player += 1
            self.ball.reset()

    def draw(self):
        self.screen.fill(BLACK)

        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.ball.draw(self.screen)

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(
            f"{self.score_player} - {self.score_enemy}", True, WHITE
        )
        self.screen.blit(score_text, (WIDTH // 2 - 30, 20))

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.handle_input()
            self.player_2()
            self.ball.move()
            self.colisao()
            self.pontuacao()
            self.draw()

            self.clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    menu = Menu(screen)
    menu.run() 

    game = Game()
    game.run()