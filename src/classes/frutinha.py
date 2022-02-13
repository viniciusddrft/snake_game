import random
import pygame

class Frutinha:
	cor = (255,0,0)
	tamanho = (10, 10)

	def __init__(self, cobrinha):
		self.textura = pygame.Surface(self.tamanho)
		self.textura.fill(self.cor)
		self.posicao = Frutinha.criar_posicao(self, cobrinha)

	def criar_posicao(self, cobrinha):
		x = random.randint(0,49) * 10
		y = random.randint(0,49) * 10
		while (x , y or (x-10), (y-10) or  (x+10), (y+10)) in cobrinha.corpo:
			self.criar_posicao(cobrinha)
		return x, y

	def blit(self, screen):
			screen.blit(self.textura, self.posicao)
		