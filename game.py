import pygame

screen = pygame.display.set_mode([1000, 500])

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == 256:
            break
    if event.type == 256:
        break  
    
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))
    pygame.draw.rect(screen, (0, 255, 0), (150, 100, 50, 50))
    pygame.draw.rect(screen, (0, 0, 255), (200, 100, 50, 50))
    pygame.display.flip()