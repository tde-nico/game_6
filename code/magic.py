from re import X
import pygame
from settings import *
from random import randint


class MagicPlayer:
	def __init__(self, animation_player):
		self.animation_player = animation_player


	def heal(self, player, strength, cost, groups):
		if player.energy < cost:
			return
		player.energy -= cost
		player.health += strength
		if player.health > player.stats['health']:
			player.health = player.stats['health']
		self.animation_player.create_particles('aura', player.rect.center, groups)
		self.animation_player.create_particles('heal',
			player.rect.center + pygame.math.Vector2(0,-20), groups)


	def flame(self, player, cost, groups):
		if player.energy < cost:
			return
		player.energy -= cost
		status = player.status.split('_')[0]
		if status == 'right':
			direction = pygame.math.Vector2(1,0)
		elif status == 'left':
			direction = pygame.math.Vector2(-1,0)
		elif status == 'up':
			direction = pygame.math.Vector2(0,-1)
		else:
			direction = pygame.math.Vector2(0,1)
		for i in range(1,6):
			if direction.x:
				offset_x = TILESIZE * direction.x * i
				x = player.rect.centerx + offset_x + randint(-TILESIZE//3, TILESIZE//3)
				y = player.rect.centery + randint(-TILESIZE//3, TILESIZE//3)
				self.animation_player.create_particles('flame', (x,y), groups)
			else:
				offset_y = TILESIZE * direction.y * i
				x = player.rect.centerx
				y = player.rect.centery + offset_y
				self.animation_player.create_particles('flame', (x,y), groups)
			

