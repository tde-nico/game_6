import pygame, sys
from settings import *
from level import Level


class Game:
	def __init__(self):
		pygame.init()
		self.screen=pygame.display.set_mode((WIDTH,HEIGTH))
		self.clock=pygame.time.Clock()
		pygame.display.set_caption('game_6')
		self.level = Level()
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)


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
					

			self.screen.fill(WATER_COLOR)
			if self.level.run():
				break
			pygame.display.update()
			self.clock.tick(FPS)



if __name__ == '__main__':
	while True:
		game = Game()
		game.run()
