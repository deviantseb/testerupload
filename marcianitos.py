import pygame
import time
pygame.init()
clock = pygame.time.Clock()
disp_w = 800
disp_h = 600
pygame.display.set_caption("Marcianitos")
gameDisplay = pygame.display.set_mode((disp_w, disp_h))
spaceShip = pygame.image.load("spaceship.png")
alienShip = pygame.image.load("alien.png")
def titleScreen():
	fontName = pygame.font.SysFont(None, 50)
	textName = fontName.render("Marcianitos!", True, ((23, 75, 245)))
	gameDisplay.blit(textName, (300, 100))
#def alienSwarm(alien_x, alien_y):
def gameRun():
	x = 400
	y = 500
	moveX = 0
	alien_x = 50
	alien_y = 50
	alien_move = +5
	runningGame = True
	gameDisplay.blit(spaceShip, (x, y))
	gameDisplay.blit(alienShip, (alien_x, alien_y))
	while runningGame:
		gameDisplay.fill((255, 215, 0))
		titleScreen()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runningGame = False
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
				moveX = -5
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
				moveX = +5
			elif event.type == pygame.KEYUP:
				moveX = 0
		x = x + moveX
		if x < 0:
			x = 0
		elif x + 100 > disp_w:
			x = disp_w - 100
		alien_x = alien_x + alien_move
		if alien_x + 100 > 600:
			alien_move = -5
		elif alien_x < 0:
			alien_move = +5

		gameDisplay.blit(alienShip, (alien_x, alien_y))
		gameDisplay.blit(spaceShip, (x, y))
		clock.tick(30)
		pygame.display.flip()
gameRun()
pygame.quit()