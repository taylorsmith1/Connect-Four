import pygame
import time as t
import thread as thread


pygame.init()

display_width = 1000
display_height = 550

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,50)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Connect Four')
clock = pygame.time.Clock()

Red = pygame.image.load('RedDot.png')
Yellow = pygame.image.load('YellowDot.png')
background = pygame.image.load('Connect4Board.png')
white1 = gameDisplay.fill(white)

def back(x2,y2):
    gameDisplay.blit(background,(x2,y2))

def reddot(x,y):
    gameDisplay.blit(Red,(x,y))
  
#RED 1 CODE
#RED 1 CODE
#RED 1 CODE  
  
  
def red1_1(threadName,delay):
    gameDisplay.blit(Red,(25,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (50,50), 27, 0)
    gameDisplay.blit(Red,(25,100))
    
def red1_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (50,125), 27, 0)
    gameDisplay.blit(Red,(25,180))
    
def red1_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (50,200), 27, 0)
    gameDisplay.blit(Red,(25,255))
    
def red1_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (50,275), 27, 0)
    gameDisplay.blit(Red,(25,335))
    
def red1_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (50,360), 27, 0)
    gameDisplay.blit(Red,(25,420))    
    
def allThreadRed1(threadNamee, delay3):
    thread.start_new_thread(red1_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red1_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red1_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red1_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red1_5, ('f', delay3))
    
def fourThreadRed1(threadName,delay):
    thread.start_new_thread(red1_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red1_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red1_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(red1_4, ('f', delay))
    
def threeThreadRed1(threadName,delay):
    thread.start_new_thread(red1_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red1_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red1_3, ('hehe', delay))
    
def twoThreadRed1(threadname,delay):
    thread.start_new_thread(red1_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red1_2, ('hi', delay))
    
def oneThreadRed1(threadname,delay):
    thread.start_new_thread(red1_1, ('lol', delay))





#RED 2 CODE
#RED 2 CODE
#RED 2 CODE




def red2_1(threadName,delay):
    gameDisplay.blit(Red,(115,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (138,50), 27, 0)
    gameDisplay.blit(Red,(115,100))
    
def red2_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (138,125), 27, 0)
    gameDisplay.blit(Red,(115,180))
    
def red2_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (138,200), 27, 0)
    gameDisplay.blit(Red,(115,255))
    
def red2_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (138,275), 27, 0)
    gameDisplay.blit(Red,(115,335))
    
def red2_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (138,360), 27, 0)
    gameDisplay.blit(Red,(115,420))    
    
def allThreadRed2(threadNamee, delay3):
    thread.start_new_thread(red2_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red2_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red2_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red2_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red2_5, ('f', delay3))
    
def fourThreadRed2(threadName,delay):
    thread.start_new_thread(red2_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red2_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red2_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(red2_4, ('f', delay))
    
def threeThreadRed2(threadName,delay):
    thread.start_new_thread(red2_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red2_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red2_3, ('hehe', delay))
    
def twoThreadRed2(threadname,delay):
    thread.start_new_thread(red2_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red2_2, ('hi', delay))
    
def oneThreadRed2(threadname,delay):
    thread.start_new_thread(red2_1, ('lol', delay))


#RED 3
#RED 3
#RED 3



def red3_1(threadName,delay):
    gameDisplay.blit(Red,(205,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (227,50), 27, 0)
    gameDisplay.blit(Red,(205,100))
    
def red3_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (226,125), 27, 0)
    gameDisplay.blit(Red,(205,180))
    
def red3_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (226,200), 27, 0)
    gameDisplay.blit(Red,(205,255))
    
def red3_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (226,275), 27, 0)
    gameDisplay.blit(Red,(205,335))
    
def red3_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (226,360), 27, 0)
    gameDisplay.blit(Red,(205,420))    
    
def allThreadRed3(threadNamee, delay3):
    thread.start_new_thread(red3_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red3_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red3_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red3_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red3_5, ('f', delay3))
    
def fourThreadRed3(threadName,delay):
    thread.start_new_thread(red3_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red3_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red3_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(red3_4, ('f', delay))
    
def threeThreadRed3(threadName,delay):
    thread.start_new_thread(red3_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red3_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red3_3, ('hehe', delay))
    
def twoThreadRed3(threadname,delay):
    thread.start_new_thread(red3_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red3_2, ('hi', delay))
    
def oneThreadRed3(threadname,delay):
    thread.start_new_thread(red3_1, ('lol', delay))


#RED 4
#RED 4
#RED 4



def red4_1(threadName,delay):
    gameDisplay.blit(Red,(295,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (317,50), 27, 0)
    gameDisplay.blit(Red,(295,100))
    
def red4_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (315,125), 27, 0)
    gameDisplay.blit(Red,(295,180))
    
def red4_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (315,200), 27, 0)
    gameDisplay.blit(Red,(295,255))
    
def red4_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (315,275), 27, 0)
    gameDisplay.blit(Red,(295,335))
    
def red4_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (315,360), 27, 0)
    gameDisplay.blit(Red,(295,420))    
    
def allThreadRed4(threadNamee, delay3):
    thread.start_new_thread(red4_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red4_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red4_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red4_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red4_5, ('f', delay3))
    
def fourThreadRed4(threadName,delay):
    thread.start_new_thread(red4_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red4_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red4_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(red4_4, ('f', delay))
    
def threeThreadRed4(threadName,delay):
    thread.start_new_thread(red4_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red4_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red4_3, ('hehe', delay))
    
def twoThreadRed4(threadname,delay):
    thread.start_new_thread(red4_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red4_2, ('hi', delay))
    
def oneThreadRed4(threadname,delay):
    thread.start_new_thread(red4_1, ('lol', delay))

#RED 5
#RED 5
#RED 5


def red5_1(threadName,delay):
    gameDisplay.blit(Red,(385,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (407,50), 27, 0)
    gameDisplay.blit(Red,(385,100))
    
def red5_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (404,125), 27, 0)
    gameDisplay.blit(Red,(385,180))
    
def red5_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (404,200), 27, 0)
    gameDisplay.blit(Red,(385,255))
    
def red5_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (404,275), 27, 0)
    gameDisplay.blit(Red,(385,335))
    
def red5_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (404,360), 27, 0)
    gameDisplay.blit(Red,(385,420))    
    
def allThreadRed5(threadNamee, delay3):
    thread.start_new_thread(red5_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red5_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red5_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red5_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red5_5, ('f', delay3))
    
