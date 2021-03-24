import pygame
pygame.init()

height = 800
screen = pygame.display.set_mode((720, height))
running = True

#colours
red = (255, 0, 0)
green = (0, 170, 0)
blue = (0, 0, 255)
orange = (200, 145, 0)
magenta = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (140, 140, 140)
cyan = (0, 255, 255)
yellow = (255, 255, 0)

#stick figure
stickWidth = 5
x, y = 209, 550
armSpeed = 2

#projectile
speed = 15
px, py = 720, 375

while running:
	screen.fill(white)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#ground
	pygame.draw.line(screen, black, (0, height), (720, height), stickWidth)
	
	#stick figure
	#head
	pygame.draw.circle(screen, black, (150, 300), 55)
	pygame.draw.circle(screen, white, (150, 300), 55-stickWidth)
	
	#body
	pygame.draw.line(screen, black, (150, 350), (150, 600), stickWidth)
	
	#legs
	pygame.draw.line(screen, black, (150, 600), (200, 670), stickWidth)
	pygame.draw.line(screen, black, (200, 670), (230, 800), stickWidth)
	
	pygame.draw.line(screen, black, (150, 600), (140, 670), stickWidth)
	pygame.draw.line(screen, black, (140, 670), (110, 800), stickWidth)
	
	#right arm
	pygame.draw.line(screen, black, (150, 380), (120, 450), stickWidth)
	pygame.draw.line(screen, black, (120, 450), (90, 550), stickWidth)
	
	#left arm
	pygame.draw.line(screen, black, (150, 380), (180, 450), stickWidth)
	pygame.draw.line(screen, black, (180, 450), (x, y), stickWidth)
	
	if y >= 380:
		x += armSpeed
		y -= armSpeed*4
		
	#projectile
	pygame.draw.line(screen, black, (px, py), (px+70, py), stickWidth)
	if px >= 220:
		px -= speed

	pygame.display.flip()

pygame.quit()
