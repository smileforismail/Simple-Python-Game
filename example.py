# Imports a game library that lets you use specific functions in your program.
# Import random to generate random numbers.

import pygame
import random

# Initialize the pygame modules to get everything started.
pygame.init()

# set up the main windows height and width
screen_width = 1500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# This creates the player and the three enemies.And gives it the image found in this folder.

player = pygame.image.load('image.png')
enemy1 = pygame.image.load('hamza1.jpg')
enemy2 = pygame.image.load('hamza2.jpg')
enemy3 = pygame.image.load('nadim.png')
prize = pygame.image.load('prize.jpg')

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player, the enemy and the prize as variables so that you can change them later.

playerXPosition = 100
playerYPosition = 50

# Make the enemy and prize start off screen and at a random y position.

enemy1XPosition = screen_width + screen_height
enemy1YPosition = 300
enemy2XPosition = screen_width  
enemy2YPosition = 100
enemy3XPosition = screen_width + screen_width
enemy3YPosition = 600
prizeXPosition = screen_width + screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False.
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to
# represent real time game play.

# This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting).
while 1:

    screen.fill(0)  # Clears the screen.
    # This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.

    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.

        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True

        # This event checks if the key is up(i.e. not pressed by the user).

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.
    # however, not certain on how to prevent the player from moving out of the display window from the left and right side

    if keyLeft == True:
        playerXPosition -= 1

    if keyRight == True:
        playerXPosition += 1

    if keyUp == True:
        # This makes sure that the user does not move the player above the window.
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        # This makes sure that the user does not move the player below the window.
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:

    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemy and the prize:

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the boxes:
    # Display losing status to the user if the user collides with the enemy boxes
    # than Quite game and exit window:

    # pygame.quit()
    # exit(0)
    if playerBox.colliderect(enemy1Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    if playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    if playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)

               

     # If the enemy is off the screen the user wins the game and if the user collides with the 
     # prize box, they win the game aswell.
     # Display wining status to the user:

    if enemy3XPosition < 0 - enemy1_width:
        print("You win!")
        pygame.quit()

        exit(0)
        
    if playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit()
        exit(0)
    
        # Quite game and exit window:
        pygame.quit()

        exit(0)

    # Make enemy and prize approach the player.

    enemy1XPosition -= 2.5
    enemy2XPosition -= 2.5
    enemy3XPosition -= 2.5
    prizeXPosition -= 2.5
    # ================The game loop logic ends here. =============
    
