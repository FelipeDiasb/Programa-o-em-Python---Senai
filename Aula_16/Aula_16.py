# import pygame

# pygame.init() # inicio 

# size = 1000, 500

# tela = pygame.display.set_mode(size)
# pygame.display.set_caption('Titulo')


# teste = True

# while teste:
#     pass


import pygame
import sys

pygame.init()

WIDTH= 800
LENGTH = 500


tela = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption('Teste') # titulo

#loop da página 
quandrado =  pygame.Rect(250,250, 50,50)
qd2 = pygame.Rect(10,150, 50,50)
lipss= pygame.Rect(100,150, 10,40)
lipss1= pygame.Rect(250,250, 80,50)

clock =  pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit() 
  
    if event.type == pygame.KEYDOWN:
             
            if event.key == pygame.K_RIGHT:
                quandrado.move_ip([5,0])
            if event.key == pygame.K_LEFT:
                quandrado.move_ip([-10,0])
            if event.key == pygame.K_UP:
                quandrado.move_ip([0,-10])
            if event.key == pygame.K_DOWN:
                quandrado.move_ip([0,5]) 
                # 2 variavel qd2      
            if event.key == pygame.K_RIGHT:
                qd2.move_ip([5,0])
            if event.key == pygame.K_LEFT:
                qd2.move_ip([-10,0])
            if event.key == pygame.K_UP:
                qd2.move_ip([0,-10])
            if event.key == pygame.K_DOWN:
                qd2.move_ip([0,5])   
              # 3 variavel 
            # if event.key == pygame.K_RIGHT:
            #     quandrado.move_ip([5,0])
            # if event.key == pygame.K_LEFT:
            #     quandrado.move_ip([-10,0])
            # if event.key == pygame.K_UP:
            #     quandrado.move_ip([0,-10])
            # if event.key == pygame.K_DOWN:
            #     quandrado.move_ip([0,5])  
                
                   
            cor =  (240,230,140)
            tela.fill('black')                     
           

    pygame.draw.rect(tela,('white'),quandrado) # 
    pygame.draw.ellipse(tela,('yellow'),lipss1)
    pygame.draw.rect(tela,('blue'),qd2)
    pygame.draw.ellipse(tela,('red'),lipss)
    pygame.display.update()

       
    pygame.display.flip()
        