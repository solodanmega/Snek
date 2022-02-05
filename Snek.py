#SNEK
#CODED BY DUSKPROGRAMMER
import pygame, sys, random
from pygame.locals import *

#SET YOUR DEFAULT SETTINGS
boardxtiles = 40#int(input('x:'))
boardytiles = 12#int(input('y:'))
tickspe = 10#int(input('speed:'))
colorscheme = '2'#'0'


while colorscheme != '1' and colorscheme != '2':
  colorscheme = input('clrschm (1:rainbow, 2:terraocean)')

pygame.init()
mainClock = pygame.time.Clock()

#define window
WINH = (boardytiles + 2) * 32 
WINW = boardxtiles * 32
WinSurf = pygame.display.set_mode((WINW,WINH),0,32)
pygame.display.set_caption('Snek')

#define colors
WHITE = (255,255,255)
GRAY = (50,50,50)
BLACK = (0,0,0)
#RED = (255,0,0)
#GREEN = (0,255,0)
colist = []

if int(colorscheme) == 1:
  modu = 30
  for i in range(5):
    colist.append((255,51*i,0))
  for i in range(5):
    colist.append((255-51*i,255,0))

  for i in range(5):
    colist.append((0,255,51*i))
  for i in range(5):
    colist.append((0,255-51*i,255))

  for i in range(5):
    colist.append((51*i,0,255))
  for i in range(5):
    colist.append((255,0,255-51*i))
elif int(colorscheme) == 2:
  modu = 20
  for i in range(5):
    colist.append((0,255,51*i))
  for i in range(5):
    colist.append((0,255-51*i,255))
  for i in range(5):
    colist.append((0,51*i,255))
  for i in range(5):
    colist.append((0,255,255-51*i))

WinSurf.fill(GRAY)

board = []
snek = [(0,0)]
directshun = 0
apol = (1,0)
score = 0

#generates board
for i in range(boardxtiles):
  templist = []
  for j in range(boardytiles):
    templist.append(pygame.Rect((i*32 + 2), (j*32 + 2), 28, 28))
  board.append(templist)

def change_apol():
  global apol
  global score
  score += 1
  while apol in snek:
    apol = (random.randint(0,boardxtiles-1),random.randint(0,boardytiles-1))

def death(methd):
  print()
  if methd == 0:
    print(random.choice(['Coward!','Where are u running','Y are u running','BOO!!!']))
  elif methd == 1:
    print(random.choice(['Watch where ya going!','WALL','lmao u died','imagine crashing into a wall','stoopid']))
  elif methd == 2:
    print(random.choice(['BUTT','A$$',"step'd on ya own tail",'lmfao u died','does your tail taste good?','APOL']))
  print('score:',score)
  pygame.quit()
  sys.exit()

basicFont = pygame.font.SysFont(None, 48)

#main loop
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      death(0)
    if event.type == KEYDOWN:
      if (event.key == K_UP or event.key == K_w) and directshun != 1:
        directshun = 3
      elif (event.key == K_LEFT or event.key == K_a) and directshun != 0:
        directshun = 2
      elif (event.key == K_DOWN or event.key == K_s) and directshun != 3:
        directshun = 1
      elif (event.key == K_RIGHT or event.key == K_d) and directshun != 2:
        directshun = 0
    
    if event.type == KEYUP:
      if event.key == K_ESCAPE:
        death(0)
  

  #main conditional statement
  if snek[0][0] == 0 and directshun == 2 or snek[0][0] == boardxtiles-1 and directshun == 0 or snek[0][1] == 0 and directshun == 3 or snek[0][1] == boardytiles-1 and directshun == 1:
    death(1)

  elif directshun == 0:
    if (snek[0][0]+1,snek[0][1]) == apol:
      snek.insert(0, apol)
      change_apol()

    elif (snek[0][0]+1,snek[0][1]) in snek:
      death(2)

    else:
      snek.insert(0, (snek[0][0]+1,snek[0][1]))
      snek.remove(snek[-1])

  elif directshun == 1:
    if (snek[0][0],snek[0][1]+1) == apol:
      snek.insert(0, apol)
      change_apol()

    elif (snek[0][0],snek[0][1]+1) in snek:
      death(2)

    else:
      snek.insert(0, (snek[0][0],snek[0][1]+1))
      snek.remove(snek[-1])

  elif directshun == 2:
    if (snek[0][0]-1,snek[0][1]) == apol:
      snek.insert(0, apol)
      change_apol()

    elif (snek[0][0]-1,snek[0][1]) in snek:
      death(2)
    else:
      snek.insert(0, (snek[0][0]-1,snek[0][1]))
      snek.remove(snek[-1])

  elif directshun == 3:
    if (snek[0][0],snek[0][1]-1) == apol:
      snek.insert(0, apol)
      change_apol()

    elif (snek[0][0],snek[0][1]-1) in snek:
      death(2)
    else:
      snek.insert(0, (snek[0][0],snek[0][1]-1))
      snek.remove(snek[-1])
  
  WinSurf.fill(GRAY)

  for xtiles in board:
    tilex = board.index(xtiles)
    for tile in xtiles:
      tiley = xtiles.index(tile)
      if (tilex,tiley) in snek:
        pygame.draw.rect(WinSurf, colist[snek.index((tilex,tiley))% modu], tile)
      elif (tilex,tiley) == apol:
        pygame.draw.rect(WinSurf, WHITE, tile)
      else:
        pygame.draw.rect(WinSurf, BLACK, tile)
  
  text = basicFont.render(str(score), True, WHITE)
  textRect = text.get_rect()
  textRect.centerx = WINW/2
  textRect.centery = WINH - 32
  WinSurf.blit(text,textRect)

  pygame.display.update()
  mainClock.tick(tickspe)
