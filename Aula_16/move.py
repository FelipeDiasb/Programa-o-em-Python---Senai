import pygame

pygame.init()

tela  = pygame.display.set_mode((500,500)) 
quadrado = pygame.Rect(250,250,50,50)
clock = pygame.time.Clock()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
            pygame.quit()

# movimento através de eventos Keydown - pressionar tecla 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                quadrado.move_ip([10,0])
            if event.key == pygame.K_a:
                quadrado.move_ip([-10,0])
            if event.key == pygame.K_s:
                quadrado.move_ip([0,10])
            if event.key == pygame.K_w:
                quadrado.move_ip([0,-10])
    
    tela.fill('red')
    pygame.draw.rect(tela, ('blue'),quadrado)  
    pygame.display.update()
                          
  

    # pygame.draw.circle(tela,('yellow'), (900,250),200)
    # pygame.draw.ellipse(tela, ('pink'),(750, 650, 540,200 ))
    # pygame.draw.line(tela, ('black'), (400, 800), (200,200),10)
    # pygame.display.flip() 
    # utilize a biblioteca para desenhar:
    # circulo
    # elipse

    


  




