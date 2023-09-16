import cv2
import mediapipe as mp
import time


camera = cv2.VideoCapture("vid.mp4")


while True:
    success, img = camera.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(20) & 0xFF == ord("d"):
        break

camera.release()
cv2.destroyAllWindows()
