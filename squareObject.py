import pygame
from enum import Enum
from commonUtils import commonUtils

class SquareObject:
    #photo = 'C:/Users/azula/OneDrive/תמונות/forProject/construction_barrier1.png'
    photo = './blocker.png'
    objectX = 0
    objectY = 0
    screen = ''

    def __init__ (self, objectX, squarePosLeftRight, objectY, screen):
        self.objectX = objectX
        self.objectY = objectY
        self.screen = screen
        # Loading image
        self.objectPhoto = pygame.image.load(self.photo)
        self.squarePosLeftRight = squarePosLeftRight


    def getPosLeftRight(self) -> commonUtils.PositionLeftRight:
        return self.squarePosLeftRight

    def getPosY(self) -> str:
        return self.objectY

    def draw(self):
        self.screen.blit(self.objectPhoto,(self.objectX, self.objectY))

    def moveDown(self):
        self.objectY += 5
        self.draw()