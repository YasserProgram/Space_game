import pygame
import random

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana del juego
WIDTH = 800
HEIGHT = 600

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Crear la ventana del juego
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

# Clase para representar al jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
    
    def update(self):
        # Obtener la posición del mouse
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = mouse_pos

# Clase para representar a los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(1, 3)
    
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(1, 3)

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Crear jugador
player = Player()
all_sprites.add(player)

# Crear enemigos
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Variable para controlar el estado del juego
game_over = False

# Bucle principal del juego
while not game_over:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Actualizar
    all_sprites.update()

    # Comprobar colisiones del jugador con los enemigos
    if pygame.sprite.spritecollide(player, enemies, True):
        # ¡Aquí puedes agregar cualquier acción que ocurra cuando el jugador colisione con un enemigo!
        pass

    # Verificar si todos los enemigos han sido eliminados
    if len(enemies) == 0:
        game_over = True
        print("¡Ganaste! Has eliminado todos los cubos rojos.")

    # Dibujar
    window.fill(BLACK)
    all_sprites.draw(window)

    # Actualizar la pantalla
    pygame.display.flip() 

# Salir del juego
pygame.quit()
