import cv2
import pygame
from hand_tracker import HandTracker


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(0)

        self.frame = None

        self.hand_tracker = HandTracker()

    def update(self):

        success, frame = self.cap.read()

        if not success:
            return

        frame = cv2.flip(frame, 1)

        self.hand_tracker.process(frame)

        frame = self.hand_tracker.draw(frame)

        self.frame = frame

        self.hand_dx = self.hand_tracker.hand_dx

        self.hand_dy = self.hand_tracker.hand_dy

        self.is_fist = self.hand_tracker.is_fist

        self.hand_open_event = self.hand_tracker.hand_open_event

    def draw(self, screen, x, y, w, h):

        if self.frame is None:
            return

        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

        frame = cv2.resize(frame, (w, h))

        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

        screen.blit(surface, (x, y))

    def release(self):

        self.cap.release()
    def get_hand_position(self):

        return self.hand_tracker.get_palm_position()
    