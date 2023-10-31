import pygame
import sys

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Tamaño de la ventana
WINDOW_SIZE = (800, 600)

# Inicializar la ventana
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Dibujo de Figuras")

# Definir las dimensiones de las figuras
current_shape = None
drawing = False  # Variable para controlar el dibujo

# Función para dibujar el menú
def draw_menu():
    pygame.draw.rect(screen, WHITE, (0, 0, WINDOW_SIZE[0], 50))
    pygame.draw.line(screen, RED, (200, 0), (200, 50), 2)
    pygame.draw.line(screen, RED, (400, 0), (400, 50), 2)
    pygame.draw.line(screen, RED, (600, 0), (600, 50), 2)
    font = pygame.font.Font(None, 36)
    text = font.render("Triángulo", True, RED)
    screen.blit(text, (70, 10))
    text = font.render("Círculo", True, RED)
    screen.blit(text, (270, 10))
    text = font.render("Cuadrado", True, RED)
    screen.blit(text, (470, 10))
    text = font.render("Borrar", True, RED)
    screen.blit(text, (670, 10))

# Ciclo principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_shape = None
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Verificar si se hace clic en el menú
            if event.pos[1] < 50:
                if event.pos[0] < 200:
                    current_shape = "triangle"
                elif 200 <= event.pos[0] < 400:
                    current_shape = "circle"
                elif 400 <= event.pos[0] < 600:
                    current_shape = "square"
                elif 600 <= event.pos[0] < 800:
                    current_shape = "erase"
            else:
                if current_shape == "erase":
                    # Borrar el área de dibujo
                    screen.fill(WHITE)
                else:
                    start_pos = event.pos
                    drawing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            end_pos = event.pos
            if current_shape == "triangle":
                # Dibujar un triángulo rectángulo en color rojo
                pygame.draw.polygon(screen, RED, [start_pos, (end_pos[0], start_pos[1]), end_pos])
            elif current_shape == "circle":
                # Dibujar un círculo en color rojo
                radius = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5
                pygame.draw.circle(screen, RED, start_pos, int(radius), 2)
            elif current_shape == "square":
                # Dibujar un cuadrado en color rojo
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]
                rect = pygame.Rect(start_pos, (width, height))
                pygame.draw.rect(screen, RED, rect, 2)

    # Dibujar el menú
    draw_menu()

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
