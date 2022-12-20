import sys

import pygame
import random

# Inicjalizacja pygame
pygame.init()

# Ustawienie wielkości okna
window_size = (1200, 800)

# Ustawienie tła
background_color = (50, 50, 50)

# Ustawienie kolorów kółek
circle_colors = [(255, 0, 0), (0, 255, 0)]

# Ustawienie ilości kulek czerwonych i zielonych
num_red_circles = 15
num_green_circles = 15

# Ustawienie szybkości poruszania się kulek
circle_speed = 10

# Utworzenie okna
screen = pygame.display.set_mode(window_size)

# Utworzenie zegara, który będzie używany do opóźniania wyświetlania klatek
clock = pygame.time.Clock()

# Utworzenie pustej listy, w której będą przechowywane kółka
circles = []

# Utworzenie kółek czerwonych
for i in range(num_red_circles):
  # Losowanie położenia początkowego kółka
  x = random.randint(0, window_size[0])
  y = random.randint(0, window_size[1])
  # Utworzenie kółka z odpowiednimi parametrami
  circle = {"color": circle_colors[0], "radius": 25, "position": (x, y), "direction": (circle_speed, circle_speed)}
  # Dodanie kółka do listy
  circles.append(circle)

# Utworzenie kółek zielonych
for i in range(num_green_circles):
  # Losowanie położenia początkowego kółka
  x = random.randint(0, window_size[0])
  y = random.randint(0, window_size[1])
  # Utworzenie kółka z odpowiednimi parametrami
  circle = {"color": circle_colors[1], "radius": 25, "position": (x, y), "direction": (circle_speed, circle_speed)}
  # Dodanie kółka do listy
  circles.append(circle)

# Główna pętla programu
while True:
  # Ustawienie ilości klatek na sekundę
  clock.tick(60)

  # Pętla zdarzeń
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Aktualizacja położenia kółek
  for circle in circles:
    # Pobranie aktualnego położenia kółka
    x, y = circle["position"]
    # Pobranie kierunku ruchu kółka
    dx, dy = circle["direction"]
    # Aktualizacja położenia kółka
    x += dx
    y += dy
    # Sprawdzenie, czy kółko nie wyszło poza granice okna
    if x < 0 or x > window_size[0]:
      dx = -dx
    if y < 0 or y > window_size[1]:
      dy = -dy
    # Uaktualnienie kierunku ruchu kółka
    circle["direction"] = (dx, dy)
    # Uaktualnienie położenia kółka
    circle["position"] = (x, y)

  # Wyświetlenie tła
  screen.fill(background_color)

  # Wyświetlenie kółek
  for circle in circles:
    # Pobranie koloru i położenia kółka
    color = circle["color"]
    x, y = circle["position"]
    radius = circle["radius"]
    # Utworzenie obiektu reprezentującego kółko
    pygame.draw.circle(screen, color, (x, y), radius)

  # Wyświetlenie zmian na ekranie
  pygame.display.flip()
