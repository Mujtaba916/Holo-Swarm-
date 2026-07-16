import cv2
import mediapipe as mp
import math


class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils

        self.results = None

        self.prev_x = None
        self.prev_y = None

        self.hand_dx = 0
        self.hand_dy = 0

        self.is_fist = False
        self.was_fist = False
        self.hand_open_event = False

        self.finger_count = 0

    def process(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(rgb)

        self.hand_dx = 0
        self.hand_dy = 0
        self.hand_open_event = False

        if not self.results.multi_hand_landmarks:
            return

        hand = self.results.multi_hand_landmarks[0]

        palm = hand.landmark[9]

        x = palm.x
        y = palm.y

        if self.prev_x is not None:

            self.hand_dx = x - self.prev_x
            self.hand_dy = y - self.prev_y

        self.prev_x = x
        self.prev_y = y

        wrist = hand.landmark[0]
        index_tip = hand.landmark[8]
        middle_tip = hand.landmark[12]

        d1 = math.hypot(
            index_tip.x - wrist.x,
            index_tip.y - wrist.y
        )

        d2 = math.hypot(
            middle_tip.x - wrist.x,
            middle_tip.y - wrist.y
        )

        self.was_fist = self.is_fist

        self.is_fist = (d1 < 0.18 and d2 < 0.18)

        if self.was_fist and not self.is_fist:
            self.hand_open_event = True

    def draw(self, frame):

        if self.results.multi_hand_landmarks:

            for hand in self.results.multi_hand_landmarks:

                self.drawer.draw_landmarks(
                    frame,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame

    def hand_detected(self):

        return self.results is not None and self.results.multi_hand_landmarks

    def get_palm_position(self):

        if self.results is None:
            return None

        if not self.results.multi_hand_landmarks:
            return None

        hand = self.results.multi_hand_landmarks[0]

        landmark = hand.landmark[9]

        return landmark.x, landmark.y
    def count_fingers(self):

     if not self.results.multi_hand_landmarks:
        return 0    


        hand=self.results.multi_hand_landmarks[0]

        count=0

        tips=[8,12,16,20]


        for tip in tips:

            if hand.landmark[tip].y < hand.landmark[tip-2].y:
                count +=1

        return count