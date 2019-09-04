import numpy as np
import cv2
from PIL import Image
import os

from image_processing import pre_initialisation
from image_processing import position_yeux_verticale
from image_processing import qualibrage
from image_processing import position_yeux_horizontal
from image_processing import association
from image_processing import pre_initialisation


def video_capture_yeux():
    """Here we lunch the video display (pc cam) with VideoCapture"""

    #We initialize list
    FIT_LIST = []
    LIST_RIGHT_LEFT = []
    QUALIFER_LIST = []

    video = cv2.VideoCapture(0)

    while(True):

        #Eyes haarcascade
        left_eye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')

        #We define the current frame and resize it
        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))

        #We try to detect eyes into the frame 
        eyes = left_eye.detectMultiScale(frame)

        #we fill in our list of the current position
        #of the eyes in order to make an average of
        #them and then to be able to continue them.
        if len(FIT_LIST) < 50:
            pre_initialisation(eyes, FIT_LIST, frame)
            print("initialisation")

        #Now we catch the current position and
        #if the eyes move by -5 pixels for example
        #(on the y-axis) it is because the person looked up.
        else:
            position1 = position_yeux_verticale(eyes, FIT_LIST, frame)
            position2 = position_yeux_horizontal(eyes, LIST_RIGHT_LEFT, frame)
            #
            association(position1, position2, FIT_LIST)


            QUALIFER_LIST.append(position1)
            qualibration = qualibrage(QUALIFER_LIST)
            if qualibration == "qualibration":
                FIT_LIST = []


            #If the person bent down, got up ...
            #We empty the list to re-initialize
            if position1 in ("the person bent down",
                             "the person got up",
                             "the person lifted his head",
                             "the person dropped his head"):

                FIT_LIST = []


        cv2.imshow('EYES CAPTURE', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()






if __name__ == "__main__":
    video_capture_yeux()












