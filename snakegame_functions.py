import pygame, random #necessary imports
pygame.init() #initialising pygame

width = 400 #constants for game
height = 400
clock = pygame.time.Clock()
snake_pixel_size = 10
snake_speed = 10

window = pygame.display.set_mode((width,height)) #setting window length and caption up
pygame.display.set_caption('Snake game')

def create_snake(ss, sp):
    for i in sp:
        pygame.draw.rect(window, (102, 205, 0), [i[0], i[1], ss, ss]) #draws snake as rectangle green colour then size

def run():
    game_over = False

    x_coor = width / 2 #centre coordinates so snake spawns in middle
    y_coor = height / 2

    x_speed = 0  #initial speed = 0 until button pressed
    y_speed = 0

    snake_blocks = [] #list for when snake eats food blocks += 1
    snake_len = 1 #initial length is one square

    food_x = round(random.randrange(0, width - snake_pixel_size)/10.0)*10.0 #coordinates for where food spawns
    food_y = round(random.randrange(0, height - snake_pixel_size)/10.0)*10.0

    while not game_over: #button configurations
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                game_over = True
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    x_speed = -snake_pixel_size
                    y_speed = 0
                if i.key == pygame.K_RIGHT:
                    x_speed = snake_pixel_size
                    y_speed = 0
                if i.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_pixel_size
                if i.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_pixel_size

        if x_coor >= width or x_coor < 0 or y_coor >= height or y_coor < 0: #if snake meets window end. game quits
            pygame.quit()

        x_coor += x_speed #position of snake to increase by speed in x and y direction when button pressed
        y_coor += y_speed

        window.fill((0, 0, 0)) #turn window black
        pygame.draw.rect(window, (255, 48, 48), [food_x, food_y, snake_pixel_size, snake_pixel_size]) #create food using randomly generated coordinate
        snake_blocks.append([x_coor, y_coor]) #need to add snake head to list so snake can move and grow by one block only

        if len(snake_blocks) > snake_len:
            del snake_blocks[0]

        create_snake(snake_pixel_size, snake_blocks) #creating snake
        pygame.display.update() #refreshing game screen so everything is visible

        if x_coor == food_x and y_coor == food_y: #increases snake length if food is eaten
            food_x = round(random.randrange(0, width - snake_pixel_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_pixel_size) / 10.0) * 10.0
            snake_len += 1

        clock.tick(snake_speed)

    pygame.quit() #quits game when game_over becomes true breaks while loop
    quit()