import pygame
import random
import sys
from pygame import *
from PIL import Image
img=Image.open('menu1.jpg')
img.show()


#Pre-set
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((803, 599))
filename=('my happy song.wav')
pygame.mixer.music.load(filename)
pygame.mixer.music.play(loops=999, start=0.0)

#blank space for noddle
nb1 = pygame.image.load("p1blank.png")
nb2 = pygame.image.load("p2blank.png")
nb3 = pygame.image.load("p3blank.png")

#Noddle
n1 = pygame.image.load("m1.PNG")
n2 = pygame.image.load("m2.PNG")
n3 = pygame.image.load("m3.PNG")

#People
p1 = pygame.image.load("p1.png")
p2 = pygame.image.load("p2.png")
p3 = pygame.image.load("p3.png")

#food
beef = pygame.image.load("beef.jpg")
chicken = pygame.image.load("chicken.jpg")
egg = pygame.image.load("egg.jpg")
noodle = pygame.image.load("nodle.jpg")
vege = pygame.image.load("vege.jpg")
shrimp = pygame.image.load("xia.jpg")


#Display background
background = pygame.image.load("background.jpg")
pygame.display.set_caption('Dragon Ramen')
screen.blit(background, [0,0])
pygame.mouse.set_visible(1)
pygame.display.update()

#Display food
screen.blit(beef,[20,520])
screen.blit(chicken,[100,520])
screen.blit(egg,[100,450])
screen.blit(noodle,[20,450])
screen.blit(vege,[20,380])
screen.blit(shrimp,[100,380])

#Draw rectangle
veg = pygame.Rect(20,380,50,50)
nod = pygame.Rect(20,450,50,50)
bef = pygame.Rect(20,520,50,50)
chic = pygame.Rect(100,520,50,50)
shri = pygame.Rect(100,380,50,50)
eg = pygame.Rect(100,450,50,50)
telephone = pygame.Rect(665,400,128,180)
dragon = pygame.Rect(577,358,76,110)


#food total
vegetotal = 0
noodtotal = 0
beeftotal = 0
shritotal = 0
egggtotal = 0
chictotal = 0

total = 0


def clear():
    board = pygame.image.load("666.png")
    screen.blit(board,[157,377])


def choose():
    global beef
    global chicken
    global egg
    global noodle
    global vege
    global shrimp
    global veg
    global nod
    global bef
    global chic
    global shri
    global eg
    global telephone
    global total
    global vegetotal
    global noodtotal
    global beeftotal
    global shritotal
    global egggtotal
    global chictotal
    press = pygame.mouse.get_pressed()
    if pygame.mouse.get_pressed() == (1,0,0)  and veg.collidepoint(position) and vegetotal < 1:
        screen.blit(vege,[177,400])
        vegetotal += 1
        total += 1
    if pygame.mouse.get_pressed() == (1,0,0)  and nod.collidepoint(position) and noodtotal < 2:
        screen.blit(noodle,[177,455])
        noodtotal += 2
        total += 2
    if pygame.mouse.get_pressed() == (1,0,0)  and bef.collidepoint(position) and beeftotal < 3:
        screen.blit(beef,[177,510])
        beeftotal += 3
        total += 3
    if pygame.mouse.get_pressed() == (1,0,0)  and shri.collidepoint(position) and shritotal < 4:
        screen.blit(shrimp,[250,400])
        shritotal += 4
        total += 4
    if pygame.mouse.get_pressed() == (1,0,0)  and eg.collidepoint(position) and egggtotal < 5:
        screen.blit(egg,[250,455])
        egggtotal += 5
        total += 5
    if pygame.mouse.get_pressed() == (1,0,0)  and chic.collidepoint(position) and chictotal < 6:
        screen.blit(chicken,[250,510])
        chictotal += 6
        total += 6
    if pygame.mouse.get_pressed() == (1,0,0)  and telephone.collidepoint(position):
        clear()
        vegetotal = 0
        noodtotal = 0
        beeftotal = 0
        shritotal = 0
        egggtotal = 0
        chictotal = 0
        total = 0

def people():
    screen.blit(p1,[100,115])
    screen.blit(p2,[258,115])
    screen.blit(p3,[551,115])

