import random
import pygame


class Snake:
	cor = (0,255,0)
	tamanho = (10, 10)
	tamanho_maximo = 49 * 49

	def __init__(self):
		self.textura = pygame.Surface(self.tamanho)
		self.textura.fill(self.cor)
		self.corpo = [(100,100), (90,100), (80,100)]
		self.direcao = 'direita'
		self.pontos = 0
		self.velocidade = 10


	def blit(self, screen):
		for posicao in cobrinha.corpo:
			screen.blit(cobrinha.textura, posicao)


	def andar(self):
		cabeca = self.corpo[0]
		x = cabeca[0]
		y = cabeca[1]
		if self.direcao == 'direita':
			self.corpo.insert(0, (x + 10, y))
		elif self.direcao == 'esquerda':
			self.corpo.insert(0, (x - 10, y))
		elif self.direcao == 'cima':
			self.corpo.insert(0, (x, y - 10))
		elif self.direcao == 'baixo':
			self.corpo.insert(0, (x, y + 10))	
		self.corpo.pop(-1)

	
	def cima(self):
		if self.direcao != 'baixo':
			self.direcao = 'cima'


	def baixo(self):
		if self.direcao != 'cima':
			self.direcao = 'baixo'


	def direita(self):
		if self.direcao != 'esquerda':
			self.direcao = 'direita'


	def esquerda(self):
		if self.direcao != 'direita':
			self.direcao = 'esquerda'


	def colisao_frutinha(self, frutinha):
		return self.corpo[0] == frutinha.posicao

	def comer(self):
		self.corpo.append((700, 700))
		self.pontos += 1
		pygame.display.set_caption('Snake | Pontos : {}'.format(self.pontos))


	def colisao_de_morte(self):
		cabeca = self.corpo[0]
		x = cabeca[0]
		y = cabeca[1]
		corpo = self.corpo[1:]

		return x < 0 or y < 0 or x > 490 or y > 490 or cabeca in corpo or len(self.corpo) > self.tamanho_maximo


	def dificuldade(self):
		if self.pontos >= 5:
			self.velocidade += 1
		elif self.pontos >=10:
			self.velocidade += 1
		elif self.pontos >=15:
			self.velocidade += 1
		elif self.pontos >=20:
			self.velocidade += 1
		elif self.pontos >=25:
			self.velocidade += 1
		elif self.pontos >=30:
			self.velocidade += 1
		elif self.pontos >=35:
			self.velocidade += 1
		elif self.pontos >=40:
			self.velocidade += 1
		elif self.pontos >=45:
			self.velocidade += 1
		elif self.pontos >=50:
			self.velocidade += 1


class Frutinha:
	cor = (255,0,0)
	tamanho = (10, 10)


	def __init__(self, cobrinha):
		self.textura = pygame.Surface(self.tamanho)
		self.textura.fill(self.cor)
		self.posicao = Frutinha.criar_posicao(cobrinha)

	@staticmethod
	def criar_posicao(cobrinha):
		x = random.randint(0,49) * 10
		y = random.randint(0,49) * 10
		while (x , y) in cobrinha.corpo:
			frutinha.criar_posicao(cobrinha)
		return x, y


	def blit(self, screen):
			screen.blit(frutinha.textura, frutinha.posicao)
			

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
			pygame.display.set_caption('Snake')

		cobrinha.andar()
		screen.fill(preto)
		try:
			frutinha.blit(screen)
		except:
			frutinha.blit(screen)
		cobrinha.blit(screen)
		pygame.display.update()
			
