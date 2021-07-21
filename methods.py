import mediapipe as mp
import vectorCalc as vc
import cv2

class Handle:

    def __init__(
        self,
        video_source_index=0,
        static_image_mode=False,
        max_num_hands=1,
        min_det_conf=0.7,
        min_track_conf=0.7,
        draw_points=False   
    ):


        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils

        self.video_source_index = video_source_index
        self.draw_points = draw_points

        self.hands = self.mp_hands.Hands(
            static_image_mode,
            max_num_hands,
            min_det_conf,
            min_track_conf
        )


    def init_video(self):

        cap = cv2.VideoCapture(self.video_source_index)
        _, image = cap.read()
        image_height, image_width, _ = image.shape

        self.resolution = (image_width, image_height)

        return (cap)

    def process_image(self, image):

        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False # for optimization, 2 lines below aswell
        results = self.hands.process(image)
        image.flags.writeable = True
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        return (image, results)

    def process_positions(self, image, results):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                if self.draw_points:
                    self.mp_drawing.draw_landmarks(
                            image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )

                finger_pts = []

                for id, lm in enumerate(hand_landmarks.landmark):
                        if id not in [0,1,2,5,7,9,11,13,15,17,19]:
                            finger_pts.append([id, lm.x, lm.y, lm.z])
                        if id == 0:
                            base = [id, lm.x, lm.y, lm.z]

                finger_pts = [[base] + finger_pts[x:x+2] for x in range(0, 10, 2)]

                finger_angles = vc.calcAngles(finger_pts, self.resolution)

                print(finger_angles)