def fourThreadRed5(threadName,delay):
    thread.start_new_thread(red5_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red5_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red5_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(red5_4, ('f', delay))
    
def threeThreadRed5(threadName,delay):
    thread.start_new_thread(red5_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red5_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red5_3, ('hehe', delay))
    
def twoThreadRed5(threadname,delay):
    thread.start_new_thread(red5_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red5_2, ('hi', delay))
    
def oneThreadRed5(threadname,delay):
    thread.start_new_thread(red5_1, ('lol', delay))

#RED 6
#RED 6
#RED 6



def red6_1(threadName,delay):
    gameDisplay.blit(Red,(475,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (498,50), 27, 0)
    gameDisplay.blit(Red,(475,100))
    
def red6_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (494,125), 27, 0)
    gameDisplay.blit(Red,(475,180))
    
def red6_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (495,200), 27, 0)
    gameDisplay.blit(Red,(475,255))
    
def red6_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (495,275), 27, 0)
    gameDisplay.blit(Red,(475,335))
    
def red6_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (494,360), 27, 0)
    gameDisplay.blit(Red,(475,420))    
    
def allThreadRed6(threadNamee, delay3):
    thread.start_new_thread(red6_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red6_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red6_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red6_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red6_5, ('f', delay3))
    
def fourThreadRed6(threadName,delay):
    thread.start_new_thread(red6_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red6_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red6_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(red6_4, ('f', delay))
    
def threeThreadRed6(threadName,delay):
    thread.start_new_thread(red6_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red6_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red6_3, ('hehe', delay))
    
def twoThreadRed6(threadname,delay):
    thread.start_new_thread(red6_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red6_2, ('hi', delay))
    
def oneThreadRed6(threadname,delay):
    thread.start_new_thread(red6_1, ('lol', delay))



#RED 7
#RED 7
#RED 7


def red7_1(threadName,delay):
    gameDisplay.blit(Red,(565,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (588,50), 27, 0)
    gameDisplay.blit(Red,(565,100))
    
def red7_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (586,125), 27, 0)
    gameDisplay.blit(Red,(565,180))
    
def red7_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (586,200), 27, 0)
    gameDisplay.blit(Red,(565,255))
    
def red7_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (586,275), 27, 0)
    gameDisplay.blit(Red,(565,335))
    
def red7_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (586,360), 27, 0)
    gameDisplay.blit(Red,(565,420))    
    
def allThreadRed7(threadNamee, delay3):
    thread.start_new_thread(red7_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red7_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red7_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red7_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(red7_5, ('f', delay3))
    
def fourThreadRed7(threadName,delay):
    thread.start_new_thread(red7_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red7_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red7_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(red7_4, ('f', delay))
    
def threeThreadRed7(threadName,delay):
    thread.start_new_thread(red7_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red7_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(red7_3, ('hehe', delay))
    
def twoThreadRed7(threadname,delay):
    thread.start_new_thread(red7_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(red7_2, ('hi', delay))
    
def oneThreadRed7(threadname,delay):
    thread.start_new_thread(red7_1, ('lol', delay))
    
    
#YELLOW CODE
 #YELLOW CODE
  #YELLOW CODE
    
    
    
    
#Yellow 1 Code
#Yellow 1 Code
    
    

def yel1_1(threadName,delay):
    gameDisplay.blit(Yellow,(25,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (50,47), 27, 0)
    gameDisplay.blit(Yellow,(25,100))
    
def yel1_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (50,125), 27, 0)
    gameDisplay.blit(Yellow,(25,180))
    
def yel1_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (50,200), 27, 0)
    gameDisplay.blit(Yellow,(25,255))
    
def yel1_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (50,275), 27, 0)
    gameDisplay.blit(Yellow,(25,335))
    
def yel1_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (50,360), 27, 0)
    gameDisplay.blit(Yellow,(25,420))    
    
def allThreadYel1(threadNamee, delay3):
    thread.start_new_thread(yel1_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel1_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel1_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel1_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel1_5, ('f', delay3))
    
def fourThreadYel1(threadName,delay):
    thread.start_new_thread(yel1_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel1_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel1_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(yel1_4, ('f', delay))
    
def threeThreadYel1(threadName,delay):
    thread.start_new_thread(yel1_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel1_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel1_3, ('hehe', delay))
    
def twoThreadYel1(threadname,delay):
    thread.start_new_thread(yel1_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel1_2, ('hi', delay))
    
def oneThreadYel1(threadname,delay):
    thread.start_new_thread(yel1_1, ('lol', delay))    
    
    
    
    
    
    
#Yellow 2 Code
#Yellow 2 Code

def yel2_1(threadName,delay):
    gameDisplay.blit(Yellow,(115,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (138,47), 27, 0)
    gameDisplay.blit(Yellow,(115,100))
    
def yel2_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (138,125), 27, 0)
    gameDisplay.blit(Yellow,(115,180))
    
def yel2_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (138,200), 27, 0)
    gameDisplay.blit(Yellow,(115,255))
    
def yel2_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (138,275), 27, 0)
    gameDisplay.blit(Yellow,(115,335))
    
def yel2_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (138,360), 27, 0)
    gameDisplay.blit(Yellow,(115,420))    
    
def allThreadYel2(threadNamee, delay3):
    thread.start_new_thread(yel2_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel2_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel2_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel2_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel2_5, ('f', delay3))
    
def fourThreadYel2(threadName,delay):
    thread.start_new_thread(yel2_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel2_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel2_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(yel2_4, ('f', delay))
    
def threeThreadYel2(threadName,delay):
    thread.start_new_thread(yel2_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel2_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel2_3, ('hehe', delay))
    
def twoThreadYel2(threadname,delay):
    thread.start_new_thread(yel2_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel2_2, ('hi', delay))
    
def oneThreadYel2(threadname,delay):
    thread.start_new_thread(yel2_1, ('lol', delay))
    
    
#Yellow 3 Code
#Yellow 3 Code

    
def yel3_1(threadName,delay):
    gameDisplay.blit(Yellow,(205,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (226,47), 27, 0)
    gameDisplay.blit(Yellow,(205,100))
    
def yel3_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (226,125), 27, 0)
    gameDisplay.blit(Yellow,(205,180))
    
def yel3_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (226,200), 27, 0)
    gameDisplay.blit(Yellow,(205,255))
    
def yel3_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (226,275), 27, 0)
    gameDisplay.blit(Yellow,(205,335))
    
def yel3_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (226,360), 27, 0)
    gameDisplay.blit(Yellow,(205,420))    
    
def allThreadYel3(threadNamee, delay3):
    thread.start_new_thread(yel3_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel3_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel3_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel3_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel3_5, ('f', delay3))
    
