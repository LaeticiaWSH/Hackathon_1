import pygame,random
from pygame.math import Vector2
import psycopg2

class Fruits:
    def __init__(self):
       self.random_pos()
       self.ele = melon
    def create_fruit(self):
        fruit_cicle = pygame.Rect(int(self.position.x * screen_width),(self.position.y* screen_width),screen_width,screen_width)
        screen.blit(self.ele,fruit_cicle)
        #pygame.draw.rect(screen,(225,0,0),fruit_cicle)
    def random_pos(self):
        self.x = random.randint(1,18)
        self.y = random.randint(1,15)
        # self.x = 18
        # self.y = 1
        self.position = Vector2(self.x,self.y)
    def random_obj(self):
        list = [melon,potion]
        self.ele = random.choice(list)
        if self.ele ==  melon:
            return True
        else:
            return False
        


         
class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_part = False
        self.color = 198,172,143

    def create_snake(self):
        for parts in self.body:
            parts_rect = pygame.Rect(int(parts.x * screen_width),int(parts.y * screen_width),screen_width,screen_width)
            pygame.draw.rect(screen,(self.color),parts_rect,border_radius = 40)
        
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

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        


class Game():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruits()
        self.valid = "Yes"
        self.score_text = 0
    def update(self):
        self.snake.move_snake()
        self.collision()
        self.game_over()

    def create_objects(self):
        self.fruit.create_fruit()
        self.snake.create_snake()
        self.score()
    def collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.random_obj()
            self.fruit.random_pos()
            self.snake.add_body()
            self.change_color()

        for part in self.snake.body[1:]:
            if part == self.fruit.position:
                self.fruit.random_pos()
            
    def game_over(self):
        if not 0 < self.snake.body[0].x <= 18 or not 0 < self.snake.body[0].y <= 15 :
            self.store_score()
            #self.restart()
            pygame.quit()

        for part in self.snake.body[1:]:
            if part == self.snake.body[0]:
                self.store_score()
                pygame.quit()
                #self.restart()

    def score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(0,0,0))
        score_rect =score_surface.get_rect(center = (400,21))
        screen.blit(score_surface,score_rect)
        self.text("Score :",game_font,(0,0,0),320,10)
        self.score_text = score_text
        

    def change_color(self):
            c = self.fruit.random_obj()
            if c == True:
                self.snake.color = 198,172,143
                self.valid = "Yes"
            else:
                self.snake.color = 0,180,216
                self.valid ="No"
                
    def change_text(self):
        if  self.valid == "Yes":
            self.text("I love melons",game_font,(231,111,81),320,650)
        else:
            self.text("I'm blue dadadee dadada.",game_font,(42,157,143),310,650)
    
    def text(self,text,font,text_col,x,y):
        txt = font.render(text,True,text_col)
        screen.blit(txt,(x,y))

    def restart(self):
        self.snake.reset()
        

    def store_score(self):
        HOSTNAME = 'localhost'
        USERNAME = 'laeticiaoceane'
        PASSWORD = '12345678'
        DATABASE = 'game'

        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

        cursor = connection.cursor()
        query = "INSERT INTO gamer(score_pt) VALUES (%s)"
        cursor.execute(query,(self.score_text))
        connection.commit()
        cursor.close()
        connection.close()
    def high_score(self):
        HOSTNAME = 'localhost'
        USERNAME = 'laeticiaoceane'
        PASSWORD = '12345678'
        DATABASE = 'game'

        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

        cursor = connection.cursor()
        query = "SELECT user_id,score_pt FROM gamer ORDER BY score_pt DESC"
        cursor.execute(query)
        top_scores = cursor.fetchall()
        cursor.close()
        connection.close()
        print(top_scores)
    
        

pygame.init() #It's mandatory to initialize the import pygame.
#color = 198,172,143
screen_width = 40
screen_height = 20
#screen = pygame.display.set_mode((screen_width*screen_height,screen_width*screen_height)) # pygame.display.set_mode, it  sets the screen to be displayed - display surface.
screen = pygame.display.set_mode((800,700))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
melon =pygame.image.load('pngegg.png').convert_alpha()
potion = pygame.image.load('potion.png').convert_alpha()
game_font = pygame.font.SysFont('leelawadeeuisemilight',30)
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
    snake_game.change_text()
    
    pygame.display.update()
    #pygame.display.flip()
    clock.tick(70)


pygame.quit() # The function that will close the screen.
