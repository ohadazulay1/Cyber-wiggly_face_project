import time
from threading import Thread
import pygame
import random
from squareObject import SquareObject
from player import Player
from Emotion import Emotion
from stopwatch import Stopwatch
from commonUtils import commonUtils
from highScore import HighScore
from messageToPresent import MessageToPresent
from clientHelperForOnlineEndGame import ClientHelperForOnlineEndGame

class Graphics:
    right_side = 900 #הX של הצד הימני של הלוח
    left_side = 600 #הX של הצד השמאלי של הלוח


    starter_y_for_objects = 30 #הגובה ההתחלתי של המכשולים
    y_for_player = 900 #הגובה של השחקן
    time_to_add_object = 3 #כל כמה זמן להוסיף מכשול
    time_to_change_speed = 1 #כל כמה זמן להגביר מהירות
    increase_speed_by = 0.09 #בכמה להגביר את המהירות - מוסיפים בכל שנייה (כל כמה זמן...) את זה
    start_speed = 3 #מהירות התחלתית

    WHITE = (255, 255, 255)
    onlinePlayerWasHit = False

    def __init__(self, oppUserName):
        self.onlineClient = ClientHelperForOnlineEndGame.get_instance()
        self.soloGame = True
        if oppUserName != "":
            self.onlineClient.newGame()
            self.oppUserName = oppUserName
            checkIfLostTread = Thread(target=self.onlineClient.didIWin)
            checkIfLostTread.start()
            self.soloGame = False

        #  self.alreadyLost = False
        #מאתחל את הלוח
        pygame.init()
        # Set up the drawing window
        pygame.display.set_caption("GAME")
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
        if self.soloGame:
            self.highScorePressent = HighScore(100, 250, self.screen)


    def initialize_game(self):
        self.alreadyLost = False
        self.alreadyWon = False
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

            if self.alreadyLost or self.alreadyWon:
                keys = pygame.key.get_pressed()
                # if Escape key pressed exit the game
                if keys[pygame.K_ESCAPE]:
                    running = False

            else:
                keys = pygame.key.get_pressed()
                # if Escape key pressed exit the game
                if keys[pygame.K_ESCAPE]:
                    if not self.soloGame:
                        self.onlineClient.IHaveLost(self.oppUserName)
                    running = False

                if not self.soloGame:
                    if playerWasHit == False:
                        if not self.onlineClient.getGameOn():
                            self.alreadyWon = True
                            MessageToPresent.youWonMassage(self.screen, self.oppUserName)
                        #    keys = pygame.key.get_pressed()
                            # if Escape key pressed exit the game
                         #   if keys[pygame.K_ESCAPE]:
                          #      running = False

                #  if self.onlinePlayerWasHit:
               #     MessageToPresent.youWonMassage(self.screen, self.oppUserName)



                if playerWasHit:
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


                    if (time.time() - self.speed_time >= self.time_to_change_speed):
                        self.speed_time = time.time()
                        self.speed += self.increase_speed_by
                        print(self.speed)
                    if (self.emotion.getEmotion() == Emotion.EMOTION.HAPPY):
                        self.player.moveleft()
                    else:
                        self.player.moveRight()

                    for singleObject in self.all_objects:
                        singleObject.moveDown(self.speed)

                        if (singleObject.getPosY() + 170 > self.y_for_player):
                            # check if player was hit
                            if (singleObject.getPosLeftRight() == self.player.getPlayerPos()):
                                playerWasHit = True
                                self.stopwatch.stop()
                                if not self.soloGame:
                                    if not self.alreadyLost:
                                        self.alreadyLost = True
                                        self.onlineClient.IHaveLost(self.oppUserName)
                                        MessageToPresent.oppWonMassage(self.screen, self.oppUserName)

                                else:
                                    highScoreBroke = self.highScorePressent.updateHighScore(self.stopwatch.get_elapsed_time())
                                    print("highscorebroke; " + str(highScoreBroke))
                                    MessageToPresent.drawHitMessage(self.screen, highScoreBroke)
                                    if highScoreBroke:
                                        self.stopwatch.draw()
                                        self.highScorePressent.draw()
                                break
                            else:
                                self.all_objects.remove(singleObject)

                    pygame.display.update()
                    self.clock.tick(60)

                    self.screen.fill(self.WHITE)

                    self.stopwatch.draw()
            #        MessageToPresent.oppWonMassage(self.screen, "lol")
                    MessageToPresent.drawQuitMessage(self.screen)
                    if not self.soloGame:
                        MessageToPresent.drawOppName(self.screen, self.oppUserName)
                    else:
                        self.highScorePressent.draw()
        pygame.quit()