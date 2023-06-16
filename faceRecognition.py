from fer import FER
from Emotion import Emotion

class Facial:

    #מחזירה את הרגש שיש בפנים בתמונה שקובץ שהתקבל
    @staticmethod
    def whatFacialExpression(frame, lastEmotion) -> Emotion.EMOTION:

        detector = FER()
        emotions = detector.detect_emotions(frame)

        if emotions:
            sad_value = emotions[0]['emotions']['sad']
            happy_value = emotions[0]['emotions']['happy']

            if happy_value > sad_value:
                return Emotion.EMOTION.HAPPY
            else:
                return Emotion.EMOTION.SAD
        else:
            return lastEmotion

