from fer import FER
import cv2
from Emotion import Emotion

class Facial:

    @staticmethod
    def whatFacialExpression(filePlace, img, lastEmotion) -> Emotion.EMOTION:

        img = cv2.imread(filePlace)
        detector = FER()
        emotions = detector.detect_emotions(img)

        if emotions:
            sad_value = emotions[0]['emotions']['sad']
            happy_value = emotions[0]['emotions']['happy']

            if happy_value > sad_value:
                return Emotion.EMOTION.HAPPY
            else:
                return Emotion.EMOTION.SAD
        else:
            return lastEmotion

