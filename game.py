import sys, pygame,random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(6,10),Vector2(7,10)]
    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(x,y,w,h)


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

pygame.init()
#Poner las celdas
cell_size =40
cell_number = 20
#Tamaño de pantalla
screen = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))



clock = pygame.time.Clock()

fruit = FRUIT()
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
    #fondo
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    #test_rect.right += 1

    #x_pos -= 1
    #screen.blit(test_surface,(200,250))
    #mostrar todos los elementos, el refresh de la pantalla
    pygame.display.update()
    #Este es el framerate o velocidad a la que irá la serpiente
    clock.tick(60)


