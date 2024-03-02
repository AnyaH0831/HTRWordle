import pygame
from pygame.rect import Rect
import math
import random

pygame.init()

SIZE = width, height = (800, 600)
screen = pygame.display.set_mode(SIZE)
titleFont = pygame.font.SysFont("Times New Roman", 30) # times size 30
LinguleFont = pygame.font.SysFont("Times New Roman", 60, True) # times size 30

# sets color values

# normal colors
RED = (255, 0, 0)
WHT = (255, 255, 255)
RED = (255, 0, 0) 
GRN = (0, 255, 0)
BLU = (0, 0, 255)
WHT = (255, 255, 255)
BLK = (0, 0, 0)
GRY = (75, 75, 75)
BRW = (92, 54, 10)
YLW = (255, 255, 0)
ORA = (255, 165, 0)
PUR = (227, 185, 255)

# house-paint like colors
HBEI = (244, 232, 210)
HRED = (255, 119, 107)
HDRED = (214, 100, 90)
HBRW = (176, 165, 144)

# dark colors
DBLU = (4, 115, 130)
DBRW = (200, 137, 101)
DGRN = (46, 112, 45)
VDGRN = (37, 89, 42)

# light colors
LGRY = (160, 160, 160)
LBLU = (227, 251, 255)
LBRW = (201, 180, 155)
LYLW = (255, 255, 171)
LPNK = (252, 177, 172)
LPUR = (235, 223, 247)
LGRN = (237, 255, 245)

# special colors
SBLU = (166, 200, 255)
SGRN = (82, 219, 79)
PGRN = (193, 225, 193)
JGRN = (0, 163, 108)
WBLU = (133, 231, 255)
NBLU = (2, 9, 33)

# initializes images

running = True
myClock = pygame.time.Clock()
mx = my = 0
backgroundX = 0

#files
frWords = []
frEnWords = []
spWords = []
spEnWords = []
frFile = open("French.txt", "r")
frEnFile = open("French English.txt", "r")
spFile = open("Spanish.txt", "r")
spEnFile = open("Spanish English.txt", "r")

for line in frFile:
  line = line.strip()
  frWords.append(line)

for line in frEnFile:
  line = line.strip()
  frEnWords.append(line)

for line in spFile:
  line = line.strip()
  spWords.append(line)

for line in spEnFile:
  line = line.strip()
  spEnWords.append(line)

frFile.close()
frEnFile.close()
spFile.close()
spEnFile.close()

# checks if the state for the buttons at the menu should change
def answerPrompt(isItTrue, stateOri, statesy):
    states = stateOri # state becomes equal to the original/previous state

    if isItTrue == True: # checks if there is a state change from button click of function "drawButtons"
        states = statesy # changes state to new state

    return states

# draws the title


# draws buttons for menu screen
def drawButtons(screen, button, mx, my, prompt, xButton, yButton, states): 
    prompt = str(prompt) # what the button will say
    stateChange = False # if the button is clicked and causes a state change

    r = Rect(xButton, yButton, 300, 75) # button dimensions

    # finds the formatting to fit text in the middle
    textWidth, textHeight = titleFont.size(prompt)  # takes height and width of text 
    inX = ((300 - textWidth))//2 + xButton # finds middle x from size
    inY = ((75 - textHeight)//2) + yButton # finds middle y from size
    text = titleFont.render(prompt, 1, BLK)	 #string, 1, colour - keep as 1

    # changes colors if mouse is over button
    if r.collidepoint(mx, my) == True:
        # draws button
        pygame.draw.rect(screen, PGRN, r) 
        pygame.draw.rect(screen, BLK, r, 10) 
        pygame.draw.rect(screen, WHT, r, 5)
        pygame.draw.rect(screen, BLK, r, 2)
        screen.blit(text, (inX, inY-2, textWidth, textHeight))	#rectangle represents where the text will be
        if button == 1: #check for button down
            return states

    else:
        # draws button (normally, no mouse over)
        pygame.draw.rect(screen, WHT, r)
        pygame.draw.rect(screen, BLK, r, 2)
        screen.blit(text, (inX, inY, textWidth, textHeight))	#rectangle represents where the text will be

    return stateChange # returns True if state should change and False if not

# draws home button at top right of screen to bring user to menu


def drawSquare():

  for i in range(5):
    for j in range(6):
      pygame.draw.rect(screen,WHT,(50*i+250,50*j + 125,50,50),2)

choice = "fr"

def drawGame(button, word):
  global state, keyCharact, keyCharact1, keyCode, userInput, y
  screen.fill(DBLU)
  
  if keyDown == True:  #there's a user input
    if keyCode == 8 and keyCharact != []: #delete one character when the user delete
      keyCharact = keyCharact[:-3]
      keyCharact1 = keyCharact1[:-1]

    elif (39<=keyCode<=122 or keyCode == 32) and len(userInput) <=16: 
      keyCharact += keys + "   " #add the character
      keyCharact1 += keys #add the character

  userInput = str(keyCharact)
  userInput1 = str(keyCharact1).upper()
  

  word1 = titleFont.render(userInput.upper(),1,WHT)

  screen.blit(word1,(262,135+50*y))  

  
  if len(userInput1) == 5:
    
    if (userInput1 == word):
      state = STATE_END
    else:
      y+=1
      userInput1 = ""
      userInput = ""
      keyCharact = ""
      keyCharact1 = ""
  

  
  # if button is clicked, switches to english

    
  drawSquare()

  return state

def drawEND(button, word, newWord):
  global state
  screen.fill(DBLU)

  text = "The word " + word + " means "
  text2 = titleFont.render(text,1,WHT)
  screen.blit(text2,(200,135,100,100))
  text = newWord + " in English."
  text2 = titleFont.render(text,1,WHT)
  screen.blit(text2,(200,250,100,100))
  
  return state

STATE_GAME = 2
STATE_END = 3

state = STATE_GAME
keyDown = False
userInput = ""
keyCharact = ""
keyCharact1 = ""

# chooses a random word
if (choice == "fr"): 
  word = random.choice(frWords)
  num = frWords.index(word)
  newWord = frEnWords[num]

elif (choice == "sp"):
  word = random.choice(spWords)
  num = spWords.index(word)
  newWord = spEnWords[num]

y=0
while running:
  keyDown = False
  button = 0 # resets the button
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      keys = event.unicode  #keys detection
      keyCode = event.key

      keyDown = True

      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_TAB:
        state = STATE_GAME

    if event.type == pygame.MOUSEBUTTONDOWN:
      mx, my = pygame.mouse.get_pos()
      button = event.button

    elif event.type == pygame.MOUSEMOTION: # checks mouse movement
      mx, my = event.pos # grabs mouse movement
  
  if state == STATE_GAME:
    state = drawGame(button, word)

    
  elif state == STATE_END:
    state = drawEND(button, word, newWord)


  pygame.display.flip()
  myClock.tick(60)

pygame.quit()