def fourThreadYel3(threadName,delay):
    thread.start_new_thread(yel3_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel3_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel3_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(yel3_4, ('f', delay))
    
def threeThreadYel3(threadName,delay):
    thread.start_new_thread(yel3_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel3_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel3_3, ('hehe', delay))
    
def twoThreadYel3(threadname,delay):
    thread.start_new_thread(yel3_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel3_2, ('hi', delay))
    
def oneThreadYel3(threadname,delay):
    thread.start_new_thread(yel3_1, ('lol', delay))
    
    
    
#Yellow 4 Code
#Yellow 4 Code
    

def yel4_1(threadName,delay):
    gameDisplay.blit(Yellow,(295,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (315,47), 27, 0)
    gameDisplay.blit(Yellow,(295,100))
    
def yel4_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (315,125), 27, 0)
    gameDisplay.blit(Yellow,(295,180))
    
def yel4_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (315,200), 27, 0)
    gameDisplay.blit(Yellow,(295,255))
    
def yel4_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (315,275), 27, 0)
    gameDisplay.blit(Yellow,(295,335))
    
def yel4_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (315,360), 27, 0)
    gameDisplay.blit(Yellow,(295,420))    
    
def allThreadYel4(threadNamee, delay3):
    thread.start_new_thread(yel4_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel4_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel4_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel4_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel4_5, ('f', delay3))
    
def fourThreadYel4(threadName,delay):
    thread.start_new_thread(yel4_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel4_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel4_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(yel4_4, ('f', delay))
    
def threeThreadYel4(threadName,delay):
    thread.start_new_thread(yel4_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel4_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel4_3, ('hehe', delay))
    
def twoThreadYel4(threadname,delay):
    thread.start_new_thread(yel4_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel4_2, ('hi', delay))
    
def oneThreadYel4(threadname,delay):
    thread.start_new_thread(yel4_1, ('lol', delay))
    
    
    
    
#Yellow 5 Code    
#Yellow 5 Code
    
    
def yel5_1(threadName,delay):
    gameDisplay.blit(Yellow,(385,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (404,46), 27, 0)
    gameDisplay.blit(Yellow,(385,100))
    
def yel5_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (404,125), 27, 0)
    gameDisplay.blit(Yellow,(385,180))
    
def yel5_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (404,200), 27, 0)
    gameDisplay.blit(Yellow,(385,255))
    
def yel5_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (404,275), 27, 0)
    gameDisplay.blit(Yellow,(385,335))
    
def yel5_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (404,360), 27, 0)
    gameDisplay.blit(Yellow,(385,420))    
    
def allThreadYel5(threadNamee, delay3):
    thread.start_new_thread(yel5_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel5_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel5_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel5_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel5_5, ('f', delay3))
    
def fourThreadYel5(threadName,delay):
    thread.start_new_thread(yel5_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel5_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel5_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(yel5_4, ('f', delay))
    
def threeThreadYel5(threadName,delay):
    thread.start_new_thread(yel5_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel5_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel5_3, ('hehe', delay))
    
def twoThreadYel5(threadname,delay):
    thread.start_new_thread(yel5_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel5_2, ('hi', delay))
    
def oneThreadYel5(threadname,delay):
    thread.start_new_thread(yel5_1, ('lol', delay))
    
    
    

#Yellow 6 Code
#Yellow 6 Code


def yel6_1(threadName,delay):
    gameDisplay.blit(Yellow,(475,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (494,46), 27, 0)
    gameDisplay.blit(Yellow,(475,100))
    
def yel6_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (494,125), 27, 0)
    gameDisplay.blit(Yellow,(475,180))
    
def yel6_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (494,200), 27, 0)
    gameDisplay.blit(Yellow,(475,255))
    
def yel6_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (494,275), 27, 0)
    gameDisplay.blit(Yellow,(475,335))
    
def yel6_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (494,360), 27, 0)
    gameDisplay.blit(Yellow,(475,420))    
    
def allThreadYel6(threadNamee, delay3):
    thread.start_new_thread(yel6_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel6_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel6_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel6_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel6_5, ('f', delay3))
    
def fourThreadYel6(threadName,delay):
    thread.start_new_thread(yel6_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel6_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel6_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(yel6_4, ('f', delay))
    
def threeThreadYel6(threadName,delay):
    thread.start_new_thread(yel6_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel6_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel6_3, ('hehe', delay))
    
def twoThreadYel6(threadname,delay):
    thread.start_new_thread(yel6_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel6_2, ('hi', delay))
    
def oneThreadYel6(threadname,delay):
    thread.start_new_thread(yel6_1, ('lol', delay))



#Yellow 7 Code
#Yellow 7 Code


def yel7_1(threadName,delay):
    gameDisplay.blit(Yellow,(565,20))
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (586,47), 27, 0)
    gameDisplay.blit(Yellow,(565,100))
    
def yel7_2(threadName1,delay1):
    t.sleep(delay1)
    pygame.draw.circle(gameDisplay, white, (586,125), 27, 0)
    gameDisplay.blit(Yellow,(565,180))
    
def yel7_3(threadName2,delay2):
    t.sleep(delay2)
    pygame.draw.circle(gameDisplay, white, (586,200), 27, 0)
    gameDisplay.blit(Yellow,(565,255))
    
def yel7_4(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (586,275), 27, 0)
    gameDisplay.blit(Yellow,(565,335))
    
def yel7_5(threadName,delay):
    t.sleep(delay)
    pygame.draw.circle(gameDisplay, white, (586,360), 27, 0)
    gameDisplay.blit(Yellow,(565,420))    
    
