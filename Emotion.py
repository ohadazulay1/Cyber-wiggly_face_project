from enum import Enum

class Emotion:

    _instance = None

    EMOTION = Enum("Emotion", ["START", "SAD", "HAPPY"])
    INITIAL_STATE = EMOTION.HAPPY

    def __init__(self):
        if Emotion._instance is not None:
            raise Exception("This class is a singleton. Use get_instance() to obtain an instance.")

        Emotion._instance = self
        self.setEmotion(self.EMOTION.START)

    @staticmethod
    def get_instance():
        if Emotion._instance is None:
            Emotion()
        return Emotion._instance

    def setHappy(self):
        self.emotion = self.EMOTION.HAPPY

    def setSad(self):
        self.emotion = self.EMOTION.SAD


    def setEmotion(self, emotion: EMOTION):
        self.emotion = emotion

    def getEmotion(self) -> str:
        return self.emotion

