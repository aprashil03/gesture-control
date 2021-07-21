import mediapipe as mp
import cv2
import json
import methods

with open('config.json') as config:
    configDict = json.load(config)


handObj = methods.Handle(**configDict)
cap = handObj.init_video()

while cap.isOpened():
    success, image = cap.read()

    if not success:
        print('Empty camera frame...')
        continue

    image, results = handObj.process_image(image)

    handObj.process_positions(image, results)

    cv2.imshow('Gesture Navigation', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release() # release sys resources