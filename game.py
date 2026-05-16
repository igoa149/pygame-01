import pygame

screen = pygame.display.set_mode([1000, 500])

x = 0
y = 0
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == 256:
            break
        if event.type == 768:
            if event.key == 1073741906:
                y -= 1
            if event.key == 1073741904:
                x -= 1
            
            if event.key == 1073741905:
                y += 1
            
            if event.key == 1073741903:
                x += 1
            
    if event.type == 256:
        break  
    
    screen.fill((0, 0, 0))  # 잔상 제거
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.rect(screen, (0, 255, 0), (150, 100, 50, 50))
    pygame.draw.rect(screen, (0, 0, 255), (200, 100, 50, 50))
    
    pygame.draw.rect(screen, (0, 255, 0), (300, 200, 100, 100))
    pygame.display.flip()