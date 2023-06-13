import pygame
from userNameClass import UserNameClass
from client import Client
from commonUtils import commonUtils

class HighScore:
    BG_COLOR = (255, 255, 255)  # White
    TEXT_COLOR = (0, 0, 0)  # Black
    X_POS = 1000
    Y_POS = 100

    def __init__(self, X_pos, Y_pos, screen):
        #self.X_pos = X_pos
        #self.Y_pos = Y_pos
        self.screen = screen
        self.client = Client.get_instance()
        self.usernameInstance = UserNameClass.get_instance()
        self.username = self.usernameInstance.getUserName()
        self.highScore = self.client.getSelfHighScore(self.username)

    def updateHighScore(self, score) -> bool:
        if score > self.highScore:
            self.client.setSelfHighScore(self.username, score)
            self.highScore = score
            return True
        else:
            return False

    def draw(self):
        font = pygame.font.Font(None, 50)
        highScoreText = commonUtils.get_time_str(self.highScore)

        highScoreToPresent = self.username + " high Score: " + highScoreText
        text = font.render(highScoreToPresent, True, self.TEXT_COLOR, self.BG_COLOR)

        self.screen.blit(text, (self.X_POS, self.Y_POS))