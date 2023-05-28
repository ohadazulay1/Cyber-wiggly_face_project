import time
import pygame
from commonUtils import commonUtils

class Stopwatch:

    bg_color = (255, 255, 255)  # White
    text_color = (0, 0, 0)  # Black
    X_Pos = 100
    Y_Pos = 100

    def __init__(self, screen):
        self.start_time = 0
        self.screen = screen
        self.running = False
        self.lastElapseTime = 0

    def start(self):
        self.start_time = time.time()
        self.running = True
        self.lastElapseTime = 0

    def stop(self):
        self.lastElapseTime = self.get_elapsed_time()
        self.running = False

    def reset(self):
        self.start_time = 0
        self.running = False
        self.lastElapseTime = 0

    def get_elapsed_time(self) -> float:
        if self.running:
            elapsed_time = time.time() - self.start_time
        else:
            elapsed_time = self.lastElapseTime

        return elapsed_time


    def draw(self):
        font = pygame.font.Font(None, 100)
        time_text = commonUtils.get_time_str(self.get_elapsed_time())
        text = font.render(time_text, True, self.text_color)

        self.screen.blit(text, (self.X_Pos, self.Y_Pos))
