import pygame
import json
from pydialogue import generate_ai_response


#screen size 
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h



#settings for game
pygame.init()

width = int(screen_width * 0.8)
height = int(screen_height * 0.8)

screen = pygame.display.set_mode((width, height), pygame.RESIZEABLE)
pygame.display.set_caption("Pygame dialogue testing")


