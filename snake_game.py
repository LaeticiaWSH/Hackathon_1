import pygame, sys,random
from pygame import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4, 10), Vector2(3, 10)] #this is going to be 3 blocks next to each other (starting position)
        self.direction = Vector2(1,0)
        self.new_block = False
        
    def draw_snake(self):
        for block in self.body:
            x_position = int(block.x * cell_size)
            y_position = int(block.y * cell_size)
            block_rect = pygame.Rect(x_position, y_position ,cell_size , cell_size)
            pygame.draw.rect(screen, (183, 111, 122),block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] 
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False

        else:
            body_copy = self.body[: -1] # copy the snake body not including the last block
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

        

    
    def add_block(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
        self.randomize()

    def randomize(self):
        # creating an x and y position by using vector2
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.postion = Vector2(self.x, self.y)

    def draw_fruit(slef):
        # creating a fruit rectangle
        fruit_rect = pygame.Rect(int(slef.postion.x * cell_size), int(slef.postion.y * cell_size) ,cell_size, cell_size)
        # Drawing the rectangle
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(slef):
        slef.snake.move_snake()
        slef.check_collision()
        slef.check_die()

    def draw_element(slef):
        slef.fruit.draw_fruit()
        slef.snake.draw_snake()

    def check_collision(slef):
        if slef.fruit.postion == slef.snake.body[0]:
            # reposition the fruit
            slef.fruit.randomize()
            # add another block to the snake
            slef.snake.add_block()

    def check_die(self):
        # check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
 
    def game_over(self):
         pygame.quit()
         sys.exit()



pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)

    screen.fill((175,215,70)) 
    main_game.draw_element()
    pygame.display.update()
    clock.tick(60)
