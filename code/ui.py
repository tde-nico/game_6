import pygame
from settings import *


class UI:
	def __init__(self):
		self.display_surf = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
		self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)
		self.weapon_graphics = [
			pygame.image.load(weapon['graphic']).convert_alpha()
			for weapon in weapon_data.values()
		]
		self.magic_graphics = [
			pygame.image.load(magic['graphic']).convert_alpha()
			for magic in magic_data.values()
		]


	def show_bar(self, current, max_amount, bg_rect, color):
		pygame.draw.rect(self.display_surf, UI_BG_COLOR, bg_rect)
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = int(current_width)
		pygame.draw.rect(self.display_surf, color, current_rect)
		pygame.draw.rect(self.display_surf, UI_BORDER_COLOR, bg_rect, 3)


	def show_exp(self, exp):
		text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
		x, y = self.display_surf.get_size()
		x -= 20
		y -= 20
		text_rect = text_surf.get_rect(bottomright=(x,y))
		pygame.draw.rect(self.display_surf, UI_BG_COLOR, text_rect.inflate(15,15))
		self.display_surf.blit(text_surf, text_rect)
		pygame.draw.rect(self.display_surf, UI_BORDER_COLOR, text_rect.inflate(15,15), 3)


	def selection_box(self, left, top, has_switched):
		bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surf, UI_BG_COLOR, bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surf, UI_BORDER_COLOR, bg_rect, 3)
		else:
			pygame.draw.rect(self.display_surf, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
		return bg_rect


	def weapon_overlay(self, weapon_index, has_switched):
		bg_rect = self.selection_box(10, self.display_surf.get_height()-ITEM_BOX_SIZE-10, has_switched)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center=bg_rect.center)
		self.display_surf.blit(weapon_surf, weapon_rect)
	

	def magic_overlay(self, magic_index, has_switched):
		bg_rect = self.selection_box(80, self.display_surf.get_height()-ITEM_BOX_SIZE-5, has_switched)
		magic_surf = self.magic_graphics[magic_index]
		magic_rect = magic_surf.get_rect(center=bg_rect.center)
		self.display_surf.blit(magic_surf, magic_rect)


	def display(self, player):
		self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
		self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
		self.show_exp(player.exp)
		self.weapon_overlay(player.weapon_index, player.can_switch_weapon)
		self.magic_overlay(player.magic_index, player.can_switch_magic)
