import pygame

# initializing pygame
pygame.init()

display_size = (1280, 720)

# setting display size
screen = pygame.display.set_mode(display_size)

# initializing clock module
clock = pygame.time.Clock()

# setting initial state of game to start the main game loop
running = True

# initialize the change in time for the physics in game
dt = 0

# ball radius
radius = 40

# jump action default state
jump = 0

# default position of the circle
player_pos = pygame.Vector2(radius+5, screen.get_height()-radius-5)

while running:
    
    # checking if the game is running or quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # filling screen with purple color
    screen.fill("purple")

    
    # drawing a circle at center of screem
    pygame.draw.circle(screen, "red", player_pos, radius)

    # handling key events and binding them to specific actions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos.y > (radius + 5):
            player_pos.y -= 300 * dt 
    if keys[pygame.K_s]:
        if player_pos.y < (display_size[1]-radius-5):
            player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        if player_pos.x > (radius + 5):
            player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        if player_pos.x < (display_size[0]-radius-5):
            player_pos.x += 300 * dt
    if keys[pygame.K_SPACE]:
        jump = 1

    # showing everything that we have done above on display
    pygame.display.flip()

    # converting from ms to s
    # for every 1s at most 60 frames should pass
    # returns number of ms passed since its last call
    dt = clock.tick(60) / 1000

# quit game once user closes the window
pygame.quit()