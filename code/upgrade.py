import pygame
from settings import *


class Upgrade:
	def __init__(self, player):
		self.display_surface = pygame.display.get_surface()
		self.player = player
		self.attribute_nbr = len(self.player.stats)
		self.attribute_names = list(self.player.stats.keys())
		self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

		self.selection_index = 0
		self.selection_time = None
		self.can_move = True
		self.selection_cooldown = 300


	def input(self):
		keys = pygame.key.get_pressed()

		if self.can_move:
			if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and \
				self.selection_index < self.attribute_nbr - 1:
				self.selection_index += 1
				self.can_move = False
				self.selection_time = pygame.time.get_ticks()
			elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and \
				self.selection_index >= 1:
				self.selection_index -= 1
				self.can_move = False
				self.selection_time = pygame.time.get_ticks()

			if keys[pygame.K_SPACE]:
				self.can_move = False
				self.selection_time = pygame.time.get_ticks()


	def cooldowns(self):
		if self.can_move:
			return
		current_time = pygame.time.get_ticks()
		if current_time - self.selection_time >= self.selection_cooldown:
			self.can_move = True


	def display(self):
		self.input()
		self.cooldowns()