def allThreadYel7(threadNamee, delay3):
    thread.start_new_thread(yel7_1, ('lol', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel7_2, ('hi', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel7_3, ('hehe', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel7_4, ('f', delay3))
    t.sleep(delay3)
    thread.start_new_thread(yel7_5, ('f', delay3))
    
def fourThreadYel7(threadName,delay):
    thread.start_new_thread(yel7_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel7_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel7_3, ('hehe', delay))
    t.sleep(delay)
    thread.start_new_thread(yel7_4, ('f', delay))
    
def threeThreadYel7(threadName,delay):
    thread.start_new_thread(yel7_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel7_2, ('hi', delay))
    t.sleep(delay)
    thread.start_new_thread(yel7_3, ('hehe', delay))
    
def twoThreadYel7(threadname,delay):
    thread.start_new_thread(yel7_1, ('lol', delay))
    t.sleep(delay)
    thread.start_new_thread(yel7_2, ('hi', delay))
    
def oneThreadYel7(threadname,delay):
    thread.start_new_thread(yel7_1, ('lol', delay))








rWins = 0
yWins = 0


def game_loop():
    
    #pygame.mixer.music.load('Spongebob Trap.mp3')
    #pygame.mixer.music.play(1)
    
    
    turn = 1
    
    
    x2 = 0
    y2 = 0

    redlist1 = []
    redlist2 = []
    redlist3 = []
    redlist4 = []
    redlist5 = []
    redlist6 = []
    redlist7 = []

    #Red List
    #Red List

    superAll = []

    superRed = []

    redV = []
    redH = []
    redP = []
    redN = []
    
    redV1 = []
    redV2 = []
    redV3 = []
    redV4 = []
    redV5 = []
    redV6 = []
    redV7 = []

    redV.append(redV1)
    redV.append(redV2)
    redV.append(redV3)
    redV.append(redV4)
    redV.append(redV5)
    redV.append(redV6)
    redV.append(redV7)

    superRed.append(redV)

    redH1 = []
    redH2 = []
    redH3 = []
    redH4 = []
    redH5 = []
    redH6 = []

    redH.append(redH1)
    redH.append(redH2)
    redH.append(redH3)
    redH.append(redH4)
    redH.append(redH5)
    redH.append(redH6)

    superRed.append(redH)
    
    redP1 = []
    redP2 = []
    redP3 = []
    redP4 = []
    redP5 = []
    redP6 = []

    redP.append(redP1)
    redP.append(redP2)
    redP.append(redP3)
    redP.append(redP4)
    redP.append(redP5)
    redP.append(redP6)

    superRed.append(redP)

    redN1 = []
    redN2 = []
    redN3 = []
    redN4 = []
    redN5 = []
    redN6 = []

    redN.append(redN1)
    redN.append(redN2)
    redN.append(redN3)
    redN.append(redN4)
    redN.append(redN5)
    redN.append(redN6)

    superRed.append(redN)

    #Yellow List
    #Yellow List

    superYel = []

    yelV = []
    yelH = []
    yelP = []
    yelN = []

    yelV1 = []
    yelV2 = []
    yelV3 = []
    yelV4 = []
    yelV5 = []
    yelV6 = []
    yelV7 = []

    yelV.append(yelV1)
    yelV.append(yelV2)
    yelV.append(yelV3)
    yelV.append(yelV4)
    yelV.append(yelV5)
    yelV.append(yelV6)
    yelV.append(yelV7)

    superYel.append(yelV)

    yelH1 = []
    yelH2 = []
    yelH3 = []
    yelH4 = []
    yelH5 = []
    yelH6 = []

    yelH.append(yelH1)
    yelH.append(yelH2)
    yelH.append(yelH3)
    yelH.append(yelH4)
    yelH.append(yelH5)
    yelH.append(yelH6)

    superYel.append(yelH)

    yelP1 = []
    yelP2 = []
    yelP3 = []
    yelP4 = []
    yelP5 = []
    yelP6 = []

    yelP.append(yelP1)
    yelP.append(yelP2)
    yelP.append(yelP3)
    yelP.append(yelP4)
    yelP.append(yelP5)
    yelP.append(yelP6)

    superYel.append(yelP)

    yelN1 = []
    yelN2 = []
    yelN3 = []
    yelN4 = []
    yelN5 = []
    yelN6 = []
    
    yelN.append(yelN1)
    yelN.append(yelN2)
    yelN.append(yelN3)
    yelN.append(yelN4)
    yelN.append(yelN5)
    yelN.append(yelN6)

    superYel.append(yelN)

    superAll.append(superRed)
    superAll.append(superYel)
    
    y = 0
    
    while y <= 5:
        
        redlist1.append(0)
        redlist2.append(0)
        redlist3.append(0)
        redlist4.append(0)
        redlist5.append(0)
        redlist6.append(0)
        redlist7.append(0)

        redV1.append(0)
        redV2.append(0)
        redV3.append(0)
        redV4.append(0)
        redV5.append(0)
        redV6.append(0)
        redV7.append(0)

        yelV1.append(0)
        yelV2.append(0)
        yelV3.append(0)
        yelV4.append(0)
        yelV5.append(0)
        yelV6.append(0)
        yelV7.append(0)

        yelN3.append(0)
        yelN4.append(0)
        yelP3.append(0)
        yelP4.append(0)

        redN3.append(0)
        redN4.append(0)
        redP3.append(0)
        redP4.append(0)

        
        y += 1

    p = 0
    
    while p <= 6:
        
        yelH1.append(0)
        yelH2.append(0)
        yelH3.append(0)
        yelH4.append(0)
        yelH5.append(0)
        yelH6.append(0)

        redH1.append(0)
        redH2.append(0)
        redH3.append(0)
        redH4.append(0)
        redH5.append(0)
        redH6.append(0)

        p += 1


    w = 0

    while w <= 4:

        yelN2.append(0)
        yelN5.append(0)
        yelP2.append(0)
        yelP5.append(0)

        redN2.append(0)
        redN5.append(0)
        redP2.append(0)
        redP5.append(0)

        w += 1
        

    b = 0

    while b <= 3:
        
        yelN1.append(0)
        yelN6.append(0)
        yelP1.append(0)
        yelP6.append(0)

        redN1.append(0)
        redN6.append(0)
        redP1.append(0)
        redP6.append(0)

        b += 1
    
    #print(superAll)
    #print(yelN1)
    #print(redH1)
    
    gameExit = False
    
    gameDisplay.fill(white)
        
    back(x2,y2)
    
#    player1 = raw_input("Player 1 Name = ")
#    player2 = raw_input("Player 2 Name = ")
        
    player1 = "Taylor"
    player2 = "Joseph"
    
    font = pygame.font.Font(None, 40)
    font1 = pygame.font.Font(None, 20)
    font2 = pygame.font.Font(None, 30)
    font3 = pygame.font.Font(None, 50)

    winText = font3.render("Yellow Wins!", 1, yellow)
    winTextpos = (700, 500)

    winTextR = font3.render("Red Wins!", 1, red)
    winTextposR = (725, 500)

    redtext = font3.render("Red", 1, red)
    rtextpos = (680,40)

    yeltext = font3.render("Yellow", 1, yellow)
    ytextpos = (840,40)
    
    text = font.render("Welcome to Connect Four!", 1, black)
    textpos = (643, 0)
    
    text1 = font1.render("Red goes first!", 1, black)
    textpos1 = (643, 90)
    
    text2 = font1.render("Yellow goes second!", 1, black)
    textpos2 = (810, 90)    
    
    text3 = font1.render("Red is numbers 1 - 7!", 1, black)
    textpos3 = (643, 120)
    
    text4 = font1.render("Yellow is letters Q - U!", 1, black)
    textpos4 = (810, 120)
    
    text5 = font1.render("1-7 is Red!", 1, black)
    textpos5 = (643, 100)
    
    text6 = font1.render("q-u is Yellow!", 1, black)
    textpos6 = (840, 100)
    
#BUTTONS    
    
    text7 = font.render("1 / Q", 1, black)
    textpos7 = (18, 500)
    
    text8 = font.render("2 / W", 1, black)
    textpos8 = (110, 500)
    
    text9 = font.render("3 / E", 1, black)
    textpos9 = (200, 500)
    
    text10 = font.render("4 / R", 1, black)
    textpos10 = (290, 500)
    
    text11 = font.render("5 / T", 1, black)
    textpos11 = (380, 500)
    
    text12 = font.render("6 / Y", 1, black)
    textpos12 = (470, 500)
    
    text13 = font.render("7 / U", 1, black)
    textpos13 = (560, 500)
    
    text14 = font2.render("F1 restarts the game", 1, black)
    textpos14 = (700, 490)
    
    text15 = font2.render("ESC quits the game", 1, black)
    textpos15 = (700, 520)
    
    #textpos.centerx = background.get_rect().centerx
    gameDisplay.blit(text, textpos)
    gameDisplay.blit(text1, textpos1)
    gameDisplay.blit(text2, textpos2)
    gameDisplay.blit(text3, textpos3)
    gameDisplay.blit(text4, textpos4)
    gameDisplay.blit(redtext, rtextpos)
    gameDisplay.blit(yeltext, ytextpos)
    #gameDisplay.blit(text5, textpos5)
    #gameDisplay.blit(text6, textpos6)
    
    pygame.draw.line(gameDisplay, black, [640,30], [1000,30], 5)
    pygame.draw.line(gameDisplay, black, [800,30], [800,480], 5)
    pygame.draw.line(gameDisplay, black, [0,480], [1000,480], 5)
    
    pygame.draw.line(gameDisplay, black, [95,479], [95,550], 5)
    gameDisplay.blit(text7,textpos7)
    
    pygame.draw.line(gameDisplay, black, [185,479], [185,550], 5)
    gameDisplay.blit(text8,textpos8)
    
    pygame.draw.line(gameDisplay, black, [275,479], [275,550], 5)
    gameDisplay.blit(text9,textpos9)
    
    pygame.draw.line(gameDisplay, black, [365,479], [365,550], 5)
    gameDisplay.blit(text10,textpos10)
    
    pygame.draw.line(gameDisplay, black, [455,479], [455,550], 5)
    gameDisplay.blit(text11,textpos11)
    
    pygame.draw.line(gameDisplay, black, [545,479], [545,550], 5)
    gameDisplay.blit(text12,textpos12)
    
    pygame.draw.line(gameDisplay, black, [637,0], [637,550], 5)
    gameDisplay.blit(text13,textpos13)
    
    gameDisplay.blit(text14,textpos14)
    gameDisplay.blit(text15,textpos15)
        
        
    
    
    while not gameExit:


        for R in superRed:
            for lis in R:
                for x in range(len(lis)-3):
                    if (int(lis[x]) + int(lis[x+1]) + int(lis[x+2]) + int(lis[x+3])) == 4:
                        gameDisplay.fill(white, (640,483,1000,600))
                        gameDisplay.blit(winTextR,winTextposR)
                        break


        for Y in superYel:
            for lis in Y:
                for x in range(len(lis)-3):
                    if (int(lis[x]) + int(lis[x+1]) + int(lis[x+2]) + int(lis[x+3])) == 4:
                        gameDisplay.fill(white, (640,483,1000,600))
                        gameDisplay.blit(winText,winTextpos)
                        break 
                            
                   
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True           
                
            if event.type == pygame.KEYDOWN:

                '''print(pygame.mouse.get_pos())'''

                
                #RED COMMANDS
                #RED COMMANDS

                if turn == 1:
                
                    if event.key == pygame.K_1:
                        turn = 0
                        if redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 0:
                            redlist1[5] = 1
                            redP3[0] = 1
                            redV1[5] = 1
                            redH6[0] = 1
                            
                            thread.start_new_thread(allThreadRed1, ('how',.5))
                            break                            
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 1:
                            redlist1[4] = 1
                            redP2[0] = 1
                            redV1[4] = 1
                            redH5[0] = 1
                            
                            thread.start_new_thread(fourThreadRed1, ('um',.5))
                            break
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 2:
                            redlist1[3] = 1
                            redP1[0] = 1
                            yelP1[0] = 1
                            redV1[3] = 1
                            redH4[0] = 1
                            
                            thread.start_new_thread(threeThreadRed1, ('a',.5))
                            break
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 3:
                            redlist1[2] = 1
                            redV1[2] = 1
                            redN1[0] = 1
                            redH3[0] = 1
                            
                            thread.start_new_thread(twoThreadRed1, ('b',.5))
                            break 
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 4:
                            redlist1[1] = 1
                            redN2[0] = 1
                            redV1[1] = 1
                            redH2[0] = 1
                            thread.start_new_thread(oneThreadRed1, ('b',.5))
                            break
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 5:
                            redlist1[0] = 1
                            redN3[0] = 1
                            redV1[0] = 1
                            redH1[0] = 1
                            gameDisplay.blit(Red,(25,20))
                            break 
                            
                            
                            
                            
    #                            
                    elif event.key == pygame.K_2:
                        turn = 0
                        if redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 0:
                            redlist2[5] = 1
                            redP4[0] = 1
                            redV2[5] = 1
                            redH6[1] = 1
                            thread.start_new_thread(allThreadRed2, ('how',.5))
                            break                            
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 1:
                            redlist2[4] = 1
                            redV2[4] = 1
                            redP3[1] = 1
                            redH5[1] = 1
                            thread.start_new_thread(fourThreadRed2, ('um',.5))
                            break
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 2:
                            redlist2[3] = 1
                            redP2[1] = 1
                            redN1[1] = 1
                            redV2[3] = 1
                            redH4[1] = 1
                            thread.start_new_thread(threeThreadRed2, ('a',.5))
                            break
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 3:
                            redlist2[2] = 1
                            redP1[1] = 1
                            redN2[1] = 1
                            redV2[2] = 1
                            redH3[1] = 1
                            thread.start_new_thread(twoThreadRed2, ('b',.5))
                            break 
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 4:
                            redlist2[1] = 1
                            redN3[1] = 1
                            redV2[1] = 1
                            redH2[1] = 1
                            thread.start_new_thread(oneThreadRed2, ('b',.5))
                            break
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 5:
                            redlist2[0] = 1
                            redN4[0] = 1
                            redV2[0] = 1
                            redH1[1] = 1
                            gameDisplay.blit(Red,(115,20))
                            break 
                        
                        
                    elif event.key == pygame.K_3:
                        turn = 0
                        if redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 0:
                            redlist3[5] = 1
                            redP5[0] = 1
                            redV3[5] = 1
                            redH6[2] = 1
                            thread.start_new_thread(allThreadRed3, ('how',.5))
                            break                            
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 1:
                            redlist3[4] = 1
                            redP4[1] = 1
                            redN1[2] = 1
                            redV3[4] = 1
                            redH5[2] = 1
                            thread.start_new_thread(fourThreadRed3, ('um',.5))
                            break
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 2:
                            redlist3[3] = 1
                            redP3[2] = 1
                            redN2[2] = 1
                            redV3[3] = 1
                            redH4[2] = 1
                            thread.start_new_thread(threeThreadRed3, ('a',.5))
                            break
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 3:
                            redlist3[2] = 1
                            redV3[2] = 1
                            redP2[2] = 1
                            redN3[2] = 1
                            redH3[2] = 1
                            thread.start_new_thread(twoThreadRed3, ('b',.5))
                            break 
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 4:
                            redlist3[1] = 1
                            redP1[2] = 1
                            redN4[1] = 1
                            redV3[1] = 1
                            redH2[2] = 1
                            thread.start_new_thread(oneThreadRed3, ('b',.5))
                            break
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 5:
                            redlist3[0] = 1
                            redN5[0] = 1
                            redV3[0] = 1
                            redH1[2] = 1
                            gameDisplay.blit(Red,(205,20))
                            break 
                        
                        
                        
                    
                    elif event.key == pygame.K_4:
                        turn = 0
                        if redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 0:
                            redlist4[5] = 1
                            redP6[0] = 1
                            redN1[3] = 1
                            redV4[5] = 1
                            redH6[3] = 1
                            thread.start_new_thread(allThreadRed4, ('how',.5))
                            break                            
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 1:
                            redlist4[4] = 1
                            redP5[1] = 1
                            redN2[3] = 1
                            redV4[4] = 1
                            redH5[3] = 1
                            thread.start_new_thread(fourThreadRed4, ('um',.5))
                            break
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 2:
                            redlist4[3] = 1
                            redP4[2] = 1
                            redN3[3] = 1
                            redV4[3] = 1
                            redH4[3] = 1
                            thread.start_new_thread(threeThreadRed4, ('a',.5))
                            break
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 3:
                            redlist4[2] = 1
                            redP3[3] = 1
                            redN4[2] = 1
                            redV4[2] = 1
                            redH3[3] = 1
                            thread.start_new_thread(twoThreadRed4, ('b',.5))
                            break 
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 4:
                            redlist4[1] = 1
                            redP2[3] = 1
                            redN5[1] = 1
                            redV4[1] = 1
                            redH2[3] = 1
                            thread.start_new_thread(oneThreadRed4, ('b',.5))
                            break
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 5:
                            redlist4[0] = 1
                            redP1[3] = 1
                            redN6[0] = 1
                            redV4[0] = 1
                            redH1[3] = 1
                            gameDisplay.blit(Red,(295,20))
                            break 
                        
                        
                    elif event.key == pygame.K_5:
                        turn = 0
                        if redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 0:
                            redlist5[5] = 1
                            redN2[4] = 1
                            redV5[5] = 1
                            redH6[4] = 1
                            thread.start_new_thread(allThreadRed5, ('how',.5))
                            break                            
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 1:
                            redlist5[4] = 1
                            redP6[1] = 1
                            redN3[4] = 1
                            redV5[4] = 1
                            redH5[4] = 1
                            thread.start_new_thread(fourThreadRed5, ('um',.5))
                            break
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 2:
                            redlist5[3] = 1
                            redP5[2] = 1
                            redN4[3] = 1
                            redV5[3] = 1
                            redH4[4] = 1
                            thread.start_new_thread(threeThreadRed5, ('a',.5))
                            break
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 3:
                            redlist5[2] = 1
                            redP4[3] = 1
                            redN5[2] = 1
                            redV5[2] = 1
                            redH3[4] = 1
                            thread.start_new_thread(twoThreadRed5, ('b',.5))
                            break 
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 4:
                            redlist5[1] = 1
                            redP3[4] = 1
                            redN6[1] = 1
                            redV5[1] = 1
                            redH2[4] = 1
                            thread.start_new_thread(oneThreadRed5, ('b',.5))
                            break
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 5:
                            redlist5[0] = 1
                            redP2[4] = 1
                            redV5[0] = 1
                            redH1[4] = 1
                            gameDisplay.blit(Red,(385,20))
                            break 
                        
                    elif event.key == pygame.K_6:
                        turn = 0
                        if redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 0:
                            redlist6[5] = 1
                            redN3[5] = 1
                            redV6[5] = 1
                            redH6[5] = 1
                            thread.start_new_thread(allThreadRed6, ('how',.5))
                            break                            
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 1:
                            redlist6[4] = 1
                            redN4[4] = 1
                            redV6[4] = 1
                            redH5[5] = 1
                            thread.start_new_thread(fourThreadRed6, ('um',.5))
                            break
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 2:
                            redlist6[3] = 1
                            redP6[2] = 1
                            redN5[3] = 1
                            redV6[3] = 1
                            redH4[5] = 1
                            thread.start_new_thread(threeThreadRed6, ('a',.5))
                            break
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 3:
                            redlist6[2] = 1
                            redP5[3] = 1
                            redN6[2] = 1
                            redV6[2] = 1
                            redH3[5] = 1
                            thread.start_new_thread(twoThreadRed6, ('b',.5))
                            break 
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 4:
                            redlist6[1] = 1
                            redP4[4] = 1
                            redV6[1] = 1
                            redH2[5] = 1
                            thread.start_new_thread(oneThreadRed6, ('b',.5))
                            break
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 5:
                            redlist6[0] = 1
                            redP3[5] = 1
                            redV6[0] = 1
                            redH1[5] = 1
                            gameDisplay.blit(Red,(475,20))
                            break
                       
                    elif event.key == pygame.K_7:
                        turn = 0
                        if redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 0:
                            redlist7[5] = 1
                            redN4[5] = 1
                            redV7[5] = 1
                            redH6[6] = 1
                            thread.start_new_thread(allThreadRed7, ('how',.5))
                            break                            
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 1:
                            redlist7[4] = 1
                            redN5[4] = 1
                            redV7[4] = 1
                            redH5[6] = 1
                            thread.start_new_thread(fourThreadRed7, ('um',.5))
                            break
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 2:
                            redlist7[3] = 1
                            redN6[3] = 1
                            redV7[3] = 1
                            redH4[6] = 1
                            thread.start_new_thread(threeThreadRed7, ('a',.5))
                            break
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 3:
                            redlist7[2] = 1
                            redP6[3] = 1
                            redV7[2] = 1
                            redH3[6] = 1
                            thread.start_new_thread(twoThreadRed7, ('b',.5))
                            break 
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 4:
                            redlist7[1] = 1
                            redP5[4] = 1
                            redV7[1] = 1
                            redH2[6] = 1
                            thread.start_new_thread(oneThreadRed7, ('b',.5))
                            break
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 5:
                            redlist7[0] = 1
                            redP4[5] = 1
                            redV7[0] = 1
                            redH1[6] = 1
                            gameDisplay.blit(Red,(565,20))
                            break
                    
                    
                    
                    
                #YELLOW COMMANDS                    
                #YELLOW COMMANDS

                if turn == 0:
                    
                    if event.key == pygame.K_q:
                        turn = 1
                        if redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 0:
                            redlist1[5] = 1
                            yelP3[0] = 1
                            yelV1[5] = 1
                            yelH6[0] = 1
                            thread.start_new_thread(allThreadYel1, ('how',.5))
                            break                            
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 1:
                            redlist1[4] = 1
                            yelP2[0] = 1
                            yelV1[4] = 1
                            yelH5[0] = 1
                            thread.start_new_thread(fourThreadYel1, ('um',.5))
                            break
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 2:
                            redlist1[3] = 1
                            yelP1[0] = 1
                            yelV1[3] = 1
                            yelH4[0] = 1
                            thread.start_new_thread(threeThreadYel1, ('a',.5))
                            break
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 3:
                            redlist1[2] = 1
                            yelN1[0] = 1
                            yelV1[2] = 1
                            yelH3[0] = 1
                            thread.start_new_thread(twoThreadYel1, ('b',.5))
                            break 
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 4:
                            redlist1[1] = 1
                            yelN2[0] = 1
                            yelV1[1] = 1
                            yelH2[0] = 1
                            thread.start_new_thread(oneThreadYel1, ('b',.5))
                            break
                        elif redlist1[0] + redlist1[1] + redlist1[2] + redlist1[3] + redlist1[4] + redlist1[5] == 5:
                            redlist1[0] = 1
                            yelN3[0] = 1
                            yelV1[0] = 1
                            yelH1[0] = 1
                            gameDisplay.blit(Yellow,(25,20))
                            break 
                            
                            
                            
                            
    #                            
                    elif event.key == pygame.K_w:
                        turn = 1
                        if redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 0:
                            redlist2[5] = 1
                            yelP4[0] = 1
                            yelV2[5] = 1
                            yelH6[1] = 1
                            thread.start_new_thread(allThreadYel2, ('how',.5))
                            break                            
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 1:
                            redlist2[4] = 1
                            yelP3[1] = 1
                            yelV2[4] = 1
                            yelH5[1] = 1
                            thread.start_new_thread(fourThreadYel2, ('um',.5))
                            break
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 2:
                            redlist2[3] = 1
                            yelP2[1] = 1
                            yelN1[1] = 1
                            yelV2[3] = 1
                            yelH4[1] = 1
                            thread.start_new_thread(threeThreadYel2, ('a',.5))
                            break
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 3:
                            redlist2[2] = 1
                            yelP1[1] = 1
                            yelN2[1] = 1
                            yelV2[2] = 1
                            yelH3[1] = 1                            
                            thread.start_new_thread(twoThreadYel2, ('b',.5))
                            break 
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 4:
                            redlist2[1] = 1
                            yelN3[1] = 1
                            yelV2[1] = 1
                            yelH2[1] = 1                            
                            thread.start_new_thread(oneThreadYel2, ('b',.5))
                            break
                        elif redlist2[0] + redlist2[1] + redlist2[2] + redlist2[3] + redlist2[4] + redlist2[5] == 5:
                            redlist2[0] = 1
                            yelN4[0] = 1
                            yelV2[0] = 1
                            yelH1[1] = 1                            
                            gameDisplay.blit(Yellow,(115,20))
                            break 
                        
                        
                    elif event.key == pygame.K_e:
                        turn = 1
                        if redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 0:
                            redlist3[5] = 1
                            yelP5[0] = 1
                            yelV3[5] = 1
                            yelH6[2] = 1
                            thread.start_new_thread(allThreadYel3, ('how',.5))
                            break                            
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 1:
                            redlist3[4] = 1
                            yelP4[1] = 1
                            yelN1[2] = 1
                            yelV3[4] = 1
                            yelH5[2] = 1
                            thread.start_new_thread(fourThreadYel3, ('um',.5))
                            break
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 2:
                            redlist3[3] = 1
                            yelP3[2] = 1
                            yelN2[2] = 1
                            yelV3[3] = 1
                            yelH4[2] = 1
                            thread.start_new_thread(threeThreadYel3, ('a',.5))
                            break
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 3:
                            redlist3[2] = 1
                            yelP2[2] = 1
                            yelN3[2] = 1
                            yelV3[2] = 1
                            yelH3[2] = 1                            
                            thread.start_new_thread(twoThreadYel3, ('b',.5))
                            break 
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 4:
                            redlist3[1] = 1
                            yelP1[2] = 1
                            yelN4[1] = 1
                            yelV3[1] = 1
                            yelH2[2] = 1                            
                            thread.start_new_thread(oneThreadYel3, ('b',.5))
                            break
                        elif redlist3[0] + redlist3[1] + redlist3[2] + redlist3[3] + redlist3[4] + redlist3[5] == 5:
                            redlist3[0] = 1
                            yelN5[0] = 1
                            yelV3[0] = 1
                            yelH1[2] = 1                         
                            gameDisplay.blit(Yellow,(205,20))
                            break 
                        
                        
                        
                    
                    elif event.key == pygame.K_r:
                        turn = 1
                        if redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 0:
                            redlist4[5] = 1
                            yelP6[0] = 1
                            yelN1[3] = 1
                            yelV4[5] = 1
                            yelH6[3] = 1
                            thread.start_new_thread(allThreadYel4, ('how',.5))
                            break                            
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 1:
                            redlist4[4] = 1
                            yelP5[1] = 1
                            yelN2[3] = 1
                            yelV4[4] = 1
                            yelH5[3] = 1
                            thread.start_new_thread(fourThreadYel4, ('um',.5))
                            break
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 2:
                            redlist4[3] = 1
                            yelP4[2] = 1
                            yelN3[3] = 1
                            yelV4[3] = 1
                            yelH4[3] = 1
                            thread.start_new_thread(threeThreadYel4, ('a',.5))
                            break
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 3:
                            redlist4[2] = 1
                            yelP3[3] = 1
                            yelN4[2] = 1
                            yelV4[2] = 1
                            yelH3[3] = 1                            
                            thread.start_new_thread(twoThreadYel4, ('b',.5))
                            break 
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 4:
                            redlist4[1] = 1
                            yelP2[3] = 1
                            yelN5[1] = 1
                            yelV4[1] = 1
                            yelH2[3] = 1
                            thread.start_new_thread(oneThreadYel4, ('b',.5))
                            break
                        elif redlist4[0] + redlist4[1] + redlist4[2] + redlist4[3] + redlist4[4] + redlist4[5] == 5:
                            redlist4[0] = 1
                            yelP1[3] = 1
                            yelN6[0] = 1
                            yelV4[0] = 1
                            yelH1[3] = 1                            
                            gameDisplay.blit(Yellow,(295,20))
                            break 
                        
                        
                    elif event.key == pygame.K_t:
                        turn = 1
                        if redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 0:
                            redlist5[5] = 1
                            yelN2[4] = 1
                            yelV5[5] = 1
                            yelH6[4] = 1
                            thread.start_new_thread(allThreadYel5, ('how',.5))
                            break                            
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 1:
                            redlist5[4] = 1
                            yelP6[1] = 1
                            yelN3[4] = 1
                            yelV5[4] = 1
                            yelH5[4] = 1
                            thread.start_new_thread(fourThreadYel5, ('um',.5))
                            break
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 2:
                            redlist5[3] = 1
                            yelP5[2] = 1
                            yelN4[3] = 1
                            yelV5[3] = 1
                            yelH4[4] = 1
                            thread.start_new_thread(threeThreadYel5, ('a',.5))
                            break
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 3:
                            redlist5[2] = 1
                            yelP4[3] = 1
                            yelN5[2] = 1
                            yelV5[2] = 1
                            yelH3[4] = 1                            
                            thread.start_new_thread(twoThreadYel5, ('b',.5))
                            break 
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 4:
                            redlist5[1] = 1
                            yelP3[4] = 1
                            yelN6[1] = 1
                            yelV5[1] = 1
                            yelH2[4] = 1                            
                            thread.start_new_thread(oneThreadYel5, ('b',.5))
                            break
                        elif redlist5[0] + redlist5[1] + redlist5[2] + redlist5[3] + redlist5[4] + redlist5[5] == 5:
                            redlist5[0] = 1
                            yelP2[4] = 1
                            yelV5[0] = 1
                            yelH1[4] = 1                            
                            gameDisplay.blit(Yellow,(385,20))
                            break 
                        
                    elif event.key == pygame.K_y:
                        turn = 1
                        if redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 0:
                            redlist6[5] = 1
                            yelN3[5] = 1
                            yelV6[5] = 1
                            yelH6[5] = 1
                            thread.start_new_thread(allThreadYel6, ('how',.5))
                            break                            
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 1:
                            redlist6[4] = 1
                            yelN4[4] = 1
                            yelV6[4] = 1
                            yelH5[5] = 1
                            thread.start_new_thread(fourThreadYel6, ('um',.5))
                            break
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 2:
                            redlist6[3] = 1
                            yelP6[2] = 1
                            yelN5[3] = 1
                            yelV6[3] = 1
                            yelH4[5] = 1
                            thread.start_new_thread(threeThreadYel6, ('a',.5))
                            break
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 3:
                            redlist6[2] = 1
                            yelP5[3] = 1
                            yelN6[2] = 1
                            yelV6[2] = 1
                            yelH3[5] = 1                            
                            thread.start_new_thread(twoThreadYel6, ('b',.5))
                            break 
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 4:
                            redlist6[1] = 1
                            yelP4[4] = 1
                            yelV6[1] = 1
                            yelH2[5] = 1                            
                            thread.start_new_thread(oneThreadYel6, ('b',.5))
                            break
                        elif redlist6[0] + redlist6[1] + redlist6[2] + redlist6[3] + redlist6[4] + redlist6[5] == 5:
                            redlist6[0] = 1
                            yelP3[5] = 1
                            yelV6[0] = 1
                            yelH1[5] = 1                            
                            gameDisplay.blit(Yellow,(475,20))
                            break
                       
                    elif event.key == pygame.K_u:
                        turn = 1
                        if redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 0:
                            redlist7[5] = 1
                            yelN4[5] = 1
                            yelV7[5] = 1
                            yelH6[6] = 1
                            thread.start_new_thread(allThreadYel7, ('how',.5))
                            break                            
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 1:
                            redlist7[4] = 1
                            yelN5[4] = 1
                            yelV7[4] = 1
                            yelH5[6] = 1
                            thread.start_new_thread(fourThreadYel7, ('um',.5))
                            break
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 2:
                            redlist7[3] = 1
                            yelN6[3] = 1
                            yelV7[3] = 1
                            yelH4[6] = 1
                            thread.start_new_thread(threeThreadYel7, ('a',.5))
                            break
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 3:
                            redlist7[2] = 1
                            yelP6[3] = 1
                            yelV7[2] = 1
                            yelH3[6] = 1                            
                            thread.start_new_thread(twoThreadYel7, ('b',.5))
                            break 
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 4:
                            redlist7[1] = 1
                            yelP5[4] = 1
                            yelV7[1] = 1
                            yelH2[6] = 1
                            
                            thread.start_new_thread(oneThreadYel7, ('b',.5))
                            break
                        elif redlist7[0] + redlist7[1] + redlist7[2] + redlist7[3] + redlist7[4] + redlist7[5] == 5:
                            redlist7[0] = 1
                            yelP4[5] = 1
                            yelV7[0] = 1
                            yelH1[6] = 1                  
                            gameDisplay.blit(Yellow,(565,20))
                            break
                
                if turn == turn:
                
                    if event.key == pygame.K_F1:
                        game_loop()
                    
                    
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                
        
                        
                        
        
        pygame.display.update()
        clock.tick(60)
        
game_loop()
pygame.quit()
