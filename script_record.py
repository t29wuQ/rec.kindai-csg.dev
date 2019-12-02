import cv2
import time

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
    cv2.imwrite("/home/recorder/rec.kindai-csg.dev/recording"+str(time.time())+'.jpg', frame)
 