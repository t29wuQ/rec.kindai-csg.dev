import cv2
import time

def recording_save_img(capture):
    while(True):
        ret, frame = capture.read()
        cv2.imwrite('/home/recorder/rec.kindai-csg.dev/latest.jpg', frame)
        cv2.imwrite("/home/recorder/rec.kindai-csg.dev/recording"+str(time.time())+'.jpg', frame)
 