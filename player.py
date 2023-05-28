import pygame
from enum import Enum
from commonUtils import commonUtils


class Player:
    photo = './player.png'

    def __init__(self, leftX, rightX, objectY, screen):
        self.rightX = rightX
        self.leftX = leftX
        self.objectY = objectY  # למטה, מיקום סופי ולא משתנה
        self.screen = screen
        # Loading image
        self.playerPhoto = pygame.image.load(self.photo)
        self.currentPos = commonUtils.PositionLeftRight.RIGHT

    def first_draw(self):
        self.draw(self.rightX)

    def moveRight(self):
        self.draw(self.rightX)
        self.currentPos = commonUtils.PositionLeftRight.RIGHT

    def moveleft(self):
        self.draw(self.leftX)
        self.currentPos = commonUtils.PositionLeftRight.LEFT

        return self.currentPos


    def getPlayerPos(self) -> commonUtils.PositionLeftRight:
        return self.currentPos

    def draw(self, where_to_draw):
        self.objectX = where_to_draw
        self.screen.blit(self.playerPhoto,(self.objectX, self.objectY))
