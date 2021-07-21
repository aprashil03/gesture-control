import mediapipe as mp
import cv2

class Handle:

    def __init__(
        self,
        video_source_index=0,
        static_image_mode=False,
        max_num_hands=1,
        min_det_conf=0.7,
        min_track_conf=0.5,
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

        return ((image_width, image_height), cap)

    def process_image(self, image):

        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False # for optimization, 2 lines below aswell
        results = self.hands.process(image)
        image.flags.writeable = True
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        return (image, results)

    def render_points(self, image, results):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                        image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )


