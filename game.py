import pygame

screen = pygame.display.set_mode([1000, 500])

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == 256:
            break
    if event.type == 256:
        break   