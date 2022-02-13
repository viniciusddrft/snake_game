import random
import pygame
from classes.snake import Snake
from classes.frutinha import Frutinha

if __name__ == "__main__":
	pygame.init()

	resolucao = (500, 500)
	screen = pygame.display.set_mode(resolucao)
	pygame.display.set_caption('Snake')
	clock = pygame.time.Clock()
	preto = (0, 0, 0)

	cobrinha = Snake()
	frutinha = Frutinha(cobrinha)

	while True:
		clock.tick(cobrinha.velocidade)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					cobrinha.cima()
					break
				elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
					cobrinha.baixo()
					break
				elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
					cobrinha.esquerda()
					break
				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					cobrinha.direita()
					break

		

		if cobrinha.colisao_frutinha(frutinha):
			cobrinha.comer()
			cobrinha.dificuldade()
			frutinha = Frutinha(cobrinha)

		if cobrinha.colisao_de_morte():
			cobrinha = Snake()
			frutinha = Frutinha(cobrinha)
			pygame.display.set_caption('Snake')

		cobrinha.andar()
		screen.fill(preto)
		try:
			frutinha.blit(screen)
		except:
			frutinha.blit(screen)
		cobrinha.blit(screen)
		pygame.display.update()
			
