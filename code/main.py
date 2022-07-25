import pygame, sys
from settings import *
from debug import debug
from level import Level

# 6 26 35
# 7 24 26

class Game: # 6 43 10
	def __init__(self):
		pygame.init()
		self.screen=pygame.display.set_mode((WIDTH,HEIGTH))
		self.clock=pygame.time.Clock()
		pygame.display.set_caption('game_6')
		self.level = Level()


	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
					elif event.key == pygame.K_m:
						self.level.toggle_menu()
					

			self.screen.fill('black')
			if self.level.run():
				break
			pygame.display.update()
			self.clock.tick(FPS)



if __name__ == '__main__':
	while True:
		game = Game()
		game.run()
