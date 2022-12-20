import pygame
import random

# Inicjalizacja biblioteki pygame
pygame.init()

# Ustawienie wielkości okna
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Ustawienie tła okna na kolor ciemnoszary
screen.fill((60, 60, 60))

# Ustawienie tytułu okna
pygame.display.set_caption('Kółka')

# Ustawienie promienia kółek na daną wielkość pikseli
radius = 10


# Klasa reprezentująca kółka
class Circle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.dx = 1  # Prędkość w poziomie
        self.dy = 1  # Prędkość w pionie

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Odbicie od ścianek
        if self.x + radius > screen_width or self.x - radius < 0:
            self.dx *= -1
        if self.y + radius > screen_height or self.y - radius < 0:
            self.dy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)


# Losowe położenie kółek na starcie
circle1 = Circle(random.randint(radius, screen_width - radius), random.randint(radius, screen_height - radius),
                 (255, 0, 0))
circle2 = Circle(random.randint(radius, screen_width - radius), random.randint(radius, screen_height - radius),
                 (0, 255, 0))

# Główna pętla programu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ruch kółek
    circle1.move()
    circle2.move()

    # Wyświetlenie kółek na ekranie
    screen.fill((60, 60, 60))
    circle1.draw()
    circle2.draw()
    pygame.display.flip()

# Zakończenie biblioteki pygame
pygame.quit()
