import pygame

pygame.init()
relogio = pygame.time.Clock()

tamanho = (1280, 720)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Homeless Walker")
dt = 0

#Carrega a fonte a ser usada no jogo 
fontTempo = pygame.font.Font("asents/Fonts/EnergyStation/EnergyStation.ttf", 80)

# Carrega a spritesheet para nosso projeto
folhaSpritesIdle = pygame.image.load("assets/Homeless_1/Idle_2.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()
folhaSpritesJump = pygame.image.load("assets/Homeless_1/Jump.png").convert_alpha()
folhaSpritRunn = pygame.image.load("assets/Homelles_1/Run.png").convert_alpha()

# Define os frames
listFramesIdle = []
listFramesWalk = []
listFramesJump = []
listFramesRunn = []

# Cria os frames do personagem na lista de listFramesIdle
for i in range(11):
    # Pega um frame da folha de sprites na posição i * 0, 0 com tamanho 128x128
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)

    # Redimensiona o frame para 2 vezes o tamanho original
    frame = pygame.transform.scale2x(frame)

    # Adiciona o frame na lista de listFramesIdle
    listFramesIdle.append(frame)

for i in range(8):
    frame = folhaSpritesWalk.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesWalk.append(frame)

for i in range(8):
    frame = folhaSpritRunn.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesRunn.append(frame)

for i in range(9):
    frame = folhaSpritesJump.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesJump.append(frame)

# Variaveis da animação do personagem parado
indexFrameIdle = 0 # Controla qual imagem está sendo mostrada na tela
tempoAnimacaoIdle = 0.0 # Controla quanto tempo se passou desde a última troca de frame
velocidadeAnimacaoIdle = 5 # Controlar o tempo de animação em relação ao tempo real (1 / velocidadeAnimacaoIdle)

# Variaveis da animação do personagem andando
indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

# Variaveis da animação do personagem pulando
indexFrameJump = 0
tempoAnimacaoJump = 0.0
velocidadeAnimacaoJump = 5

# Variavéis da animação do personagem correndo
indexFrameRunn = 0
tempoAnimacaoRunn = 0.0
velocidadeAnimacaoRunn = 10

# Retangulo do personagem na tela para melhor controle e posicionamento do personagem
personagemRect = listFramesIdle[0].get_rect(midbottom=(250, 480))

gravidade = 1 # Gravidade do jogo, valor que aumenta a cada frame
direcaoPersonagem = 1 # Direção que o personagem está olhando (1 = Direita, -1 = Esquerda)
estaAndando = False # Define se o personagem está andando ou não

#Importa as imagens do plano de fundo
listBgimages = [
    pygame.image.load("assets/Apocalipse/apocalipse1/Bright/clouds1.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/apocalipse1/Bright/clouds2.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/apocalipse1/Bright/ground&houses_bg.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/apocalipse1/Bright/ground&houses2.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/apocalipse1/Bright/ground&houses.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/apocalipse1/Bright/fence.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/apocalipse1/Bright/road.png").convert_alpha(),
]

# velocidades de cada imagem dp plano de fundo
listaBgVelocidades = [1, 3, 5, 9, 12, 15, 16] 

# Posições de cada imagem do plamo de fundo
listaBgPosicoes = [0 for _ in range(len(listBgimages))] 

#loop que redimenciona as imagens do plano de fundo
for i in range(len(listBgimages)):
    listBgimages[i] = pygame.transform.scale(listBgimages[i], tamanho)

#Variável para determinar altura do personagem em relação ao "Chão"
ALTURA_CHAO = 530
VELOCIDADE_PERSONAGEM = 10

