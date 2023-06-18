
from cv2 import *
import cv2
from faceRecognition import Facial
from Emotion import Emotion

class Camera:
    CAPTURE_TIME_INTERVAL = 50  # in milli-seconds - 20 times in a second

    def __init__(self):
        self.emotion = Emotion.get_instance()

    #מצלם כל פעם פריים, שם אותו כפרמטר לפוקציה שבודקת את הרגש ומשנה את EMOTION לפיו (אחרי ניתוח רגשות)
    def mainProcess(self):
        lastEmotion = Emotion.EMOTION.START
        self.vc = cv2.VideoCapture(0)

        if self.vc.isOpened():  # try to get the first frame
            rval, frame = self.vc.read()
        else:
            rval = False

        while rval:
            rval, frame = self.vc.read()
            self.emotion.setEmotion(Facial.whatFacialExpression(frame, lastEmotion))

            if self.emotion.getEmotion() != lastEmotion:
                lastEmotion = self.emotion.getEmotion()

            key = cv2.waitKey(self.CAPTURE_TIME_INTERVAL)
        #    if key == 27:  # exit on ESC
         #       break

        self.finish()

    def finish(self):
        self.vc.release()

