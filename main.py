import os
import urllib.request
import math
from random import randint, random
import time
import pygame







def game(true,showtext):
    
    
    pygame.init()

    SCREENHEIGHT = 640
    SCREENWIDTH = 480

    if not os.path.exists("Highscore.dat"):
        with open("Highscore.dat","w") as f:
            f.write("0")


    window = pygame.display.set_mode((SCREENHEIGHT,SCREENWIDTH))
    pygame.display.set_caption("Snakes Maina by aditya")
    exit_game = False
    game_over = False
    home_screen = True
    x = 12
    y = 32
    velo_x = 0
    velo_y = 0
    snake_l = []
    snake_len = 0
    score = 0
    radius = 7
    show_ball = False
    splashScreenTimer = 0
    f_x = randint(0,620)
    f_y = randint(0,400)
    b_x = randint(0,620)
    b_y = randint(0,400)
    with open("Highscore.dat","r") as f:
        global highscore
        a = f.read()
        highscore = a

    clock = pygame.time.Clock()

    urllib.request.urlretrieve(
    'https://programmingwithaditya.000webhostapp.com/snake.png',
    "snake.png")
    

    
    def CheckCollision(x1,x2,y2,y1):
        if abs(x1 - x2) < 16 and abs(y1 - y2) < 16:   
            return True
        else:
            return False

    def snake():
        for x,y in  snake_l:
            pygame.draw.circle(window,(0,0,0),(x,y),7)
    
        
 


    while splashScreenTimer < 1.8 and true:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            dt = clock.tick(60) / 1000
            splashScreenTimer += dt 
            window.fill((100,150,250))
            font = pygame.font.Font("font.otf",40)
            text = font.render("CREATED BY ADITYA",True,(48, 93, 120))
            window.blit(text,(175,200))
            pygame.display.update()
        


    home_screen = True
    while home_screen:
        clock.tick(60)/ 100
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            window.fill((100,205,80))
            font = pygame.font.Font("font.otf",30)
            text = font.render("SPACE TO START",True,(0, 0, 0))
            window.blit(text,(225,290))
            font2 = pygame.font.Font("font.otf",90)
            name = font2.render("SNAKE",True,(0, 0, 0))
            lost = font.render("Game Over",True,(0, 0, 0))
            window.blit(name,(window.get_width()/2 - name.get_width()/2,190 + math.sin(time.time()*5)*5 - 25))
            if showtext:
                window.blit(lost,(window.get_width()/2 - lost.get_width()/2,30))
            try:
                img = pygame.image.load("snake.png")
                img = pygame.transform.scale(img,(122,122)).convert_alpha()
                window.blit(img,(260,50))
            except Exception as e:
                if e == FileNotFoundError:
                    pass

            pygame.display.update()
            pygame.time.delay(10)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    home_screen = False
        x = 12
        y = 12
        velo_x = 0
        velo_y = 0

    
            
    while not exit_game:

        clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit_game = True
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            velo_x = -1.8
            velo_y = 0

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            velo_x = 1.8
            velo_y = 0

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            velo_y = 1.9
            velo_x = 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            velo_y = -1.9
            velo_x = 0

        if CheckCollision(f_x,x,y,f_y):
            f_x = randint(0,SCREENWIDTH / 2)
            f_y = randint(0,SCREENHEIGHT / 2)
            snake_len += 10
            score += 10
      
            with open("Highscore.dat","r") as f:
                content = f.read()

                if int(content) < int(score):
                    with open("Highscore.dat","w") as  file:
                        file.write(str(score))
                        highscore = score
        

        if x > 630:
            x = 0

        if x < 0:
            x = 630

        if y < 0:
            y = 460

        if y > 466:
            y = 0

            

        if len(snake_l)>snake_len:
            del snake_l[0]
        

        

        x = velo_x + x
        y = velo_y + y
        head = []
        head.append(x)
        head.append(y)
        snake_l.append(head)
        window.fill((255,255,255))
        font = pygame.font.Font("font.otf",40)
        scoretext = font.render(f"Score:{score} Highscore:{highscore}",True,(0,0,0))
        window.blit(scoretext,(50,0))
        snake()
        
        if head in snake_l[:-1]:
            
            game(False,True)
            pygame.display.update()

        apple = pygame.draw.circle(window,(255,0,0),(f_x,f_y),radius)
        pygame.display.update()
    

game(True,False)