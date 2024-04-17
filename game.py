import sys, pygame,random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1, 0)
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,191,122),block_rect)
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body = body_copy[:]
class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)
        #Creando x y
        #Dibujando un cuadrado
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126,166,114), fruit_rect)
        #create a rectangle

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        snake.move_snake()

pygame.init()
#Poner las celdas
cell_size =40
cell_number = 20
#Tamaño de pantalla
screen = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))



clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

#Rectangulo

#test_surface = pygame.Surface((100,200))
#test_surface.fill((0,0,255))
#Posición inicial
#x_pos = 400

#test_rect = test_surface.get_rect(topright=(200,250))


#Se seguirá ejecutando mientras
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==SCREEN_UPDATE:
            main_game.update()
            #Aqui es el evento cuando toquemos los botones
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
    #fondo
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    #test_rect.right += 1

    #x_pos -= 1
    #screen.blit(test_surface,(200,250))
    #mostrar todos los elementos, el refresh de la pantalla
    pygame.display.update()
    #Este es el framerate o velocidad a la que irá la serpiente
    clock.tick(60)


