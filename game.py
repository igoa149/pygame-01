import pygame

pygame.font.init()
font = pygame.font.SysFont("gulim", 20)
screen = pygame.display.set_mode([1000, 500])

x = 0
y = 0
n = 0


r = 255
g = 255
b = 255
click = 0
is_right_key_down = False
is_left_key_down = False
is_up_key_down = False
is_down_key_down = False
is_clicked = False
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
        
        if event.type == 1025:
            print(f"is_clicked: {is_clicked}")
            click += 1
            if click % 2 == 0:
                is_clicked = True
            else:
                is_clicked = False

       
        

            
    if event.type == 256:
        break  
    
    if is_right_key_down == True:
        x += 0.1
    if is_left_key_down == True:
        x -= 0.1
    if is_up_key_down == True:
        y -= 0.1
    if is_down_key_down == True:
        y += 0.1




    screen.fill((0, 0, 0))  # 잔상 제거
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))


    if is_clicked == False:
        pygame.draw.rect(screen, (0, 255, 0), (150, 100, 50, 50))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (150, 100, 50, 50))

    pygame.draw.rect(screen, (0, 0, 255), (200, 100, 50, 50))
    
    pygame.draw.rect(screen, (0, 255, 0), (300, 200, 100, 100), 5)
    
    pygame.draw.rect(screen, (0, 255, 0), (300, 180, 100, 10), 2)


    pygame.draw.rect(screen, (0, 255, 0), (500, 0, 10, 500), 5)
    if 450 <= x:
        x = 450
        pygame.draw.rect(screen,(0, 255, 0),(500 ,0 ,500, 500))


    if 300 < x < 350 and 200 < y < 250:#x, y 가 내부에 있는가?:
        n += 0.5
        pygame.draw.rect(screen, (0, 255, 0), (300, 200, 100, 100))
        pygame.draw.rect(screen, (0, 255, 0), (300, 180, n, 10), 5)
        if n >= 100:
            n = 100

    text = "클릭 횟수"
    text_render = font.render(text, True, (255, 255, 255))
    screen.blit(text_render, (50, 50))

    text = f"{click}"
    text_render = font.render(text, True, (255, 255, 255))
    screen.blit(text_render, (50, 50 + 40))

    pygame.display.flip()