lonoddle = [7,7,11,11,14,14]
lopositon = [1,1,2,2,3,3]
requir1 = 0
requir2 = 0
requir3 = 0
#noddle1 = 7 noddle2 = 11 noddle3 = 14
def requir():
    global total
    global dragon
    global lonoddle
    global lopositon
    global requir1
    global requir2
    global requir3
    global requirment1
    global requirment2
    global requirment3
    global position1
    global position2
    global position3
    press1 = pygame.mouse.get_pressed()
    if requir1 == 0:
        global requirment1
        global position1
        requirment1 = random.choice(lonoddle)
        requir1 = 1
        position1 = random.choice(lopositon)
        lopositon.remove(position1)
        if requirment1 == 7 and position1 == 1:
            screen.blit(n1,[110,10])
        if requirment1 == 7 and position1 == 2:
            screen.blit(n1,[260,10])
        if requirment1 == 7 and position1 == 3:
            screen.blit(n1,[560,10])
        if requirment1 == 11 and position1 == 1:
            screen.blit(n2,[110,10])
        if requirment1 == 11 and position1 == 2:
            screen.blit(n2,[260,10])
        if requirment1 == 11 and position1 == 3:
            screen.blit(n2,[560,10])
        if requirment1 == 14 and position1 == 1:
            screen.blit(n3,[110,10])
        if requirment1 == 14 and position1 == 2:
            screen.blit(n3,[260,10])
        if requirment1 == 14 and position1 == 3:
            screen.blit(n3,[560,10])
    if requir2 == 0:
        global requirment2
        global position2
        requirment2 = random.choice(lonoddle)
        requir2 = 1
        position2 = random.choice(lopositon)
        lopositon.remove(position2)
        if requirment2 == 7 and position2 == 1:
            screen.blit(n1,[110,10])
        if requirment2 == 7 and position2 == 2:
            screen.blit(n1,[260,10])
        if requirment2 == 7 and position2 == 3:
            screen.blit(n1,[560,10])
        if requirment2 == 11 and position2 == 1:
            screen.blit(n2,[110,10])
        if requirment2 == 11 and position2 == 2:
            screen.blit(n2,[260,10])
        if requirment2 == 11 and position2 == 3:
            screen.blit(n2,[560,10])
        if requirment2 == 14 and position2 == 1:
            screen.blit(n3,[110,10])
        if requirment2 == 14 and position2 == 2:
            screen.blit(n3,[260,10])
        if requirment2 == 14 and position2 == 3:
            screen.blit(n3,[560,10])
    if requir3 == 0:
        global requirment3
        global position3
        requirment3 = random.choice(lonoddle)
        requir3 = 1
        position3 = random.choice(lopositon)
        lopositon.remove(position3)
        if requirment3 == 7 and position3 == 1:
            screen.blit(n1,[110,10])
        if requirment3 == 7 and position3 == 2:
            screen.blit(n1,[260,10])
        if requirment3 == 7 and position3 == 3:
            screen.blit(n1,[560,10])
        if requirment3 == 11 and position3 == 1:
            screen.blit(n2,[110,10])
        if requirment3 == 11 and position3 == 2:
            screen.blit(n2,[260,10])
        if requirment3 == 11 and position3 == 3:
            screen.blit(n2,[560,10])
        if requirment3 == 14 and position3 == 1:
            screen.blit(n3,[110,10])
        if requirment3 == 14 and position3 == 2:
            screen.blit(n3,[260,10])
        if requirment3 == 14 and position3 == 3:
            screen.blit(n3,[560,10])

def checkout():
    global score
    global total
    global dragon
    global requir1
    global position1
    global position2
    global position3
    global requirment1
    global requirment2
    global requirment3
    global vegetotal
    global noodtotal
    global beeftotal
    global shritotal
    global egggtotal
    global chictotal
    if pygame.mouse.get_pressed() == (1,0,0)  and dragon.collidepoint(position):
            if total == requirment1:
                screen.blit(nb1,[0,0])
                requir1 = 0
                vegetotal = 0
                noodtotal = 0
                beeftotal = 0
                shritotal = 0
                egggtotal = 0
                chictotal = 0
                total = 0
                lopositon.append(position1)
                lonoddle.append(requirment1)
                score += 100
                print ("Score + 100")
            if total == requirment2:
                screen.blit(nb2,[243,0])
                requir1 = 0
                vegetotal = 0
                noodtotal = 0
                beeftotal = 0
                shritotal = 0
                egggtotal = 0
                chictotal = 0
                total = 0
                lopositon.append(position2)
                lonoddle.append(requirment2)
                score += 100
                print ("Score + 100")
            if total == requirment3:
                screen.blit(nb3,[551,0])
                requir1 = 0
                vegetotal = 0
                noodtotal = 0
                beeftotal = 0
                shritotal = 0
                egggtotal = 0
                chictotal = 0
                total = 0
                lopositon.append(position3)
                lonoddle.appened(requirment3)
                score += 100
                print ("Score + 100")
            else:
                clear()
                vegetotal = 0
                noodtotal = 0
                beeftotal = 0
                shritotal = 0
                egggtotal = 0
                chictotal = 0
                total = 0
score = 0
total = 0

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)

    pygame.display.update()
    position = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()
    choose()
    people()
    requir()
    checkout()
    #noddle1 = 7 noddle2 = 11 noddle3 = 14

pygame.quit()
quit()