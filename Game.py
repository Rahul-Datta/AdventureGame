# Name:        module1
# Purpose:
#
# Author:      7004008
#
# Created:     17/11/2022
# Copyright:   (c) 7004008 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE =	(255,255,255)
BLUE = (0,128,255)
GREEN = (0, 128, 0)
GREEN2=(0,130,78)
WATERCOLOR=(15,94,156)
SKYCOLOR=(0,181,226)
ORANGE=(255, 102, 0)
CHOCOLATE=(65,25,0)
GRAY=(160,160,160)
NATURAL_DIRT=(155,118,83)
rect_x = 250
rect_y = 450
# Set the height and width of the screen
size = (710, 710)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adventure game")
# Loop until the user clicks the close button.
PI=3.14159
room_list=[]

current_room=0
done=False

clock = pygame.time.Clock()

key=0



room=("You are in the room 0. There is a passage to the East",None,1,None,None)     #These are the Room details.
room_list.append(room)

room=("You are in the room 1. There is a passage to the North and West",4,None,0,None)
room_list.append(room)

room=("You are in the room 2. There is a passage to the North and East ",5,"Swimming pool",None,None)
room_list.append(room)

room=("You are in the room 3. There is a passage to the North and East",6,4,None,None)
room_list.append(room)

room=("You are in the room 4. There is a passage to the West, North and South",7,None,3,1)
room_list.append(room)

room=("You are in the room 5. There is a passage to the North and South",8,None,None,2)
room_list.append(room)

room=("You are in the room 6. There is a passage to the West,East and South",None,7,"Garden",3)
room_list.append(room)


room=("You are in the room 7. There is a passage to the East, West and South",None,8,6,4)
room_list.append(room)

room=("You are in the room 8. There is a passage to the East,West and South",None,"Field",7,5)
room_list.append(room)


