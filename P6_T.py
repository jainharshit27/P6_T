import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

bulb_state = "on"

clock = pygame.image.load("bulb.png")
clock = pygame.transform.scale(clock, (64, 90)).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        # Add game_state condition
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # change value of game_state
        # Add game_state condition
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # change value of game_state
                    
    # Use the following lines in conditionals one for if and one for else block
    screen.blit(clock, (50,50))
    screen.fill((0,0,0))   

    pygame.display.update()