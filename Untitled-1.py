import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 3. Set the window title
pygame.display.set_caption("Asteroid Dodger")

# 4. Game colors (RGB tuples)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0) # New color for the player

# --- Player Properties ---
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
# Initial position: bottom center of the screen
player_x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10 # 10 pixels from the bottom edge
player_speed = 5 # How many pixels the player moves per frame

# 5. Game loop control
running = True
clock = pygame.time.Clock() # Helps control the frame rate

# 6. Main game loop
while running:
    # 7. Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Player Movement Input ---
    # Get all currently pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: # If left arrow key is pressed
        player_x -= player_speed
    if keys[pygame.K_RIGHT]: # If right arrow key is pressed
        player_x += player_speed

    # --- Keep Player On Screen ---
    # Prevent player from moving off the left edge
    if player_x < 0:
        player_x = 0
    # Prevent player from moving off the right edge
    if player_x > SCREEN_WIDTH - PLAYER_WIDTH:
        player_x = SCREEN_WIDTH - PLAYER_WIDTH

    # 8. Game logic updates (e.g., player movement, asteroid movement)
    # (We'll add more here in the next steps)

    # 9. Drawing (rendering)
    screen.fill(BLACK) # Fill the screen with black each frame

    # --- Draw the Player ---
    # pygame.draw.rect(surface, color, rect_tuple)
    # rect_tuple is (x, y, width, height)
    player_rect = (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    pygame.draw.rect(screen, RED, player_rect) # Draw the player as a red rectangle

    # 10. Update the full display
    pygame.display.flip()

    # 11. Control frame rate
    clock.tick(60)

# 12. Quit Pygame
pygame.quit()
print("Game Exited Successfully!")