import pygame,random
from pygame.math import Vector2

class Fruits:
    def __init__(self):
       self.random_pos()
    def create_fruit(self):
        fruit_cicle = pygame.Rect(int(self.position.x * screen_width),(self.position.y* screen_width),screen_width,screen_width)
        pygame.draw.rect(screen,(225,0,0),fruit_cicle)
    def random_pos(self):
        self.x = random.randint(1,18)
        self.y = random.randint(1,15)
        # self.x = 18
        # self.y = 1
        self.position = Vector2(self.x,self.y)

         
class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_part = False

    def create_snake(self):
        for parts in self.body:
            parts_rect = pygame.Rect(int(parts.x * screen_width),int(parts.y * screen_width),screen_width,screen_width)
            pygame.draw.rect(screen,(217,237,146),parts_rect)
        
    def move_snake(self):
        if self.new_part == True:
            change_move = self.body[:]
            change_move.insert(0,change_move[0] + self.direction)
            self.body = change_move[:]
            self.new_part = False
        else:
            change_move = self.body[:-1]
            change_move.insert(0,change_move[0] + self.direction)
            self.body = change_move[:]

    def add_body(self):
        self.new_part = True


class Game():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruits()
    def update(self):
        self.snake.move_snake()
        self.collision()
        self.game_over()

    def create_objects(self):
        self.fruit.create_fruit()
        self.snake.create_snake()
    def collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.random_pos()
            self.snake.add_body()
    def game_over(self):
        if not 0 < self.snake.body[0].x <= 18 or not 0 < self.snake.body[0].y <= 15 :
            pygame.quit()




pygame.init() #It's mandatory to initialize the import pygame.
screen_width = 40
screen_height = 20
#screen = pygame.display.set_mode((screen_width*screen_height,screen_width*screen_height)) # pygame.display.set_mode, it  sets the screen to be displayed - display surface.
screen = pygame.display.set_mode((800,700))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
#melon =pygame.image.load('potion.png').convert_alpha()

snake_game = Game()

run = True

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,200)
while run:    #A statement that will keep the screen open .
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          #DON'T FORGET an event is often times an user input.
        if event.type == SCREEN_UPDATE:
            snake_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_game.snake.direction.y != 1:
                    snake_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if snake_game.snake.direction.y != -1:
                    snake_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if snake_game.snake.direction.x != 1:
                    snake_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if snake_game.snake.direction.x != -1:
                    snake_game.snake.direction = Vector2(1,0)
            




    screen.fill((88,129,87))     # fill the screen with a color to wipe away anything from last frame
    pygame.draw.rect(screen,(218,215,205),(35,35,730,610),width = 4)    #This is the border white
    
    snake_game.create_objects()

    
    pygame.display.update()
    clock.tick(70)


pygame.quit() # The function that will close the screen.