userInput=""
userOutput=""
user_guess=""
Input=""
Output=""
input_rect=pygame.Rect(300,120,80,25)
output_rect=pygame.Rect(12,560,500,100)
next_room=""

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
             done=True

        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                user_guess=user_guess[:-1]    # That's for userinput
            elif event.key==pygame.K_RETURN:
                Input=user_guess
            else:
                user_guess+=event.unicode

    screen.fill(GRAY)#screencolor

    pygame.draw.rect(screen,GREEN,input_rect,2)
    pygame.draw.rect(screen,GREEN,output_rect)


    pygame.draw.circle(screen, GREEN,[rect_x,rect_y ],5)           # ANIMATION OF THE PROJECT
    pygame.draw.rect(screen,BLACK,[200,200,300,300],3)
    pygame.draw.line(screen, BLACK, [200, 295], [500, 295], 3)
    pygame.draw.line(screen, BLACK, [200, 395], [500, 395], 3)
    pygame.draw.line(screen, BLACK, [300, 200], [300, 500], 3)
    pygame.draw.line(screen, BLACK, [400, 200], [400, 500], 3)
    pygame.draw.rect(screen,BLACK,[195,238,13,20],2)
    pygame.draw.rect(screen,BLACK,[240,289,20,13],2)
    pygame.draw.rect(screen,BLACK,[294,240,13,20],2)
    pygame.draw.rect(screen,BLACK,[492,240,13,20],2)
    pygame.draw.rect(screen,BLACK,[492,440,13,20],2)
    pygame.draw.rect(screen,BLACK,[294,340,13,20],2)
    pygame.draw.rect(screen,BLACK,[294,440,13,20],2)
    pygame.draw.rect(screen,BLACK,[340,289,20,13],2)
    pygame.draw.rect(screen,BLACK,[440,289,20,13],2)
    pygame.draw.rect(screen,BLACK,[440,389,20,13],2)
    pygame.draw.rect(screen,BLACK,[340,389,20,13],2)
    pygame.draw.rect(screen,BLACK,[394,240,13,20],2)


    pygame.draw.rect(screen,WHITE,[500,397,68,100],3)
    pygame.draw.rect(screen,BLACK,[500,394,71,106],3)
    pygame.draw.rect(screen,WATERCOLOR,[503,400,65,94],35)  #swimming pool
    pygame.draw.rect(screen,BLACK,[503,410,15,75],10)
    pygame.draw.rect(screen,BLACK,[515,422,15,50],10)

    pygame.draw.rect(screen,BLACK,[497,200,71,98],3)
    pygame.draw.rect(screen,GREEN2,[500,203,65,92])

    pygame.draw.rect(screen,WHITE,[505,209,55,82],2)
    pygame.draw.line(screen,WHITE,[505,250],[559,250],2)
    pygame.draw.arc(screen, WHITE, [522,241,20,20],  PI/2,     PI, 2)
    pygame.draw.arc(screen, WHITE, [522,241,20,20],     0,   PI/2, 2)
    pygame.draw.arc(screen, WHITE,   [522,241,20,20],3*PI/2,   2*PI, 2)
    pygame.draw.arc(screen, WHITE,  [522,241,20,20],    PI, 3*PI/2, 2)
    pygame.draw.rect(screen,WHITE,[522,209,20,10],2)
    pygame.draw.rect(screen,WHITE,[515,209,35,18],2)
    pygame.draw.rect(screen,WHITE,[522,279,20,12],2)
    pygame.draw.rect(screen,WHITE,[515,273,35,18],2)
    pygame.draw.arc(screen, WHITE,   [520,217,25,20],3*PI/2,   2*PI, 2)
    pygame.draw.arc(screen, WHITE,  [520,217,25,20],    PI, 3*PI/2, 2)
    pygame.draw.arc(screen, WHITE, [520,263,25,20],  PI/2,     PI, 2)
    pygame.draw.arc(screen, WHITE, [520,263,25,20],     0,   PI/2, 2)


    pygame.draw.rect(screen,BLACK,[132,200,71,98])
    pygame.draw.rect(screen,NATURAL_DIRT,[135,203,65,92])
    pygame.draw.rect(screen,BLACK,[145,260,10,20])
    pygame.draw.rect(screen,CHOCOLATE,[140,240,20,20])
    pygame.draw.rect(screen,BLACK,[175,260,10,20])
    pygame.draw.rect(screen,CHOCOLATE,[170,240,20,20])



    pygame.draw.circle(screen, GREEN,[rect_x,rect_y ],5) #This is something which will move based on userinput


    font = pygame.font.SysFont('Calibri', 25, True, False) #Font sizes
    font1 = pygame.font.SysFont('Calibri', 30, True, False)
    keys = pygame.font.SysFont('Calibri', 15, True, False)
    base_fond=pygame.font.SysFont('Calibri',20,True, False)

    keyVariable=keys.render("Keys are here",True,BLACK)
    screen.blit(keyVariable, [212, 365])

    heading=font1.render("Which way would you like to go? ",True,BLACK)
    screen.blit(heading, [160, 60])


    userInput=  base_fond.render(user_guess,True,BLACK)    #Code for userInput
    screen.blit(userInput, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, userInput.get_width()+10)

    userOutput=  base_fond.render(Output,True,BLACK)   # Code of output after user gave input
    screen.blit(userOutput, (output_rect.x+5, output_rect.y+5))
    output_rect.w = max(680, userOutput.get_width()+10)

    text = font.render("0",True,BLACK)
    screen.blit(text, [220, 440])
    text1 = font.render("1",True,BLACK)
    screen.blit(text1, [320, 440])
    text2 = font.render("2",True,BLACK)
    screen.blit(text2, [420, 440])
    text3 = font.render("3",True,BLACK)
    screen.blit(text3, [220, 340])
    text4 = font.render("4",True,BLACK)
    screen.blit(text4, [320, 340])
    text5 = font.render("5",True,BLACK)
    screen.blit(text5, [420, 340])
    text6 = font.render("6",True,BLACK)
    screen.blit(text6, [220, 240])
    text7 = font.render("7",True,BLACK)
    screen.blit(text7, [320, 240])
    text8 = font.render("8",True,BLACK)
    screen.blit(text8, [420, 240])



    pygame.display.flip()
    clock.tick(60)


