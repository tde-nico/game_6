from unicodedata import name
from pandas import value_counts
import pygame
from settings import *


class Upgrade:
	def __init__(self, player):
		self.display_surface = pygame.display.get_surface()
		self.player = player
		self.attribute_nbr = len(player.stats)
		self.attribute_names = list(player.stats.keys())
		self.max_values = list(player.max_stats.values())
		self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

		self.height = self.display_surface.get_size()[1] * 0.8
		self.width = self.display_surface.get_size()[0] // (self.attribute_nbr+1)
		self.create_items()

		self.selection_index = 0
		self.selection_time = None
		self.can_move = True
		self.selection_cooldown = 150


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


	def create_items(self):
		self.item_list = []
		for item in range(self.attribute_nbr):
			full_width = self.display_surface.get_size()[0]
			increment = full_width // self.attribute_nbr
			left = (item * increment) + (increment - self.width) // 2
			top = self.display_surface.get_size()[1] * 0.1
			item = Item(left, top, self.width, self.height, item, self.font)
			self.item_list.append(item)


	def display(self):
		self.input()
		self.cooldowns()
		for index, item in enumerate(self.item_list):
			name = self.attribute_names[index]
			value = self.player.get_value_by_index(index)
			max_value = self.max_values[index]
			cost = self.player.get_cost_by_index(index)
			item.display(self.display_surface,
				self.selection_index, name, value, max_value, cost)



class Item:
	def __init__(self, l, t, w, h, index, font):
		self.rect = pygame.Rect(l,t,w,h)
		self.index = index
		self.font = font


	def display_names(self, surface, name, cost, selected):
		color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR
		title_surf = self.font.render(name, False, color)
		title_rect = title_surf.get_rect(
			midtop = self.rect.midtop + pygame.math.Vector2(0,20))
		cost_surf = self.font.render(f'{int(cost)}', False, color)
		cost_rect = cost_surf.get_rect(
			midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))
		surface.blit(title_surf, title_rect)
		surface.blit(cost_surf, cost_rect)


	def display_bar(self, surface, value, max_value, selected):
		top = self.rect.midtop + pygame.math.Vector2(0,60)
		bottom = self.rect.midbottom - pygame.math.Vector2(0,60)
		color = BAR_COLOR_SELECTED if selected else BAR_COLOR
		full_height = bottom[1] - top[1]
		realtive_number = (value / max_value) * full_height
		value_rect = pygame.Rect(top[0] - 15, bottom[1] - realtive_number, 30,10)
		pygame.draw.line(surface, color, top, bottom, 5)
		pygame.draw.rect(surface, color, value_rect)


	def display(self, surface, selection_num, name, value, max_value, cost):
		selected = self.index == selection_num
		if selected:
			pygame.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
			pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
		else:
			pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
			pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
		self.display_names(surface, name, cost, selected)
		self.display_bar(surface, value, max_value, selected)

