import mediapipe as mp
import cv2
import methods

handObj = methods.Handle(video_source_index=0, draw_points=True)
resolution, cap = handObj.init_video()

while cap.isOpened():
    success, image = cap.read()

    if not success:
        print('Empty camera frame...')
        continue

    image, results = handObj.process_image(image)

    if handObj.draw_points:
        handObj.render_points(image, results)

    cv2.imshow('Gesture Navigation', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release() # release sys resources