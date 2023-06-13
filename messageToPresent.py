import pygame

class MessageToPresent:

    @staticmethod
    def drawHitMessage(screen, brokeHighScore: bool):
        BG_COLOR = (255, 255, 255)  # White
        TEXT_COLOR_RED = (255, 0, 0)  # Red
        TEXT_COLOR_GREEN = (0, 255, 0)  # Green
        TEXT_COLOR_BLACK = (0, 0, 0)  # Black
        X_POS_HIT = 670
        Y_POS_HIT = 400
        X_POS_SPACE = 690
        Y_POS_SPACE = 600
        X_POS_RECORD = 560
        Y_POS_RECORD = 500

        messageHit = "You were hit!!"
        messageSpace = "Press <Space> to Restart"

        font = pygame.font.Font(None, 100)
        text = font.render(messageHit, True, TEXT_COLOR_RED, BG_COLOR)
        screen.blit(text, (X_POS_HIT, Y_POS_HIT))

        font = pygame.font.Font(None, 50)
        text = font.render(messageSpace, True, TEXT_COLOR_BLACK, BG_COLOR)
        screen.blit(text, (X_POS_SPACE, Y_POS_SPACE))

        if brokeHighScore:
            messageRecord = "You broke your Record!"
            font = pygame.font.Font(None, 100)
            text = font.render(messageRecord, True, TEXT_COLOR_GREEN, BG_COLOR)
            screen.blit(text, (X_POS_RECORD, Y_POS_RECORD))

    @staticmethod
    def drawQuitMessage(screen):
        BG_COLOR = (255, 255, 255)  # White
        TEXT_COLOR = (0, 0, 0)  # Black
        X_POS = 100
        Y_POS = 1000

        font = pygame.font.Font(None, 35)
        message = "Press <Escape> to Quit"

        text = font.render(message, True, TEXT_COLOR, BG_COLOR)
        screen.blit(text, (X_POS, Y_POS))


    @staticmethod
    def drawOppName(screen, oppUserName):
        BG_COLOR = (255, 255, 255)  # White
        TEXT_COLOR = (0, 0, 0)  # Black
        X_POS = 480
        Y_POS = 100

        font = pygame.font.Font(None, 50)
        message = "You are playing against " + oppUserName

        text = font.render(message, True, TEXT_COLOR, BG_COLOR)
        screen.blit(text, (X_POS, Y_POS))

    @staticmethod
    def oppWonMassage(screen, oppUserName):
        BG_COLOR = (255, 255, 255)  # White
        TEXT_COLOR_BLACK = (0, 0, 0)  # Black
        TEXT_COLOR_RED = (255, 0, 0)  # Red
        X_POS_OPP_WON = 600
        Y_POS_OPP_WON = 450
        X_POS_ESC = 620
        Y_POS_ESC = 510

        font = pygame.font.Font(None, 75)
        messageYouLost = "You lost the game against " + oppUserName
        text = font.render(messageYouLost, True, TEXT_COLOR_RED, BG_COLOR)
        screen.blit(text, (X_POS_OPP_WON, Y_POS_OPP_WON))

        font = pygame.font.Font(None, 50)
        messagePressEsc = "press escape to exit to main window"
        text = font.render(messagePressEsc, True, TEXT_COLOR_BLACK, BG_COLOR)
        screen.blit(text, (X_POS_ESC, Y_POS_ESC))



    @staticmethod
    def youWonMassage(screen, oppUserName):
        BG_COLOR = (255, 255, 255)  # White
        TEXT_COLOR_BLACK = (0, 0, 0)  # Black
        TEXT_COLOR_GREEN = (0, 255, 0)  # Green
        X_POS_YOU_WON = 600
        Y_POS_YOU_WON = 450
        X_POS_ESC = 620
        Y_POS_ESC = 510

        font = pygame.font.Font(None, 75)
        messageYouLost = "You won the game against " + oppUserName
        text = font.render(messageYouLost, True, TEXT_COLOR_GREEN, BG_COLOR)
        screen.blit(text, (X_POS_YOU_WON, Y_POS_YOU_WON))

        font = pygame.font.Font(None, 50)
        messagePressEsc = "press escape to exit to main window"
        text = font.render(messagePressEsc, True, TEXT_COLOR_BLACK, BG_COLOR)
        screen.blit(text, (X_POS_ESC, Y_POS_ESC))