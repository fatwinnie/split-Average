import cv2
import numpy as np
import os

#FPS=10
# Playing video from file:
cap = cv2.VideoCapture('video.avi')
#cap.set(cv2.CAP_PROP_FPS, FPS)

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
success=True
while success:
    # Capture frame-by-frame
    success, frame = cap.read()

   # save frame as JPEG file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)   # save frame as JPEG file

    if cv2.waitKey(10)==27:
        break
    currentFrame +=1
   #waitKey()只有搭配OpenCV視窗才有效果，沒有視窗的話無此暫停程式功能。
   #可以使用這個特性搭配while迴圈，讓圖片不斷顯示，直到按下某特定按鍵後才停止。
   #由於esc鍵的ASCII碼為27，所以程式只有按下esc鍵，程式才會跳出迴圈：


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
