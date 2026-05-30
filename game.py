import pygame

screen = pygame.display.set_mode([1000, 500])

x = 0
y = 0

is_right_key_down = False
is_left_key_down = False
is_up_key_down = False
is_down_key_down = False
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == 256:
            break
        if event.type == 768:  # keydown
            if event.key == 1073741906:
                #y -= 10
                is_up_key_down = True
            if event.key == 1073741904:
                #x -= 10
                is_left_key_down = True
            if event.key == 1073741905:
                #y += 10
                is_down_key_down = True
            
            if event.key == 1073741903:
                # x += 10
                is_right_key_down = True

        if event.type == 769: # keyup
            if event.key == 1073741903:
                is_right_key_down = False

            if event.key == 1073741904:
                is_left_key_down = False

            if event.key == 1073741905:
                is_down_key_down = False

            if event.key == 1073741906:
                is_up_key_down = False

            
    if event.type == 256:
        break  
    
    if is_right_key_down == True:
        x += 1
    if is_left_key_down == True:
        x -= 1
    if is_up_key_down == True:
        y -= 1
    if is_down_key_down == True:
        y += 1

    screen.fill((0, 0, 0))  # 잔상 제거
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.rect(screen, (0, 255, 0), (150, 100, 50, 50))
    pygame.draw.rect(screen, (0, 0, 255), (200, 100, 50, 50))
    
    pygame.draw.rect(screen, (0, 255, 0), (300, 200, 100, 100), 5)
    if 300 < x < 350 and 200 < y < 250:#x, y 가 내부에 있는가?:
        pygame.draw.rect(screen, (0, 255, 0), (300, 200, 100, 100))
    pygame.display.flip()
