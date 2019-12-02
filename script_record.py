import cv2
import time

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
    cv2.imwrite(str(time.time())+'.jpg', frame)
 