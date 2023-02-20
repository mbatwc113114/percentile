import pygame
import pygame.locals
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Input App")

# Set up the font
font = pygame.font.Font(None, 32)

# Function to display alert box with input value
def display_alert(input_text):
    alert_text = font.render(f"Input value is {input_text}", True, (255, 255, 255))
    alert_rect = alert_text.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(alert_text, alert_rect)
    pygame.display.update()
    pygame.time.delay(2000)

# Set up the input field
input_text = ""
input_rect = pygame.Rect(50, 50, 200, 50)

# Set up the button
button_text = font.render("Display Input", True, (255, 255, 255))
button_rect = pygame.Rect(50, 150, 200, 50)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.unicode.isalnum():
                input_text += event.unicode
            elif event.key == K_BACKSPACE:
                input_text = input_text[:-1]
        elif event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                display_alert(input_text)
                input_text = ""

    # Draw the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
    input_surface = font.render(input_text, True, (255, 255, 255))
    screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
    pygame.draw.rect(screen, (255, 0, 0), button_rect)
    screen.blit(button_text, (button_rect.x + 5, button_rect.y + 5))

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
