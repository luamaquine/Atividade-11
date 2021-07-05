import sys

import pygame

WIDTH, HEIGHT = 400, 400
TITLE = "Mario Animation"
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

idle_left = pygame.image.load('./assets/mario-walk-left-4.png')
idle_right = pygame.image.load('./assets/mario-walk-right-4.png')

walk_left = [pygame.image.load('./assets/mario-walk-left-4.png'),
             pygame.image.load('./assets/mario-walk-left-3.png'),
             pygame.image.load('./assets/mario-walk-left-2.png'),
             pygame.image.load('./assets/mario-walk-left-1.png')]

walk_right = [pygame.image.load('./assets/mario-walk-right-4.png'),
              pygame.image.load('./assets/mario-walk-right-3.png'),
              pygame.image.load('./assets/mario-walk-right-2.png'),
              pygame.image.load('./assets/mario-walk-right-1.png')]

jump_left = pygame.image.load('./assets/mario-jump-left.png')

jump_right = pygame.image.load('./assets/mario-jump-right.png')

x = 250
y = 250
velocity_x = 10
velocity_y = 10
move_left = False
move_right = False
stepIndex = 0
jump = False


def draw_game():
    global stepIndex
    screen.fill((0, 0, 0))
    if stepIndex >= 3:
        stepIndex = 0
    if move_left:
        screen.blit(walk_left[stepIndex], (x, y))
        stepIndex += 1
    elif move_right:
        screen.blit(walk_right[stepIndex], (x, y))
        stepIndex += 1
    elif jump:
        screen.blit(jump_left, (x, y))
    else:
        if not move_left:
            screen.blit(idle_left, (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_game()

    key_pressed = pygame.key.get_pressed()

    # Movement

    if key_pressed[pygame.K_a]:
        x -= velocity_x
        move_left = True
        move_right = False
        is_walking_left = True
    elif key_pressed[pygame.K_d]:
        x += velocity_x
        move_left = False
        move_right = True
    elif jump is False and key_pressed[pygame.K_SPACE]:
        jump = True
    elif jump is True:
        y -= velocity_y
        velocity_y -= 1
        if velocity_y < -10:
            jump = False
            velocity_y = 10
    else:
        move_left = False
        move_right = False
        jump = False
        stepIndex = 0

    pygame.display.flip()
    clock.tick(30)