# Be IDLE friendly



    if Input.lower() =="north" or Input.lower() =="n": #if user input north then what will happen depend on situation and that controled by these code
        next_room=room_list[current_room][1]

        Output=""

        if next_room==None:
            rect_x= rect_x
            rect_y= rect_y
            Output= "Oops! There is no way to go.You are still in same room."

        elif  next_room==3 and key< 1  :  #this line mean if nextroom is 3 and key is 0 only then user will take an key
            key+=1
            current_room=next_room
            rect_x = 250
            rect_y = 350
            Output= room_list[current_room][0]

        elif next_room=="Swimming pool" or next_room=="Field" or next_room=="Garden" : # user can go outside only user has key to go
            if key>0 and key<=1:

               done=True
            else:

               Output="Without key,You are trying to go outside! Go and find a key"

               current_room=current_room
               rect_x= rect_x
               rect_y= rect_y

        else:

            current_room=next_room
            rect_x= rect_x
            rect_y= rect_y-100
            Output = room_list[current_room][0]


        user_guess=""    #make userguess and input empty
        Input=""


    elif Input.lower() =="east" or Input.lower() =="e":  #if user input east then what will happen depend on situation and that controled by these code
        next_room=room_list[current_room][2]

        Output=""

        if next_room==None:
            rect_x= rect_x
            rect_y= rect_y
            Output= "Oops! There is no way to go.You are still in same room."

        elif next_room==3 and key< 1  : #this line mean if nextroom is 3 and key is 0 only then user will take an key
            key+=1
            current_room=next_room
            rect_x = 250
            rect_y = 350
            Output= room_list[current_room][0]

        elif next_room=="Swimming pool" or next_room=="Field" or next_room=="Garden" :  # user can go outside only user has key to go
            if key>0 and key<=1:
               done=True
            else:
                Output="Without key,You are trying to go outside! Go and find a key"
                current_room=current_room

        else:
            current_room=next_room
            rect_x= rect_x+100
            rect_y= rect_y
            Output = room_list[current_room][0]

        user_guess=""   #make userguess and input empty
        Input=""


    elif Input.lower() =="west" or Input.lower() =="w":
        next_room=room_list[current_room][3]

        Output=""
        if next_room==None:
            rect_x= rect_x
            rect_y= rect_y
            Output= "Oops! There is no way to go.You are still in same room."

        elif next_room==3 and key< 1 :   #this line mean if nextroom is 3 and key is 0 only then user will take an key
            key+=1
            current_room=next_room
            rect_x = 250
            rect_y = 350
            Output= room_list[current_room][0]


        elif next_room=="Swimming pool" or next_room=="Field" or next_room=="Garden" :  # user can go outside only user has key to go
            if key>0 and key<=1:
              done=True
            else:
                Output="Without key,You are trying to go outside! Go and find a key"
                current_room=current_room

        else:
            current_room=next_room
            rect_x= rect_x-100
            rect_y= rect_y
            Output = room_list[current_room][0]

        user_guess=""  #make userguess and input empty
        Input=""


    elif Input.lower() =="south" or Input.lower() =="s":
        next_room=room_list[current_room][4]
        Output=""

        if next_room==None:
            rect_x= rect_x
            rect_y= rect_y
            Output= "Oops! There is no way to go.You are still in same room."


        elif next_room==3 and key< 1  :   #this line mean if nextroom is 3 and key is 0 only then user will take an key
            key+=1
            current_room=next_room

            rect_x = 250
            rect_y = 350
            Output=room_list[current_room][0]


        elif next_room=="Swimming pool" or next_room=="Field" or next_room=="Garden" :  # user can go outside only user has key to go
            if key>0 and key<=1:

               done=True
            else:
                Outpur="Without key,You are trying to go outside! Go and find a key"
                print()
                current_room=current_room
                print(room_list[current_room][0])

        else:
            current_room=next_room
            rect_x= rect_x
            rect_y= rect_y + 100

            Output=room_list[current_room][0]


        user_guess=""   #make userguess and input empty
        Input=""



pygame.quit()


#This part is for when game will stop or user will get out from house then these code will let us know where user is.

pygame.init()
size = (710, 710)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adventure game")

one = False
clock = pygame.time.Clock()

# Loop as long as one == False
while not one:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            one = True  # Flag that we are done so we exit this loop

    screen.fill(GRAY)

    new_fond=pygame.font.SysFont('Calibri',25,True, False)

    if next_room=="Swimming pool"  and key>0 or next_room=="Field" and key>0 or next_room=="Garden" and key>0 :
        out1 = new_fond.render(f"Congratulations Buddy! You are in {next_room}.",True,CHOCOLATE)
        screen.blit(out1, [130, 300])
        out2 = new_fond.render("Game is over. Thanks for being participate",True,CHOCOLATE)
        screen.blit(out2, [130, 335])
        out3 = new_fond.render("Press Quit to stop the game",True,CHOCOLATE)
        screen.blit(out3, [130, 370])


    elif next_room=="Swimming pool"  and key<=0 or next_room=="Field" and key<=0 or next_room=="Garden" and key<=0 :
        out1 = new_fond.render(f"You are in room {current_room}.",True,CHOCOLATE)
        screen.blit(out1, [130, 300])
        out2 = new_fond.render("Sorry! You have exited from middle of the game! ",True,CHOCOLATE)
        screen.blit(out2, [130, 335])
        out3 = new_fond.render("Press Quit to stop the game.",True,CHOCOLATE)
        screen.blit(out3, [130, 370])




    elif next_room==0 or next_room==1 or next_room==2 or next_room==3 or next_room==4 or next_room==5 or next_room==6 or next_room==7 or next_room==8 or next_room==None:
        if next_room==None:
            out5 = new_fond.render(f"You are in room {current_room}.",True,CHOCOLATE)
            screen.blit(out5, [130, 300])
            out6 = new_fond.render("Sorry! You have exited from middle of the game! ",True,CHOCOLATE)
            screen.blit(out6, [130, 335])
            out7 = new_fond.render("Press Quit to stop the game.",True,CHOCOLATE)
            screen.blit(out7, [130, 370])


        else:
            out5 = new_fond.render(f"You are in room {next_room}.",True,CHOCOLATE)
            screen.blit(out5, [130, 300])
            out6 = new_fond.render("Sorry! You have exited from middle of the game! ",True,CHOCOLATE)
            screen.blit(out6, [130, 335])
            out7 = new_fond.render("Press Quit to stop the game.",True,CHOCOLATE)
            screen.blit(out7, [130, 370])



    else:
        out8 = new_fond.render("Sorry! You didn't play the game.",True,CHOCOLATE)
        screen.blit(out8, [190, 350])



    pygame.display.flip()
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