# LOOP PRINCIPAL
while True:

    # Loop que verifica todos os eventos que acontecem no jogo
    for event in pygame.event.get():

        # Verifica se o evento é de fechar a janela
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha o jogo
            exit() # Fecha o programa

    tela.fill((255, 255, 255)) # Preenche a tela com a cor branca

    # Percorre todas as imagens do plano para movimentar
    for i in range(len(listBgimages)):
        if estaAndando:
            # move a imagem para a esquerda
            listaBgPosicoes[i] -= listaBgVelocidades[i] * VELOCIDADE_PERSONAGEM * dt *  direcaoPersonagem 

        #verifica se a imagem saiu da tela para a esquerda
        if listaBgPosicoes[i] <= -tamanho[0]:
            listaBgPosicoes[i] = 0 #Retorna a imagem para a posição inicial

        #verifica se a imagem saiu da tela para a direita
        if listaBgPosicoes[i] >= tamanho[0]:
            listaBgPosicoes[i] = 0  

    # Desenha o plano de fundo
    for i in range(len(listBgimages)):
        # Desenha a imagem do plano de fundo que está na tela
        tela.blit(listBgimages[i], (listaBgPosicoes[i],0))

        # Desenha a imagem do plano de fundo que esta fora da tela na direita
        tela.blit(listBgimages[i], (listaBgPosicoes[i] + tamanho[0], 0))

        # Desenha a iamgem do plano de fundo que esta fora da tela na esquerda
        tela.blit(listBgimages[i], (listaBgPosicoes[i] + -tamanho[0], 0))


    # Soma o tempo que se passou desde o último frame
    tempoAnimacaoIdle += dt

    # Verifica se o tempo de animação do personagem parado é maior ou igual ao tempo de animação
    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        # Atualiza o frame do personagem parado de acordo com a lista de frames
        indexFrameIdle = (indexFrameIdle + 1) % len(listFramesIdle)
        tempoAnimacaoIdle = 0.0 # Reseta o tempo entre os frames

    # Atualiza a animação do personagem andando
    tempoAnimacaoWalk += dt
    
    # Verifica se o tempo de animação do personagem andando é maior ou igual ao tempo de animação
    if tempoAnimacaoWalk >= 1 / velocidadeAnimacaoWalk:
        # Atualiza o frame do personagem andando
        indexFrameWalk = (indexFrameWalk + 1) % len(listFramesWalk)
        tempoAnimacaoWalk = 0.0

    # Atualiza a animação do personagem pulando
    tempoAnimacaoJump += dt

    # Verifica se o tempo de animação do personagem pulando é maior ou igual ao tempo de animação
    if tempoAnimacaoJump >= 1 / velocidadeAnimacaoJump:
        # Atualiza o frame do personagem pulando
        indexFrameJump = (indexFrameJump + 1) % len(listFramesJump)
        tempoAnimacaoJump = 0.0

    # Verifica se o personagem está andando
    estaAndando = False

    # Pega as teclas que foram pressionadas
    listTeclas = pygame.key.get_pressed()

    if listTeclas[pygame.K_LEFT]: # Verifica se a tecla esquerda foi pressionada
        personagemRect.x -= 200 * dt # Movimenta o personagem para a esquerda
        direcaoPersonagem = -1 # Define a direção do personagem para a esquerda
        estaAndando = True # Define que o personagem está andando

    if listTeclas[pygame.K_RIGHT]:
        personagemRect.x += 200 * dt # Movimenta o personagem para a direita
        direcaoPersonagem = 1
        estaAndando = True

    if listTeclas[pygame.K_SPACE]: # Verifica se a tecla espaço foi pressionada
        if personagemRect.centery == ALTURA_CHAO: # Verifica se o personagem está no chão
            gravidade = -30 # Define como negativo para o personagem subir
            indexFrameJump = 0 # Reseta o frame do pulo

    # Gravidade Aumenta
    gravidade += 2

    # Atualiza a posição Y do personagem de acordo com a gravidade
    personagemRect.y += gravidade

    # Verifica se o personagem está no chão
    if personagemRect.centery >= ALTURA_CHAO:
        personagemRect.centery = ALTURA_CHAO

    # Desenha o personagem
    if gravidade < 0: # Verifica se o personagem está subindo
        frame = listFramesJump[indexFrameJump]
    else:
        if estaAndando: # Verifica se o personagem está andando
            frame = listFramesWalk[indexFrameWalk]
        else: # Caso contrário, o personagem está parado
            frame = listFramesIdle[indexFrameIdle]

    if direcaoPersonagem == -1: # Verifica se o personagem está olhando para a esquerda e inverte a imagem
        frame = pygame.transform.flip(frame, True, False) # Inverte a imagem

    tela.blit(frame, personagemRect) # Desenha o personagem na tela

    pygame.display.update() # Atualiza a tela

    dt = relogio.tick(60) / 1000 # Define o tempo de cada frame em segundos