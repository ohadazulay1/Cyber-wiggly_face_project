import time
import pygame
import random
from squareObject import SquareObject
from player import Player
from Emotion import Emotion
from stopwatch import Stopwatch
from commonUtils import commonUtils
from highScore import HighScore
from messageToPresent import MessageToPresent

class Graphics:
    right_side = 900 #הX של הצד הימני של הלוח
    left_side = 600#הX של הצד השמאלי של הלוח


    starter_y_for_objects = 30#הגובה ההתחלתי של המכשולים
    y_for_player = 900#הגובה של השחקן
    time_to_add_object = 3#כל כמה זמן להוסיף מכשול
    time_to_change_speed = 5#כל כמה זמן להגביר מהירות
    increase_speed_by = 0.75  #בכמה להגביר את המהירות - מכפילים את זמן השהייה בין תזוזה לתזוזה
    start_speed = 0.05#מהירות התחלתית

    WHITE = (255, 255, 255)


    def __init__(self):
        #מאתחל את הלוח
        pygame.init()
        # Set up the drawing window
        pygame.display.set_caption("test")
        # Initializing surface
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Fill the background with white
        self.screen.fill((255, 255, 255))

        self.clock = pygame.time.Clock()

        self.emotion = Emotion.get_instance()

        # create the player
        self.player = Player(self.left_side, self.right_side, self.y_for_player, self.screen)
        self.player.first_draw()

        self.stopwatch = Stopwatch(self.screen)
        self.highScorePressent = HighScore(100, 250, self.screen)


    def initialize_game(self):
        self.startingTime = time.time()
        self.speed = self.start_speed
        self.speed_time = time.time()
        self.add_object_time = time.time()
        self.all_objects = []
        self.counter, self.text = 10, '10'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.stopwatch.start()



    def playerManager(self):
        X_average = (self.left_side + self.right_side) / 2#לנקודת ההתחלה של השחקן
        player = Player(X_average, self.y_for_player, self.screen)
        player.first_draw()
        if self.emotion.getEmotion() == Emotion.EMOTION.HAPPY:
            player.moveRight()
        elif self.emotion.getEmotion() == Emotion.EMOTION.SAD:
            player.moveleft()


    def objectsManeger(self):
        self.initialize_game()

        clock = pygame.time.Clock()
        font = pygame.font.SysFont('Consolas', 30)

        # Run until the user asks to quit
        running = True
        playerWasHit = False
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    self.counter += 1
                    self.text = str(self.counter).rjust(3)
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            # if Escape key pressed exit the game
            if keys[pygame.K_ESCAPE]:
                running = False

            if (playerWasHit):
                # if player was hit, and space key pressed, restart game
                if keys[pygame.K_SPACE]:
                    self.initialize_game()
                    playerWasHit = False

            else: # Player is not hit yet
                if (time.time() - self.add_object_time >= self.time_to_add_object):
                    self.add_object_time = time.time()
                    which_side_rand = random.randint(1,2)
                    if which_side_rand == 1: #1 מסמל את צד שמאל
                        self.all_objects.append(SquareObject(self.left_side, commonUtils.PositionLeftRight.LEFT, self.starter_y_for_objects, self.screen))

                    if which_side_rand == 2: #2 מסמל את צד ימין
                        self.all_objects.append(SquareObject(self.right_side, commonUtils.PositionLeftRight.RIGHT, self.starter_y_for_objects, self.screen))

                for singleObject in self.all_objects:
                    singleObject.moveDown()


                    if (singleObject.getPosY() + 170 > self.y_for_player):
                        # check if player was hit
                        if (singleObject.getPosLeftRight() == self.player.getPlayerPos()):
                            playerWasHit = True
                            self.stopwatch.stop()

                            highScoreBroke = self.highScorePressent.updateHighScore(self.stopwatch.get_elapsed_time())
                            MessageToPresent.drawHitMessage(self.screen, highScoreBroke)
                            if highScoreBroke:
                                self.stopwatch.draw()
                                self.highScorePressent.draw()
                            break
                        else:
                            self.all_objects.remove(singleObject)

                if(time.time() - self.speed_time >= self.time_to_change_speed):
                    self.speed_time = time.time()
                    self.speed *= self.increase_speed_by

                if (self.emotion.getEmotion() == Emotion.EMOTION.HAPPY):
                    self.player.moveleft()
                else:
                    self.player.moveRight()

                pygame.display.update()
                self.clock.tick(60)

                self.screen.fill(self.WHITE)

                self.stopwatch.draw()
                self.highScorePressent.draw()
                MessageToPresent.drawQuitMessage(self.screen)

        pygame.quit()